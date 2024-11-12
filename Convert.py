import json
import xml.etree.ElementTree as ET

def json_to_xml(json_data):

    root = ET.Element("People")
    for person in json_data:
        person_element = ET.SubElement(root, "Person")
        for key, value in person.items():
            pers = ET.SubElement(person_element, key)
            pers.text = str(value)
    return ET.tostring(root, encoding='utf-8').decode('utf-8')

with open('data.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

xml_data = json_to_xml(data)
with open('data.xml', 'w', encoding='utf-8') as xml_file:
    xml_file.write(xml_data)

print("Conversion JSON to XML...completed!")