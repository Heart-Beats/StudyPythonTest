#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pyexpat import ParserCreate


def parseXml(xml_str):
    handler = xmlSaxHandler()
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    parser.Parse(xml_str)
    return handler.value


class xmlSaxHandler(object):

    def __init__(self):
        self.__nodeName = None
        self.__nodeAttrs = None
        self.__attrsValue = []

    def start_element(self, name, attrs):
        if name == "property":
            self.__nodeName = name
            self.__nodeAttrs = attrs

    def end_element(self, name):
        if name == "property":
            if self.__nodeAttrs["name"] == "idea.background.editor" or self.__nodeAttrs["name"] == "idea.background.frame":
                self.__attrsValue .append(self.__nodeAttrs["value"])

    @property
    def value(self):
        return self.__attrsValue

    def char_data(self, text):
        return


xml_path = r'C:\Users\HL_913305160\Desktop\SoftwareConfig\软件配置\AndroidStudio\config\options\other.xml'
with open(xml_path, 'r') as file:
    xml_str = file.read()
result = parseXml(xml_str)
print(result)
