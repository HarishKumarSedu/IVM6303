from src import log

from src.components.data_ingestion import DataIngestion
from src.components.test_data_generate import TestDataGenerate

dataIngetion = DataIngestion()
dataIngetion.download_file()

testDataGenerate = TestDataGenerate()
testDataGenerate.generate_test_data()