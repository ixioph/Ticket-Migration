''' ticket_migration.py '''
import sys
import json



def main(args):
    ''' main function '''
data = []
with open("yourpathtojsonfile") as jsonFile:
    s = jsonFile.read() #Reads the json file and delimiters
    s = s.replace('\t','') #Replaces all the invalid characters with supported
    s = s.replace('\n','')
    s = s.replace(',}','}')
    s = s.replace(',]',']')
    data = json.loads(s) #Loads the result into a list

print(data)


#if __name__ == "__main__":
  # main(sys.argv)
