import json
import csv
from flatten_denorm_json import flatten_denorm_json

if __name__ == "__main__":

    # load attributes dictionary
    #attribute_filename = r'output/json_sample_flattened_keys.json'
    attribute_filename = r'output/EUOZJB_flattened_keys.json'
    with open(attribute_filename, 'r') as attributesfile:
        rawjson = attributesfile.read()
        attributes = json.loads(rawjson)

    with open(r'output/EUOZJB.csv', 'w') as awf:
        # x01 is ctl-a = the default delimiter for Impala
        #w = csv.DictWriter(awf, sorted(attributes.keys()), lineterminator='\n', delimiter='\x01')
        w = csv.DictWriter(awf, sorted(attributes.keys()), lineterminator='\n', extrasaction='ignore')
        w.writeheader()

        # filename = r'sample_json/json_sample.json'
        filename = r'sample_json/EUOZJB.json'
        with open(filename, 'r') as f:
            for line in f:
                denormrows = flatten_denorm_json(line, attributes)
                if denormrows is not None:
                    # deduplicate rows
                    dedup_denormrows = [i for n, i in enumerate(denormrows) if i not in denormrows[n + 1:]]

                    w.writerows(dedup_denormrows)
