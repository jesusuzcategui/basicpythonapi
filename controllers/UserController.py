from flask import jsonify
from src.Database import DbConection
import logging

def findAll():
    result = []
    db = DbConection()
    res = db.select('users', '*')
    datita = res.all()
    for i in datita:
        result.append({
            "id": i['id'],
            "email": i['email'],
            "pass": i['pasword'],
            "estado": i['estado']
        })
    
    return jsonify(result)