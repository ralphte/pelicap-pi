#!/usr/bin/env python

import argparse
import os
import xml.etree.ElementTree as et

#set up arguments
parser = argparse.ArgumentParser()
parser.add_argument('-r', '--read', metavar='read', help='The packet dump to read', required=True)
parser.add_argument('-l', '--list', action='store_true', help='List results from packet dump', required=False)
write_group_target = parser.add_mutually_exclusive_group(required=False)
write_group_target.add_argument('-f', '--force-write', metavar='force-write', help='The packet dump to force write', required=False)
write_group_target.add_argument('-w', '--write', metavar='write', help='The packet dump to write', required=False)
group_target = parser.add_mutually_exclusive_group(required=True)
group_target.add_argument('-b', '--bssid', metavar='bssid', help='The BSSID to search for')
group_target.add_argument('-s', '--ssid', metavar='ssid', help='The SSID to search for')
parser.add_argument('-x', '--netxml', metavar='netxml', help='The .netxml to read', required=False)
args = parser.parse_args()

def write_to_file(read, write, bssid):
    #read files and write temporary output
    #look for a few packets displaying the SSID
    os.system('tshark -2 -c 5 -r {0} -w {1}.ssid -R "(wlan.bssid eq {2}) and ((wlan.fc.type_subtype eq 0x08) or '
              '(wlan.fc.type_subtype eq 0x05)) and not (wlan.ssid eq \\"\\")" '
              '2>/dev/null'.format(read, write, bssid))
    #look for WPA1/2-PSK
    os.system('tshark -2 -c 10 -r {0} -w {1}.psk -R \"(wlan.bssid eq {2}) and wlan.rsn.akms.type eq 2\" '
              '2>/dev/null'.format(read, write, bssid))
    #look for EAP-TLS
    os.system('tshark -2 -c 10 -r {0} -w {1}.eaptls -R \"(wlan.bssid eq {2}) and eap.type eq 13\" '
              '2>/dev/null'.format(read, write, bssid))
    #look for PEAP
    os.system('tshark -2 -c 10 -r {0} -w {1}.peap -R \"(wlan.bssid eq {2}) and eap.type eq 25\" '
              '2>/dev/null'.format(read, write, bssid))
    #look for open network
    os.system('tshark -2 -c 10 -r {0} -w {1}.openauth -R \"(wlan.bssid eq {2}) and ((wlan.fc.type_subtype eq 0x08) or '
              '(wlan.fc.type_subtype eq 0x05)) and not (wlan.tag.number eq 48)\" '
            '2>/dev/null'.format(read, write, bssid))
    #merge temporary outputs into final output
    os.system('mergecap -w {0} {0}.ssid {0}.psk {0}.eaptls {0}.peap {0}.openauth'.format(write))
    os.system('rm {0}.ssid {0}.psk {0}.eaptls {0}.peap {0}.openauth'.format(write))
    print "[+] Proof packets written successfully..."

def print_to_screen(read, bssid):
    #read files and look for a few packets displaying the SSID
    os.system('tshark -2 -c 5 -r {0} -R "(wlan.bssid eq {1}) and ((wlan.fc.type_subtype eq 0x08) or '
              '(wlan.fc.type_subtype eq 0x05)) and not (wlan.ssid eq \\"\\")" '
              '2>/dev/null'.format(read, bssid))
    #look for WPA1/2-PSK
    os.system('tshark -2 -c 10 -r {0} -R \"(wlan.bssid eq {1}) and wlan.rsn.akms.type eq 2\" '
              '2>/dev/null'.format(read, bssid))
    #look for EAP-TLS
    os.system('tshark -2 -c 10 -r {0} -R \"(wlan.bssid eq {1}) and eap.type eq 13\" '
              '2>/dev/null'.format(read, bssid))
    #look for PEAP
    os.system('tshark -2 -c 10 -r {0} -R \"(wlan.bssid eq {1}) and eap.type eq 25\" '
              '2>/dev/null'.format(read, bssid))
    #look for open network
    os.system('tshark -2 -c 10 -r {0} -R \"(wlan.bssid eq {1}) and ((wlan.fc.type_subtype eq 0x08) or '
              '(wlan.fc.type_subtype eq 0x05)) and not (wlan.tag.number eq 48)\" '
            '2>/dev/null'.format(read, bssid))

#set up local information
read = args.read
arg_list = args.list
force_write = args.force_write
write = args.write
bssid = args.bssid
ssid = args.ssid

if write == None:
    write = force_write

if arg_list == False and write == None:
    parser.print_help()
    exit('error: Must provide list or write')

if ssid:
    if args.netxml:
        netxml = args.netxml
    elif os.path.exists(os.path.splitext(read)[0] + '.netxml'):
        netxml= os.path.splitext(read)[0] + '.netxml'
    elif os.path.exists(os.path.splitext(read)[0] + '.kismet.netxml'):
        netxml = os.path.splitext(read)[0] + '.kismet.netxml'
    else:
        parser.print_help()
        exit('error: you must specify a netxml file to use to search for BSSIDs')

#check if some of this stuff exists
try:
    open(read)
except:
    exit('error: problem reading input packet capture: ' + read)
# Attempt to write file
if write or force_write:
    if force_write and os.path.exists(write):
        try:
            os.remove(write)
            os.mknod(write)
        except:
            exit('error: problem writing to output path: ' + write)
    else:
        if os.path.exists(write):
            exit('error: output file already exists, cowardly refusing to trample it')
        try:
            os.mknod(write)
        except:
            exit('error: problem writing to output path: ' + write)

#read and parse input netxml file
bssids = []
if ssid:
    try:
        tree = et.parse(netxml)
    except:
        exit('error: unable to parse netxml file: ' + netxml)
    root = tree.getroot()
    for network in root.findall('wireless-network'):
        try: #cause parsing fails sometimes
            bssid = network.find('BSSID').text
            for xmlssid in network.findall('SSID'):
                if xmlssid.find('essid').text is not None:
                    if xmlssid.find('essid').text == ssid:
                        bssids.append('{0}'.format(bssid))
        except:
            pass
    bssid = ' or wlan.bssid eq '.join(bssids)
    if not bssid:
        exit('error: could not find {0} in netxml file'.format(ssid))

if arg_list:
    print_to_screen(read, bssid)
if write:
    write_to_file(read, write, bssid)
