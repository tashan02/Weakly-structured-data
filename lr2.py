from xml.etree import ElementTree as ET
import csv
import tkinter as tk
from tkinter import filedialog
import json
import xml.dom.minidom as md

def convert_to_xml(data, file_path):
    root = ET.Element("data")
    for key, value in data.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    xml_str = ET.tostring(root, encoding='utf-8')
    xml_str = md.parseString(xml_str).toprettyxml(indent="  ")  
    with open(file_path, 'w') as xmlfile:
        xmlfile.write(xml_str)

def convert_to_csv(data, file_path):
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(data.keys())
        writer.writerow(data.values())

def convert_to_tsv(data, file_path):
    with open(file_path, 'w') as tsvfile:
        for key, value in data.items():
            tsvfile.write(f"{key}\t{value}\n")

def convert_to_json(data, file_path):
    with open(file_path, 'w') as jsonfile:
        json.dump(data, jsonfile, indent=4)


root = tk.Tk()
root.withdraw()

data_file = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv"), ("TSV files", "*.tsv"), ("JSON files", "*.json")])
output_format = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json"), ("XML files", "*.xml"), ("CSV files", "*.csv"), ("TSV files", "*.tsv")])

if data_file and output_format:
    with open(data_file, 'r') as file:
        if data_file.endswith('.json'):
            data = json.load(file)
        elif data_file.endswith('.csv'):
            data = {row[0]: row[1] for row in csv.reader(file)}
        elif data_file.endswith('.tsv'):
            data = dict(line.strip().split('\t') for line in file)

    # Determine the output format selected
    if output_format.endswith('.json'):
        convert_to_json(data, output_format)
        print(f"Данные успешно конвертированы и сохранены в формате JSON в файле: {output_format}")
    elif output_format.endswith('.xml'):
        convert_to_xml(data, output_format)
        print(f"Данные успешно преобразованы и сохранены в формате XML в файле: {output_format}")
    elif output_format.endswith('.csv'):
        convert_to_csv(data, output_format)
        print(f"Данные успешно конвертированы и сохранены в формате CSV в файле: {output_format}")
    elif output_format.endswith('.tsv'):
        convert_to_tsv(data, output_format)
        print(f"Данные успешно конвертированы и сохранены в формате TSV в файле: {output_format}")
    else:
        print("Неверный формат")
else:
    print("Файл не выбран")