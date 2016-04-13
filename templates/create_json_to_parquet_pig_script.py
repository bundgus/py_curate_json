import io
from jinja2 import Environment, FileSystemLoader


def create_json_to_parquet_pig_script(graph, prefixname='', parts=[], depth=0, nodename='rootnode'):

    env = Environment(loader=FileSystemLoader(searchpath='templates'))
    template_file = "Flatten_Denormalize_JSON_to_Parquet.pig.template"
    template = env.get_template(template_file)
    filetext = template.render(parts=parts, prefixname=prefixname)

    with open('output\\{}-Flatten_Denormalize_JSON_Parquet.pig'.format(prefixname), 'w') as outfile:
        outfile.write(filetext)