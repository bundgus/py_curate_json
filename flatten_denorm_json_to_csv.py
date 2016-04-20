import json
import csv
from flatten_denorm_json import flatten_denorm_json

if __name__ == "__main__":

    # load attributes dictionary
    attribute_filename = r'output/master-businessRecord_flattened_keys.json'
    with open(attribute_filename, 'r') as attributesfile:
        rawjson = attributesfile.read()
        attributes = json.loads(rawjson)

    with open(r'output/businessRecord.csv', 'w') as awf:
        # x01 is ctl-a = the default delimiter for Impala
        #w = csv.DictWriter(awf, sorted(attributes.keys()), lineterminator='\n', delimiter='\x01')
        w = csv.DictWriter(awf, sorted(attributes.keys()), lineterminator='\n', extrasaction='ignore')
        w.writeheader()

        #filename = r'sample_json/v12-businessRecord.json'
        filename = r'sample_json/analyticsWeb_SSW2010.2016-04-17-14_WCI_sswhlp1201_inst8-businessRecord.log'
        with open(filename, 'r') as f:
            for line in f:
                jstring = f.readline()
                denormrows = flatten_denorm_json(jstring, attributes)
                if denormrows is not None:
                    w.writerows(denormrows)
