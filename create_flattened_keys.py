import io
from jinja2 import Environment, FileSystemLoader


def create_flattened_keys(partlist, prefixname=''):

    env = Environment(loader=FileSystemLoader(searchpath='templates'))
    template_file = "flattened_keys.json.template"
    template = env.get_template(template_file)
    filetext = template.render(parts=partlist)

    with open('output\\{}-flattened_keys.json'.format(prefixname), 'w') as outfile:
        outfile.write(filetext)