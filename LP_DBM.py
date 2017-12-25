# Written by Miguel Bigueur
# Log parsing and Database Management
# Security Scripting w/Python
# Dec 24, 2017


import os, argparse, sqlite3

DIR_NAME = os.path.dirname('/root/PycharmProjects/untitled/attacks')
db_path = os.path.join(DIR_NAME, "History.db")
print(db_path)

try:
    sqlConn = sqlite3.connect(db_path)
except sqlConn.DatabaseError:
    print("unable to open database")
    exit(0)
print("Database opened successfully")

sqlConn.execute('CREATE TABLE IF NOT EXISTS attacks(id INTEGER PRIMARY KEY, attack_line TEXT)')
print("Table created successfully");

dbLoc = sqlConn.execute("SELECT * FROM attacks")

#   This is a class designed to store the results from the parsed file until we're
#   ready to print them out
class modsecRec:
    #  this is the initializer
    def __init__(self):
        #  this is the list where all of the individual items are stored
        self.storageList = []

    #  append items to the list
    def append(self, newItem):
        self.storageList.append(newItem)

    #  extract information from the message line and append it
    def extractMessage(self, msgLine):
        self.storageList.append(msgLine)

    #  print the parsed data out to a file from the list
    def printListToFile(self, outputFilename):
        with open(outputFileName, 'a') as outHandle:
            #  create a blank string
            completeLine = ''
            for singleEntry in self.storageList:
                #  strip newlines out but append a comma for CSV format
                completeLine = completeLine + singleEntry.rstrip() + ","
            #  now we can write the line out, but strip the trailing comma
            outHandle.write(completeLine.rstrip(","))

    #  print out the entries to screen since we don't have an output file
    def printList(self):
        for singleEntry in self.storageList:
            print(singleEntry.rstrip(), ",")

    #  start over on the list since we've dumped one out
    def clear(self):
        self.storageList = []


#  parse the command line arguments
argParser = argparse.ArgumentParser()
argParser.add_argument('-i', type=str, help='the input file with the ModSecurity audit log', required=True)
argParser.add_argument('-o', type=str, help='the output file this should generate')
# argParser.add_argument('-f', type=str, help='the format of the output')

passedArgs = vars(argParser.parse_args())

inputFileName = passedArgs['i']
outputFileName = passedArgs['o']

if not os.path.exists(inputFileName):
    print("You must specify an input file that exists")
    exit()

if outputFileName and os.path.exists(outputFileName):
    os.remove(outputFileName)

eachRecord = modsecRec()


with open(inputFileName, 'r') as fileHandle:
    for dataLine in fileHandle:
        if '--' in dataLine:
            if '-B--' in dataLine:
                httpReq = fileHandle.readline()
                eachRecord.append(httpReq)

                if "<script>alert(1)</script>" in httpReq:
                    print("Attack found on line!")
                    print("Writing Values to Database")
                    print(httpReq)
                    Attack = httpReq
                    # PUT your insert sql statement lines here to insert url_line
                    for row in dbLoc:
                        print(row[0], row[1])
                    sqlConn.execute("INSERT INTO attacks VALUES (?, ?);",(None, str(Attack)))
                sqlConn.commit()

                if "../etc" in httpReq:
                    print("Attack found on line!")
                    print("Writing Values to Database")
                    print(httpReq)
                    Attack = httpReq
                    # PUT your insert sql statement lines here to insert url_line
                    for row in dbLoc:
                        print(row[0], row[1])
                    sqlConn.execute("INSERT INTO attacks VALUES (?, ?);",(None, str(Attack)))
                sqlConn.commit()
                if outputFileName:
                    eachRecord.printListToFile(outputFileName)
                else:
                    eachRecord.printList()
                eachRecord.clear()


sqlConn.close()
fileHandle.close()
