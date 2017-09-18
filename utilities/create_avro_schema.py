import json
from jinja2 import Environment, FileSystemLoader


if __name__ == "__main__":

    # load attributes dictionary
    attribute_filename = r'output/json_sample_flattened_keys.json'
    with open(attribute_filename, 'r') as attributesfile:
        rawjson = attributesfile.read()
        attributes = json.loads(rawjson)

    elements = list(attributes.keys())

    env = Environment(loader=FileSystemLoader(searchpath='templates'))
    template_file = "avro_schema.avsc.template"
    template = env.get_template(template_file)
    filetext = template.render(elements=elements)

    with open('output\\avro_schema.avsc', 'w') as outfile:
        outfile.write(filetext)