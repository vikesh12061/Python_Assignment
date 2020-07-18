import csv
import logging
import json 
logging.basicConfig(
    filename='csvReaderLog.log',
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')


class CSVReader():
    def __init__(self, path):
        self.finalDict = dict(baseUrl=None, children=[])
        self.main(path)

    # Function to check level dictionary is alreay exist then return that dictionary
    def checkIfExist(self, listData, id):
        for item in listData:
            if item['id'] == id:
                return item
        return False 
    
    # This Recursive function creates children dictionaries present in single row data
    def createChildNode(self, parentObj, data, index):
        j = index + 1
        nextLevelAvailable = data.get('Level '+ str(j) +' - ID')
        if nextLevelAvailable:
            nodeExist = self.checkIfExist(parentObj['children'], data['Level '+ str(j) +' - ID'])
            if nodeExist:
                self.createChildNode(nodeExist, data, j)
            else:
                childrenDict =  dict(label=None, id=None, link=None, children=[])
                childrenDict['label'] = data['Level '+ str(j) +' - Name']
                childrenDict['id'] = data['Level '+ str(j) +' - ID']
                link = data.get('Level '+ str(j) +' - URL')
                childrenDict['link'] = link if link else data['Level '+ str(j) +' URL'] # handel '-' in URL field

                parentObj['children'].append(childrenDict)
                self.createChildNode(childrenDict, data, j)

    # This function read specified csv file and writes the final dictionary
    def main(self, path):
        try:
            with open(path, mode='r') as csv_file:
                logging.info('File data2.csv read successfully')
                csv_reader = csv.DictReader(csv_file)
                fileldNames = csv_reader.fieldnames
                for row in csv_reader:
                    i = 0
                    if not self.finalDict['baseUrl'] and row[fileldNames[i]]: # Set baseUrl from first non empty row in excel
                        self.finalDict['baseUrl'] = row[fileldNames[i]]
                    self.createChildNode(self.finalDict, row, i) # Call Recursive function to create children dictionaries

                # Serializing json  
                json_object = json.dumps(self.finalDict, indent = 4)
                with open("output.json", "w") as outfile: 
                    outfile.write(json_object)
                logging.info('File output.json write successfully') 
 
        except FileNotFoundError:
            logging.error('File ' +path+ ' not found.')
        except KeyError:
            logging.error('File ' +path+ ' not in expected format')
        except IOError:
            logging.error('File ' +path+ ' opened successfully, but couldn\'t write')


if __name__ == '__main__':
    r = CSVReader('F:\Software\data4.csv') 


