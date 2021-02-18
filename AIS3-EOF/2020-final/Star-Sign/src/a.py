#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import string
import random
import html

a =["HER>pl^VPk|1LTG2d",
	"Np+B(#O%DWY.<*Kf)",
	"By:cM+UZGW()L#zHJ",
	"Spp7^l8*V3pO++RK2",
	"_9M+ztjd|5FP+&4k/",
	"p8R^FlO-*dCkF>2D(",
	"#5+Kq%;2UcXGV.zL|",
	"(G2Jfj#O+_NYz+@L9",
	"d<M+b+ZR2FBcyA64K"]

b = ''

p = "IHOPEYOUAREHAVINGLOTSOFFANINTRYINGTOCATCHMETHATWASNTMEONTHETVSHOWWHICHBRINGOUPAPOINTABOUTMEIAMNOTAFRAIDOFTHEGASCHAMBERBECAASEITWILLSENDMETOPAYALLCEALLTHE"

for i in range(17):
	for j in range(9):
		b += a[j][(i + j * 2)%17]
d = {}
d['{'] = '{'
d['}'] = '}'

for i in range(9*17):
    if p[i] not in d.keys():
        d[p[i]] = b[i]

    if b[i] not in d[p[i]]:
        d[p[i]] += b[i]
d['K'] = d['V']

f = "DOYOUKNOWTHEREISACONSTELLATIONFORSHARKANDSHARKISVERYCUTEBUTINEVERWATCHTHOSEHOLOSTUFFPEKOITSTOOOILTHOSEAREFORFATNERDSANYWAYYOUSHOULDKNOWTHATTHEFLAGFORMATISEOF{PRINTABLEASCII}ANDTHEFLAGISEOF{THEKILLERISSTILLUNKNOWN}IHOPEYOUAREHAVINGFUNWITHTHISMISCCHALLENGEANDBECAREFULNOTTOSLIPBECAUSETHEFLOORISCOVEREDWITHOIL"
f2 = f[9*17:]

f = f.upper()
c = ''
t = {}
tt = {}
bf = 1
while bf:
    c = ''
    t = {}
    tt = {}
    bf = 0
    for i in string.ascii_uppercase:
        t[i] = ''
        tt[i] = 0
    t['{'] = ''
    t['}'] = ''
    tt['{'] = 0
    tt['}'] = 0

    for k in range(2):
        for i in range(9):
            for j in range(17):
                z = random.choice(d[f[i*17+j + k*9*17]])
                c += z
                tt[f[i*17+j + k*9*17]] += 1
                if z not in t[f[i*17+j + k*9*17]]:
                    t[f[i*17+j + k*9*17]] += z

    for i in string.ascii_uppercase:
        if i in d.keys():
            if len(t[i]) < len(d[i]) and len(t[i]) < tt[i]:
                bf = 1

p = [ '0123456789ABCDEFG'*2 for _ in range(9*2) ]

for l in range(2):
    for i in range(17):
        for j in range(9):
            tmp = ''
            for k in range(17):
                if k == (i+j*2)%17:
                    tmp += c[i*9+j + l*9*17]
                else:
                    tmp += p[j + l*9][k]
            p[j + l*9] = tmp
for k in range(2):
    for i in range(9):
        print('\t\t', end='')
        for j in range(17):
            print(html.escape(p[i + k*9][j]), end='')
        print("<br>")

