import yaml
import json
import pandas as pd

with open("vi-VN.yml", "r", encoding="utf-8") as yml_in, open("vi-VN.json", "w") as json_out:
    yml_data = yaml.safe_load(yml_in)
    json.dump(yml_data, json_out)

with open("vi-VN.json", "r", encoding="utf-8") as json_data:
    data = json.load(json_data)

def getFullKey(obj):
    merge_keys = {}

    def flatten(item, parent_key='', sep="/"):
        if type(item) is dict:
            for key in item:
                flatten(item[key], parent_key + str(key) + sep)

        elif type(item) is list:
            index = 0

            for ele in item:
                flatten(ele, parent_key + str(index) + sep)
                index = index + 1
        else:
            merge_keys[parent_key[:-1]] = item

    flatten(obj)
    return merge_keys

with open("temp-vi.json", "w", encoding="utf-8") as test_file:
    json.dump(getFullKey(data), test_file, ensure_ascii=False)

dataObj = pd.read_json("temp-vi.json", orient='index')
excelFile = dataObj.to_excel("vi-VN.xlsx", encoding="utf-8") 
