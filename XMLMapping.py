import xml.etree.ElementTree as ET

def printchildpaths(node, currentpath):
    xmlpaths = []
    
    for child in node:
        if len(child):
            printchildpaths(child, currentpath + ',' + child.tag)
        else:
            xmlpath = currentpath + ',' + child.tag
            if xmlpath not in xmlpaths:
                xmlpaths.append(xmlpath)
    
    return xmlpaths
                
                
root = ET.fromstring(xml_content)
for child in root:
    xmlpaths = printchildpaths(child, root.tag)
