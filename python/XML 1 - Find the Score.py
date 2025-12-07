'''
Problem description link: https://www.hackerrank.com/challenges/xml-1-find-the-score/problem
'''
import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    x = 0
    for i in node.iter():
        att = len(i.attrib)
        x += att
    return x
        
if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
