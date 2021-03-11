import pandas as pd
import yaml

def parseYAML(data, dataFrame, path):
  if type(data) is dict:
    for key in data:
      newPath = str(key) if path is "" else path + "/" + str(key)
      if type(data[key]) is str:
        replaceData(data, key, dataFrame, newPath)
      else:
        parseYAML(data[key], dataFrame, newPath)
  elif type(data) is list:
    for key in range(len(data)):
      newPath = str(key) if path is "" else path + "/" + str(key)
      if type(data[key]) is str:
        replaceData(data, key, dataFrame, newPath)
      else:
        parseYAML(data[key], dataFrame, newPath)

def replaceData(data, key, dataFrame, path):
  print(path)
  search = dataFrame.loc[dataFrame['key'] == path].values
  if len(search) > 0:
    data[key] = search[0][1]

xl_file = pd.ExcelFile("./Book1.xlsx")
df = xl_file.parse("Sheet1")

with open("en-GB.yml", 'r', encoding="utf8") as file:
  data = yaml.safe_load(file)
  parseYAML(data, df, "")
  with open('vi-VN.yml', 'w', encoding="utf8") as outfile:
    yaml.dump(data, outfile, default_flow_style=False, allow_unicode=True)
