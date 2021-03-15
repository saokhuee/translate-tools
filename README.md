1. Create a virtual environment for python
   https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/

##USAGE

Start from `jsonToExcel.py` file:

Step 1: If you have a yaml file, convert it to json file:

```py
with open("data.yaml"), "r", encoding="utf-8") as yml_in, open("data.json", "w") as json_out:
    yml_data = yaml.safe_load(yml_in)
    json.dump(yml_data, json_out)
```

Then load your data with json file:

```py
with open("data.json", "r", encoding="utf-8") as json_data:
    data = json.load(json_data)
```

Step 2: Flatten JSON key using `getFullKey(data)`
Step 3: Dump newly flatten json data to a temp file using `json.dump()`, then transfer data to excel file:

```py
dataObj = pd.read_json("tempfile.json", orient='index')
excelFile = dataObj.to_excel("excelFile.xlsx", encoding="utf-8")
```

Now that you have excel file, you can use google translate service with spreadsheet.
To convert replace data value and transfer them to json, yaml file, we use `run.py` file:
Step 4:

```py
##From Excel file, parse data and return Dataframe or dict of Dataframes
xl_file = pd.ExcelFile("translatedFile.xlsx")
df = xl_file.parse("Sheet1")

with open("data.yml", 'r', encoding="utf8") as file:
  data = yaml.safe_load(file)
  parseYAML(data, df, "")
  with open('translatedYaml.yml', 'w', encoding="utf8") as outfile:
    yaml.dump(data, outfile, default_flow_style=False, allow_unicode=True)
```
