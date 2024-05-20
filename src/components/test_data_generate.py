import re 
import json
import openpyxl
import yaml
import pandas as pd 
import os

os.makedirs('artifacts/test_data')
sheetnames =  openpyxl.load_workbook('artifacts/IVM6303_ATE_Test_Plan_Rev1.xlsx').sheetnames
config = {}
print(sheetnames)
for sheet in sheetnames:
    data = pd.read_excel('artifacts/IVM6303_ATE_Test_Plan_Rev1.xlsx',sheet_name=sheet)
    dataset = {}
    sheet = re.sub('[!-\/:-@[-`{-~\s]','_', sheet) 
    tests = []
    print(data.columns[1:])
    for column in data.columns[1:]:
        tests.append(re.sub('[!-\/:-@[-`{-~\s]','_',data[column][2]))
        dataset.update(
            {
                tests[-1]: {
                    "TestNumber" :data[column][1],
                    "TestStatus" :data[column][0],
                    "TestData" :data[column][3],
                    "Limits" : {
                        "Min" : data[column][4],
                        "Min Value/%" : data[column][5],
                        "Min Value/%" : data[column][5],
                        "Value" : data[column][6],
                        "Max" : data[column][7],
                        "Max Value/%" : data[column][8],
                        },
                }
            }
        )
    config.update({
        sheet:tests
    })
    
    with open(f'artifacts/test_data/{sheet}_data.json','w') as file:
        json.dump(dataset, file)

os.makedirs('config')
with open( f'config/config.yaml','w') as file:
    yaml.dump({"TestBench":config}, file)