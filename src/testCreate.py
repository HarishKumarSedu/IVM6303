import json
import yaml
import re 
import pandas as pd 
from pathlib import Path 
import os 

class TestCreate:
    
    def __init__(self, sheets = ['Digital','Reference','Boost']) -> None:
        self.sheets = sheets
        self.sheets = [re.sub('[!-\/:-@[-`{-~\s]','_', sh) for sh in sheets]
        print(self.sheets)
    def dump_test_names(self,testscripts_generate_config_file_path:Path):
        dirname, filename = os.path.split(testscripts_generate_config_file_path)
        if not os.path.exists(dirname) :
            os.makedirs(dirname)
            
        DFT_tests = {}
        for sh in self.sheets:
            sheet = 'raw_data/IVM6303_ATE_Test_Plan_Rev1.xlsx'
            data = pd.read_excel(sheet)
            cols = []

            for col in data.columns.to_list()[1:]:
                #replace the space with 
                
                col = re.sub(' ','_', data[col][2].strip()) 
                #replace the special charecters with underscore '_'
                col = re.sub('[!-\/:-@[-`{-~]','_', col)
                cols.append(col)
            DFT_tests.update(
                {
                   sh: cols
                }
            )

        with open(testscripts_generate_config_file_path, 'w') as file :
            yaml.dump({"TestBench":DFT_tests}, file)
    
    def create_test_scripts(self,testscripts_generate_config_file_path:Path):
        dirname, filename = os.path.split(testscripts_generate_config_file_path)
        if not os.path.exists(testscripts_generate_config_file_path) :
            os.makedirs(dirname)
        with open(testscripts_generate_config_file_path) as stream:
            try:
                tests = yaml.safe_load(stream).get('TestBench')
                # create the directory for each page 
                for page in list(tests.keys()):
                    #if there is not directory for the page create one else pass 
                    page_dir = os.path.join(os.getcwd(),f'TestBench/{page}')
                    if not(os.path.exists(page_dir)):
                        os.mkdir(page_dir)
                    #if the directory exists create the test scripts 
                    else:
                        for test_name in tests.get(page):

                            test_scripts_name = os.path.join(page_dir, f'{test_name}.py')
                            if not(os.path.exists(test_scripts_name)):
                                with open(test_scripts_name, 'w') as file:
                                    test_string = f'''
class {test_name}:
    def __init__(self) -> None:
        pass
    def {test_name}_testSetup(self):
        pass 
    def {test_name}_measurements(self,config: dict):
        pass
    def {test_name}_evaluation(self,limits:dict):
        return None           
                                    '''
                                    file.write(test_string)
                            else:
                                pass 
            except yaml.YAMLError as exc:
                print(exc)
                
if __name__ == '__main__':
    testCreate = TestCreate(sheets = ['PGM production self consistent'])
    testCreate.dump_test_names('TestBench/testscript_generate_config.yaml')
    testCreate.create_test_scripts('TestBench/testscript_generate_config.yaml')