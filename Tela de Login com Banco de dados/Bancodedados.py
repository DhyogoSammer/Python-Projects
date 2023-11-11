import sqlite3 
from sqlite3 import Error 
import os 

pastaApp = os.path.dirname(__file__)
nomeBanco = pastaApp+"\\BD.db"

# Criar conexão 
def ConexaoBanco():
    con = None 
    try : 
        con = sqlite3.connect(nomeBanco)
    except Error as ex :
        print(ex)
    return con 


def dql(query): #SELECT 
    vcon = ConexaoBanco()
    c = vcon.cursor()
    c.execute(query)
    res = c.fetchall()
    vcon.close()
    return res 


def dml(query): #Insert, Update, Delete 
    try : 
        vcon = ConexaoBanco()
        c = vcon.cursor()
        c.execute(query)
        vcon.commit()
        vcon.close()
    except Error as ex : 
        print(ex)
    
