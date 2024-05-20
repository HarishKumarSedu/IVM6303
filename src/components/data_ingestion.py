import os
import urllib.request as request
import requests
import zipfile
from src import log
from src.constants import CONFIG_FILE_PATH
from src.utils.common import read_yaml


class DataIngestion:
    def __init__(self, config_filepath= CONFIG_FILE_PATH):
        self.data_ingestion = read_yaml(config_filepath).data_ingestion
        #check the the data ingestion directory
        if not os.path.exists(self.data_ingestion.root_dir) :
            os.makedirs(self.data_ingestion.root_dir)
            log.info('data_ingestion directory created under the aritifacts')


    
    def download_file(self):
        # if not os.path.exists(self.config.local_data_file):
            response =  requests.get(
                url = self.data_ingestion.URL,
            )
            if response.status_code  == 200:
                
                with open(os.path.join(self.data_ingestion.root_dir,self.data_ingestion.local_filename),'wb') as file:
                    file.write(response.content)
                    log.info(f' data file name downloaded with name of {self.data_ingestion.local_filename}')
            else:
                    log.error(f' Failed to download the data ....! {self.data_ingestion.root_dir}')
                
        # else:
        #     log.info(f"File already exists ")



    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
  
if __name__ == '__main__':
    dataIngestion=DataIngestion()
    dataIngestion.download_file()