import sqlite3
from datetime import datetime

class Database:
    dbConnection = None
    dbCursor = None

    #Stores the versions of the binaries into variables
    nodeJs18Ver = None
    nodeJs20Ver = None
    javaCorretto17Ver = None 
    javaOpenJdk11Ver = None
    javaOracleJdk11Ver = None

    def __init__(self):
        self.dbConnection = sqlite3.connect('sql.db')

    def connect(self) -> bool:
        self.dbConnection = None
        self.dbCursor = None
        try:
            self.dbConnection = sqlite3.connect('sql.db')
            self.dbCursor = self.dbConnection.cursor()
            return True
        except Exception as err:
            print('Exception: {}'.format(err))
            return False                
    
    #Execute Create Table query
    def createTable(self):
        if self.connect():
            try:
                query = """ CREATE TABLE BINARIES (
                            ID INTEGER PRIMARY KEY AUTOINCREMENT,
                            BINARYNAME CHAR(50) NOT NULL,
                            VERSION CHAR(25) NOT NULL,
                            BINARY_INSTALLED_AT DATETIME NOT NULL
                        ); """
                self.dbCursor.execute(query)
                self.dbConnection.commit()
            except Exception as err:
                    print('Exception: {}'.format(err))
            finally:
                self.dbCursor.close()
                self.dbConnection.close()
    
    #Query - Insert New Record
    def insertNewRecord(self, record):
        if self.connect():
            try:
                data = (record.get('name'), record.get('version'), datetime.now())
                query = """ INSERT INTO BINARIES (BINARYNAME, VERSION, BINARY_INSTALLED_AT)
                            VALUES (?, ?, ?)
                        """
                self.dbCursor.execute(query, data)
                self.dbConnection.commit()
            
            except Exception as err:
                print('Exception: {}'.format(err))
            
            finally:
                self.dbCursor.close()
                self.dbConnection.close()

    #Query - Update version
    def updateVersion(self, record):
        if self.connect():
            try:
                data = (record.get('version'), datetime.now(), record.get('name'))
                query = """ UPDATE BINARIES
                            SET VERSION = ?, BINARY_INSTALLED_AT = ?
                            WHERE BINARYNAME = ?;
                        """
                self.dbCursor.execute(query, data)
                self.dbConnection.commit()
                print('Data successfully updated')
            
            except Exception as err:
                print('Exception: {}'.format(err))
            finally:
                self.dbCursor.close()
                self.dbConnection.close()

    def getVersion(self, version) :
        if self.connect():
            try:
                query = "SELECT * FROM BINARIES WHERE BINARYNAME = ?"
                self.dbCursor.execute(query, (version,))
                result = self.dbCursor.fetchone()
                if result is not None:
                    print('Version of ' + version + ' is: ' + result[2])
                else:
                    print('No records found in database for ' + version)
            except Exception as err:
                    print('Exception: {}'.format(err))
            finally:
                self.dbCursor.close()
                self.dbConnection.close()

    def populateVersion(self):
        self.nodeJS18Ver = self.dbCursor.execute(self.getVersion("nodejs18"))
        self.nodeJS20Ver = self.dbCursor.execute(self.getVersion("nodejs20"))


#Test Database object
db = Database()
dataRecord = {
    'name': 'nodeJs18',
    'version': '18.0.0'
}

db.createTable()
print('Database table created')

db.insertNewRecord(record=dataRecord)
print('Data inserted successfully')

db.getVersion(version=dataRecord.get('name'))

dataRecord = {
    'name': 'nodeJs18',
    'version': '18.1.0'
}
db.updateVersion(record=dataRecord)
print('Data updated successfully')

db.getVersion(version=dataRecord.get('name'))