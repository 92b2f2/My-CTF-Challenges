#!/usr/bin/env python
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
b = ''

#cipher
p=[ "S#R<T5#NM/UMFD+%*",
	"+LM+>M5y|E&F%JlXM",
	"W/lFCB-Y*&fW4FVc#",
	"K9ld(V^1#F95/l+j^",
	"bMTc3S%T@|bVAc(G^",
	"pt5kbZC5+25y6Z&1P",
	"C.+MM6FAV>BK.-7&+",
	"+zp4(Jk(V&@VF%RzK",
	"p(l1/5+#%+Z*-WtH)",
	"U(P6(H5jzk&LZRqMB",
	"ZANK}O+JYb5:pNc-J",
	"6NkWR_lLb-RCy+pzF",
	"D/HGJHF7>H5:)MD;+",
	"+*Stj+p({|S&yP.@L",
	"OFk6f._N^+8KG|t7}",
	"7H1/J6cM4F5^TJ+^d",
	"Fb/+4Y2cp:pdb<kpN",
	"<F{Z>V+)<9K(OVEt9",]


for k in range(2):
    for i in range(17):
        for j in range(9):
            b += p[j + k*9][(i + j * 2)%17]

for k in range(2):
    for i in range(9*17):
        for j in string.ascii_uppercase:
            if j in d.keys():
                if b[i + k*9*17] in d[j]:
                    print(j, end='')
                    break
                if b[i + k*9*17] in '{}':
                    print(b[i + k*9*17], end='')
                    break

