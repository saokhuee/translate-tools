import pandas as pd
import yaml
import sys

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
    data[key] = search[0][2]



if __name__ == "__main__":
  sourceFilename = sys.argv[1]
  destinationFilename = sys.argv[2]
  excelFilename = sys.argv[3]

  xlFile = pd.ExcelFile("./data/" + excelFilename)
  df = xlFile.parse(sourceFilename)

  with open("./data/" + sourceFilename, 'r', encoding="utf8") as file:
    data = yaml.safe_load(file)
    parseYAML(data, df, "")
    with open("./data/" + destinationFilename, 'w', encoding="utf8") as outfile:
      yaml.dump(data, outfile, default_flow_style=False, allow_unicode=True)
