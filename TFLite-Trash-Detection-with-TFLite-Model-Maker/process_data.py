import os
import xml.etree.ElementTree as ET

# Define the mapping
category_mapping = {
    'Drink can': 'Metal',
    'Pop tab': 'Metal',
    'Metal bottle cap': 'Metal',
    'Scrap metal': 'Metal',
    'Aluminium foil': 'Metal',
    'Aluminium blister pack': 'Metal',
    'Metal lid': 'Metal',
    'Food Can': 'Metal',
    'Glass bottle': 'Glass',
    'Broken glass': 'Glass',
    'Glass cup': 'Glass',
    'Glass jar': 'Glass',
    'Food waste': 'Biological',
    'Normal paper': 'Paper',
    'Paper cup': 'Paper',
    'Tissues': 'Paper',
    'Magazine paper': 'Paper',
    'Wrapping paper': 'Paper',
    'Paper straw': 'Paper',
    'Paper bag': 'Paper',
    'Toilet tube': 'Paper',
    'Battery': 'Battery',
    'Unlabeled litter': 'Trash',
    'Cigarette': 'Trash',
    'Garbage bag': 'Trash',
    'Aerosol': 'Trash',
    'Rope - strings': 'Trash',
    'Foam food container': 'Trash',
    'Crisp packet': 'Trash',
    'Disposable food container': 'Trash',
    'Six pack rings': 'Trash',
    'Corrugated carton': 'Cardboard',
    'Other carton': 'Cardboard',
    'Pizza box': 'Cardboard',
    'Egg carton': 'Cardboard',
    'Meal carton': 'Cardboard',
    'Drink carton': 'Cardboard',
    'Carded blister pack': 'Cardboard',
    'Shoe': 'Shoes',
    'Plastic gloves': 'Clothes',
    'Clear plastic bottle': 'Plastic',
    'Plastic film': 'Plastic',
    'Other plastic wrapper': 'Plastic',
    'Plastic bottle cap': 'Plastic',
    'Other plastic': 'Plastic',
    'Styrofoam piece': 'Plastic',
    'Foam cup': 'Plastic',
    'Other plastic bottle': 'Plastic',
    'Disposable plastic cup': 'Plastic',
    'Squeezable tube': 'Plastic',
    'Plastic utensils': 'Plastic',
    'Plastic straw': 'Plastic',
    'Single-use carrier bag': 'Plastic',
    'Plastic lid': 'Plastic',
    'Other plastic container': 'Plastic',
    'Other plastic cup': 'Plastic',
    'Polypropylene bag': 'Plastic',
    'Tupperware': 'Plastic',
    'Spread tub': 'Plastic'
}

# Function to update XML file
def update_xml_file(xml_file_path):
    # Read the file and remove encoding declaration
    with open(xml_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    if lines[0].startswith('<?xml'):
        lines = lines[1:]
    
    xml_str = ''.join(lines)
    root = ET.fromstring(xml_str)

    # Update object names
    for obj in root.findall('object'):
        name = obj.find('name').text
        if name in category_mapping:
            obj.find('name').text = category_mapping[name]

    # Write the updated XML back to the file
    tree = ET.ElementTree(root)
    tree.write(xml_file_path, encoding='utf-8', xml_declaration=False)

# Function to process all XML files in a directory
def process_directory(directory_path):
    for root_dir, _, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.xml'):
                file_path = os.path.join(root_dir, file)
                update_xml_file(file_path)

# Update XML files in both directories
process_directory('data/test')
process_directory('data/train')

print('XML files updated successfully.')