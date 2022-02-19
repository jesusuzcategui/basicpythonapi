import pymysql

def getConection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="",
        db="publiviajes"
    )