# -*- coding: utf-8 -*-

import re
import xml.etree.ElementTree as et

import utility_xml as uxml
import utility_opml as uopml
import cabocha as ca

MAXRAW = 400

larray = [[] for i in range(MAXRAW)]
tarray = []
earray = []

tin = et.ElementTree(file='input.xml')
lastID = ca.readCabocha(tin.getroot(), larray, tarray, earray)

tout = et.ElementTree(file='init.opml')

root = tout.getroot()
head = root[0]
body = root[1]
CIdea = body[0]

Mbranch = et.SubElement(CIdea, 'outline')
Mbranch.set('text', '')

uopml.makeBranch(Mbranch, larray, tarray, earray, lastID)

uxml.indent(root)

tout.write('imindmap.opml', encoding = 'utf-8', xml_declaration=True)
