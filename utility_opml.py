# -*- coding: utf-8 -*-

import xml.etree.ElementTree as et

def makeBranch(Pbranch, larray, tarray, earray, ID):
    eleNum = len(larray[ID])

    if eleNum != 0:
        for i in range(eleNum):
            Cbranch = et.SubElement(Pbranch, 'outline')
            Cbranch.set('text', '')

            makeBranch(Cbranch, larray, tarray, earray, int(larray[ID][i]))

            if int(larray[ID][i]) in earray:
                Pbranch = et.SubElement(Pbranch, 'outline')
                Pbranch.set('text', '')
                
        Cbranch = et.SubElement(Pbranch, 'outline')
        Cbranch.set('text', tarray[ID])
        
    else:
        Pbranch.set('text', tarray[ID])