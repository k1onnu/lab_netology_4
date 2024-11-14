import json
import xml.etree.ElementTree as ET
from xml.dom import minidom

def json_to_xml(json_data):
    # Создаем корневой элемент
    root = ET.Element("People")

    # Заполняем XML-элементами на основе данных JSON
    for person in json_data:
        person_element = ET.SubElement(root, "Person")
        for key, value in person.items():
            pers = ET.SubElement(person_element, key)
            pers.text = str(value)

    # Возвращаем строку XML, отформатированную в многострочном виде
    xml_str = ET.tostring(root, encoding='utf-8')
    parsed_xml = minidom.parseString(xml_str)
    return parsed_xml.toprettyxml(indent="    ")


# Чтение данных из JSON-файла
with open('data.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

#Конвертируем JSON to XML
xml_data = json_to_xml(data)

# Запись отформатированного XML в файл
with open('data.xml', 'w', encoding='utf-8') as xml_file:
    xml_file.write(xml_data)

print("Conversion JSON to XML...completed!")