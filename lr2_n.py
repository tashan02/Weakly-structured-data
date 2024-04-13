import xml.etree.ElementTree as ET
import csv
import os
import re
import json

def preprocess_data(data):
    if isinstance(data, ET.Element):
        cleaned_data = ET.tostring(data, encoding='unicode', method='text')
    elif isinstance(data, str):
        cleaned_data = data
        cleaned_data = re.sub(r'[^\w\s]', '', cleaned_data)  # удаление специальных символов
        cleaned_data = re.sub(r'[\n\t\r]', '', cleaned_data)
    else:
        cleaned_data = str(data)
    return cleaned_data



def load_file(file_path):
    _, file_extension = os.path.splitext(file_path)
    if file_extension == '.html':
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    if file_extension == '.xml':
        tree = ET.parse(file_path)
        root = tree.getroot()
        return root
    elif file_extension == '.csv' or file_extension == '.tsv':
        data = []
        with open(file_path, 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file, delimiter='\t' if file_extension == '.tsv' else ',')
            for row in csv_reader:
                data.append(row)
        return data
    elif file_extension == '.json':
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    else:
        raise Exception('Unsupported file format: {}'.format(file_extension))


def save_file(output_data, output_format):
    output_path = 'output.' + output_format
    input_data_processed = [preprocess_data(item) for item in output_data]
    if output_format == 'html':
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write('\n'.join(input_data_processed))
    elif output_format == 'xml':
        output_root = ET.Element('root')
        for data_row in input_data_processed:
            child = ET.SubElement(output_root, 'row')
            for item in data_row:
                subchild = ET.SubElement(child, 'item')
                subchild.text = str(item)  # Преобразуем данные в строковый тип
        tree = ET.ElementTree(output_root)
        tree.write(output_path)
    elif output_format == 'csv':
        with open(output_path, 'w', encoding='utf-8', newline='') as file:
            csv_writer = csv.writer(file)
            for row in input_data_processed:
                csv_writer.writerow(row)
    elif output_format == 'tsv':
        with open(output_path, 'w', encoding='utf-8', newline='') as file:
            tsv_writer = csv.writer(file, delimiter='\t')
            for row in input_data_processed:
                tsv_writer.writerow(row)
    elif output_format == 'json':
        with open(output_path, 'w', encoding='utf-8') as file:
            json.dump(input_data_processed, file, ensure_ascii=False, indent=4)
    else:
        raise Exception('Unsupported output format')


if __name__ == '__main__':
    input_file = input("Enter the location of the input file: ")
    output_format = input("Enter the desired output format (html/xml/csv/tsv/json): ")

    input_data = load_file(input_file)

    if output_format == 'html' or output_format == 'csv' or output_format == 'tsv':
        output_data = input_data
    elif output_format == 'xml':
        output_data = input_data
    elif output_format == 'json':
        if isinstance(input_data, dict):
            output_data = input_data
        else:
            output_data = {'data': input_data}
    else:
        print("Unsupported output format")
        exit()

    save_file(output_data, output_format)
    print("Conversion successful. Output saved as 'output." + output_format + "' file")


def save_file(output_data, output_format):
    output_path = 'output.' + output_format
    input_data_processed = [preprocess_data(item) for item in output_data]
    if output_format == 'html':
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write('\n'.join(input_data_processed))
    elif output_format == 'xml':
        output_root = ET.Element('root')
        for data_row in input_data_processed:
            child = ET.SubElement(output_root, 'row')
            for item in data_row:
                subchild = ET.SubElement(child, 'item')
                subchild.text = str(item)  # Преобразуем данные в строковый тип
        tree = ET.ElementTree(output_root)
        tree.write(output_path)
    elif output_format == 'csv':
        with open(output_path, 'w', encoding='utf-8', newline='') as file:
            csv_writer = csv.writer(file)
            for row in input_data_processed:
                csv_writer.writerow(row)
    elif output_format == 'tsv':
        with open(output_path, 'w', encoding='utf-8', newline='') as file:
            tsv_writer = csv.writer(file, delimiter='\t')
            for row in input_data_processed:
                tsv_writer.writerow(row)
    elif output_format == 'json':
        with open(output_path, 'w', encoding='utf-8') as file:
            json.dump(input_data_processed, file, ensure_ascii=False, indent=4)
    else:
        raise Exception('Unsupported output format')


if __name__ == '__main__':
    input_file = input("Enter the location of the input file: ")
    output_format = input("Enter the desired output format (html/xml/csv/tsv/json): ")

    input_data = load_file(input_file)

    if output_format == 'html' or output_format == 'csv' or output_format == 'tsv':
        output_data = input_data
    elif output_format == 'xml':
        output_data = input_data
    elif output_format == 'json':
        if isinstance(input_data, dict):
            output_data = input_data
        else:
            output_data = {'data': input_data}
    else:
        print("Unsupported output format")
        exit()

    save_file(output_data, output_format)
    print("Conversion successful. Output saved as 'output." + output_format + "' file")
