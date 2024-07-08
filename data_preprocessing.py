import xml.etree.ElementTree as ET
from operator import concat
from itertools import starmap

def parse_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    return root


def extract_data(root):
    data = []
    labels = []

    for pair in root.findall("pair"):
        h = pair.find("h").text
        t = pair.find("t").text

        data.append((h,t))

        entailment = pair.get("entailment")
        labels.append(entailment)

    return data, labels


def preprocess_data(data):
    return list(starmap(concat, data))

