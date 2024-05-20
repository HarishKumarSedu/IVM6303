import os
import urllib.request as request
import requests
import zipfile
from src import log



class DataIngestion:
    def __init__(self):
        # self.config = config
        pass


    
    def download_file(self):
        # if not os.path.exists(self.config.local_data_file):
            response =  requests.get(
                url = 'https://github.com/HarishKumarSedu/IVM6303/blob/master/src/raw_data/IVM6303_ATE_Test_Plan_Rev1.xlsx?raw=true',
            )
            if response.status_code  == 200:
                log.info('fetch pass')
                with open('artifacts/IVM6303_ATE_Test_Plan_Rev1.xlsx','wb') as file:
                    file.write(response.content)
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