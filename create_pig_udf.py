import io
from jinja2 import Environment, FileSystemLoader


def create_pig_udf(graph, prefixname='', parts=[], depth=0, nodename='rootnode'):

    env = Environment(loader=FileSystemLoader(searchpath='templates'))
    template_file = "flatten_json_udf.py.template"
    template = env.get_template(template_file)
    filetext = template.render(parts=parts, prefixname=prefixname)

    with open('output\\{}-flatten_json_udf.py'.format(prefixname), 'w') as outfile:
        outfile.write(filetext)