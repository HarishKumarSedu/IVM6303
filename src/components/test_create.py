import json
import yaml
import re 
import pandas as pd 
from pathlib import Path 
import os 
from src import log 
from src.utils.common import read_yaml
from src.constants import CONFIG_FILE_PATH


class TestCreate:
    
    def __init__(self, config_filepath= CONFIG_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.test_data_generate = self.config.test_data_generate
        self.test_bench = self.config.test_bench
    
    def create_test_scripts(self):
        if not os.path.exists(self.test_bench.root_dir):
            os.makedirs(self.test_bench.root_dir)
            log.info('TestBench created ...\n')
        test_config_file = os.path.join(self.test_data_generate.root_dir,self.test_data_generate.test_cofig_filename)
        if os.path.exists(test_config_file):
                tests =read_yaml(Path(test_config_file)).TestBench
                # create the directory for each page 
                for page in list(tests.keys()):
                    #if there is not directory for the page create one else pass 
                    page_dir = os.path.join(self.test_bench.root_dir, page)
                    if not(os.path.exists(page_dir)):
                        os.mkdir(page_dir)
                        log.info(f'Page {page} directory created')
                    #if the directory exists create the test scripts 
                    for test_name in tests.get(page):
                        test_scripts_name = os.path.join(page_dir, f'{test_name.lower()}.py')
                        if not(os.path.exists(test_scripts_name)):
                            with open(test_scripts_name, 'w') as file:
                                log.info(f'{test_name}.py script created...!')
                                test_string = f'''
class {test_name}:
    def __init__(self) -> None:
        print({test_name})
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
                            log.warn(f'{test_name}.py script already exists...!')
if __name__ == '__main__':
    testCreate = TestCreate(sheets = ['PGM production self consistent'])
    testCreate.dump_test_names('TestBench/testscript_generate_config.yaml')
    testCreate.create_test_scripts('TestBench/testscript_generate_config.yaml')