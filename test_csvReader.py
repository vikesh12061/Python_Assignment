import unittest
import os.path
import json

from os import path

from csvReader2 import CSVReader

class TestCSVReaderMethods(unittest.TestCase):


    def test_checkIfExist_function(self):
        listdata = [{'label': 'SOFT DRINKS', 'id': '179037', 'link': 'https://groceries.morrisons.com/browse/178974/178973/179037', 'children': []}, 
                    {'label': 'WINE & SPARKLING', 'id': '179038', 'link': 'https://groceries.morrisons.com/browse/178974/178973/179038', 'children': []}]
        newId = '179039'
        response = CSVReader.checkIfExist(self, listdata, newId)
        self.assertEqual(response, False)
        newId = '179037'
        response = CSVReader.checkIfExist(self, listdata, newId)
        self.assertEqual(response['id'], '179037')
    
    def test_createChildNode_function(self):
        finalDict = dict(baseUrl=None, children=[])
        csvReader = CSVReader('data.csv')
        rowData  = {'Base URL': 'https://groceries.morrisons.com/browse', 
                        'Level 1 - Name': 'THE BEST', 'Level 1 - ID': '178974', 'Level 1 - URL': 'https://groceries.morrisons.com/browse/178974', 
                        'Level 2 - Name': 'FRESH', 'Level 2 - ID': '178969', 'Level 2 URL': 'https://groceries.morrisons.com/browse/178974/178969', 
                        'Level 3 - Name': 'CHEESE', 'Level 3 - ID': '178975', 'Level 3 URL': 'https://groceries.morrisons.com/browse/178974/178969/178975'}
        response  = csvReader.createChildNode(finalDict, rowData, 0)
        self.assertGreater(len(finalDict['children']), 0)
        self.assertGreater(len(finalDict['children'][0]['children']), 0)

    def test_check_op_file_creation(self):
        j = CSVReader('data.csv')
        path_check = path.exists("output.json")
        self.assertTrue(path_check)

if __name__ == '__main__':
    unittest.main()