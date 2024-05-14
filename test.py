import sqlite3


def getCreateTableQuery():
    query = """ CREATE TABLE BINARIES (
            ID INT PRIMARY KEY NOT NULL,
            BINARYNAME CHAR(50) NOT NULL,
            VERSION CHAR(25) NOT NULL,
            BINARY_INSTALLED_AT DATETIME NOT NULL
        ); """
    return query



dbConn = sqlite3.connect('sql.db')
dbCursor = dbConn.cursor()

createTableQuery = getCreateTableQuery() 

dbCursor.execute(createTableQuery)