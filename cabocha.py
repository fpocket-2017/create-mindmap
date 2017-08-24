# -*- coding: utf-8 -*-

import re
import xml.etree.ElementTree as et

def readCabocha(root, larray, tarray, earray):

    for chunk in root:

        if int(chunk.attrib['link']) != -1:
            larray[int(chunk.attrib['link'])].append(int(chunk.attrib['id']))
        else:
            lastID = int(chunk.attrib['id'])

        tmp = ''
        for tok in chunk:
            if re.search(u"句点|読点", tok.attrib['feature']) == None:
                tmp += tok.text
            elif re.search(u"句点", tok.attrib['feature']) != None:
                earray.append(int(chunk.attrib['id']))

        tarray.append(tmp)
        
    return(lastID)