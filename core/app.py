import json
from flask import Flask, jsonify, request
from core.api import API
from core.logger import CustomLogger
import os

alice = API(os.getenv('ARCHIMONDE_VM_DIR'),os.getenv('ARCHIMOND_IMG_DIR'))


@app.route('/',methods=['GET'])
def index():
    return jsonify({'message':'YOU FOUND A PLACEHOLDER!'})

@app.route('/create',methods=['POST'])
def create_vm():
    #parse the form
    return jsonify(isError=False,message="Success",statusCode=200,data=data)

@app.route('/vms/<string:uuid>',methods=['GET','POST'])
def get_status(uuid):
    response = alice.get_status(uuid)
    return jsonify({'message':response})

@app.route('/vms',methods=['GET'])
def list_vms():
    return jsonify({'message':'YOU FOUND A PLACEHOLDER!'})