
import re 
import json
import openpyxl
import yaml
import os
from pathlib import Path
from src import log 
from src.utils.common import read_yaml,create_directories
from src.constants import CONFIG_FILE_PATH
from src.TestBench.PGM_production_self_consistent import VBG_TRM_1_2V_REF
class MainTestBnech:
    
    def __init__(self, config_file_path=CONFIG_FILE_PATH) -> None:
        self.config = read_yaml(config_file_path)
        self.test_data_generate = self.config.test_data_generate
        test_config_file = os.path.join(self.test_data_generate.root_dir,self.test_data_generate.test_cofig_filename)
        tests =read_yaml(Path(test_config_file)).TestBench
        VBG_TRM_1_2V_REF.VBG_TRM_1_2V_REF()
        # PGM_production_self_consistent.FRO_TRM.FRO_TRM()
        # PGM_production_self_consistent.FRO_TRM_dummy.FRO_TRM_dummy()
            