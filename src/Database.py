from medoo import Medoo

def DbConection():
    return Medoo(dbtype='mysql', host='localhost', database='publiviajes', user='root', password='')