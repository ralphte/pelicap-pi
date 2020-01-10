# Pelicap 
![](img/logo.png)

## Overview
Pelicap is a wireless pen testing hardware build. It consist of two parts, the build instructions / part list and a ansable script to configure the os. This build is designed to be mobile and very customizable. Enterprise Wireless pentest can take a wide range of software and utilizing a laptop can be extremely cumbersome. In addition USB Wireless support can very frustrating no matter the platform. Even when it does work, you don’t want to carry it around on a large assessment with wires everywhere. Lastly this build allows you to have a known good wireless testing system to grab and go.

## Why
The out of box solutions suck or they’re $1000's of dollars and still suck. I am not saying this build is perfect but this build allows for the most flexibility.

## Goals
Open platform
Rugged design
Battery’s included
Small footprint
Customizable
Phone or tablet control

## Features
- Three Wireless Cards (Monitor Mode)
- LTE (out of band) internet
- POE
- GPS
- Crazy radio
- Battery powered (Easy Removal)
- Bluetooth Control
- Full Kali / Linux OS

## Parts List
The following is the parts I used to build version 1. Use this as a guide as you may want to remove or replace these parts with better gear or parts that are available. All the parts should be pretty easy to find.


| Part               | Cost  | Amount | Total |
|--------------------|-------|--------|-------|
|[Pelican 1120 Case With Foam (Desert Tan)](https://www.amazon.com/gp/product/B0014D47RY/ref=ppx_yo_dt_b_asin_title_o05_s00?ie=UTF8&psc=1)|$38.36|1|$38.36 |
|[Raspberry Pi 4 Model B 2019 Quad Core 64 Bit WiFi Bluetooth (4GB)](https://www.amazon.com/gp/product/B07TC2BK1X/ref=ppx_yo_dt_b_asin_title_o04_s00?ie=UTF8&psc=1)|$62.00|1|$62.00|
|[Lexar Professional 1800x 64GB microSDXC UHS-II Card](https://www.amazon.com/gp/product/B07QM348D9/ref=ppx_yo_dt_b_asin_title_o05_s00?ie=UTF8&psc=1)|$39.99|1|$39.99|
|[Raspberry Pi 3G/4G-LTE Base HAT](https://sixfab.com/product/raspberry-pi-base-hat-3g-4g-lte-minipcie-cards/)|$39.99|1|39.99|
|[Quectel EC25 Mini PCle 4G/LTE Module - Sixfab](https://sixfab.com/product/quectel-ec25-mini-pcle-4glte-module/)|$49.99|1|$49.99|
|[LTE Main & Diversity & GNSS Triple Port u.FL Antenna - 100mm - Sixfab](https://sixfab.com/product/lte-main-diversity-gnss-triple-port-u-fl-antenna-100mm/)|$12.75|1|$12.75|
|[Panda Wireless PAU09 N600 Dual Band (2.4GHz and 5GHz) Wireless N USB Adapter W/Dual 5dBi Antennas - Windows XP/Vista/7/8/8.1/10, Mint, Ubuntu, openSUS](https://www.amazon.com/gp/product/B01LY35HGO/ref=ppx_yo_dt_b_asin_title_o09_s00?ie=UTF8&psc=1)|$34.99|2|$69.98|
|[SeeedStudio - Crazyradio PA - Long Range 2.4Ghz USB Radio Dongle With Antenna - DIY Maker Open Source BOOOLE: Computers & Accessories](https://www.amazon.com/SeeedStudio-Crazyradio-2-4Ghz-Dongle-Antenna/dp/B00VYA3A2U)|$34.00|1|$34.00|
|[Official Raspberry Pi Power Over Ethernet (PoE) HAT for Raspberry Pi 3 B+ and 802.3af PoE Network](https://www.amazon.com/gp/product/B07GR9XQJH/ref=ppx_yo_dt_b_asin_title_o05_s00?ie=UTF8&psc=1)| #30.00|1|$30.00|
| [Adafruit Accessories GPIO Stacking Header for Pi A+/B+/Pi 2 - Extra-long 2x20 Pins (1 piece): Electronics](https://www.amazon.com/gp/product/B00TW0W9HQ/ref=ppx_yo_dt_b_asin_title_o08_s00?ie=UTF8&psc=1)|$7.37|1|$7.37|
| [Bingfu RP-SMA Male to RP-SMA Female Bulkhead Mount RG316 WiFi Antenna Extension Coaxial Cable 30cm / 1 feet (2-Pack) for Wireless PCI Express PCIE Network Card WiFi Adapter WiFi Router Security Camera](https://www.amazon.com/gp/product/B07MT3VZXZ/ref=ppx_yo_dt_b_asin_title_o02_s00?ie=UTF8&psc=1)|$6.99|3|$20.97|
|[Boobrie 90 Degree RF Coaxial Coax Adapter RP SMA Male (Hole) to RP SMA Female (pin) Right Angle Connector for Audio FPV Antennas Radio Video Mobile Pack of 2: Computers & Accessories](https://www.amazon.com/gp/product/B07DC2374L/ref=ppx_yo_dt_b_asin_title_o04_s00?ie=UTF8&psc=1)|$5.50|2|$11.00|
|[SMAKN® M25 Waterproof USB3.0 Coupler](https://www.amazon.com/gp/product/B01JYLH2PG/ref=ppx_yo_dt_b_asin_title_o02_s03?ie=UTF8&psc=1)|$12.66|1|$12.66|
|[CNLINKO RJ45 Dual Port Ethernet Connector, Panel Mount Receptacles Socket Jack, Outdoor Waterproof IP67, Fast Data, Industrial: Electronics](https://www.amazon.com/gp/product/B073RZHPKS/ref=ppx_yo_dt_b_asin_title_o03_s02?ie=UTF8&psc=1)|$9.98|1|$9.98|
|[SaiTech IT 2 Pack Short Length 1 Feet USB 3.0 Extension Cable, USB 3.0 A Male to Female Extender Cable](https://www.amazon.com/gp/product/B077MFLH7W/ref=ppx_yo_dt_b_asin_title_o03_s00?ie=UTF8&psc=1)|$8.99|3|$26.97|
|[Superbat U.FL Cable 10cm/3.9” IPX (IPEX/UFL) Female to IPX (IPEX/UFL) Male RF Pigtail Cable 1.37mm Low-Loss U.FL Extension Cable Pack of 2: Home Audio & Theater](https://www.amazon.com/gp/product/B07PBDQ375/ref=ppx_yo_dt_b_asin_title_o09_s00?ie=UTF8&psc=1)| $6.99|2|$13.98|
|[eBoot 180 Pieces Male Female Hex Brass Spacer Standoff Screw Nut Assortment Kit (M2.5)](https://www.amazon.com/gp/product/B06XXV8RTR/ref=ppx_yo_dt_b_asin_title_o03_s01?ie=UTF8&psc=1)| $8.99|1|$8.99| 

- POE Riser 
- Battery 

TOTAL FULL BUILD $461
TOTAL WITHOUT LTE $360


## Build instructions 



## OS configuration
