import json
from flask import Flask, jsonify, request, Response
from core.api import API
from core.logger import CustomLogger
import os

alice = API(os.getenv('ARCHIMONDE_VM_DIR'),os.getenv('ARCHIMOND_IMG_DIR'))


@app.route('/',methods=['GET'])
def index():
    return jsonify({'message':'YOU FOUND A PLACEHOLDER!'})

@app.route('/create',methods=['POST'])
def create_vm():
    name = request.form.get('name')
    ostype=  request.form.get('os')
    response = alice.create_vm(name,ostype)
    #what else to parse? what does vbox support?
    return jsonify(isError=False,message=f"Success",statusCode=200,data=response)

@app.route('/vms/<string:uuid>/start',methods=['GET'])
def start_vm(uuid):
    response = alice.start_vm(uuid)
    return jsonify({'message':response})

@app.route('/vms/<string:uuid>/stop',methods=['GET'])
def stop_vm(uuid):
    response = alice.stop_vm(uuid)
    return jsonify({'message':response})


@app.route('/vms/<string:uuid>',methods=['GET'])
def get_status(uuid):
    response=alice.get_status(uuid)
    return jsonify({'message':response})

@app.route('/vms',methods=['GET'])
def list_vms():
    response = alice.list_vms()
    return jsonify({'message':response})