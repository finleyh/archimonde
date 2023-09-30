import subprocess
import re
import os

class API:
    def __init__(self, vm_folder:str, img_folder:str ):
        self.instances={}
        self.vm_folder = vm_folder
        self.img_folder = img_folder
        self.img_folder_exists = self.__exists(img_folder)
        self.vm_folder_exists = self.__exists(vm_folder)

    def __is_valid_uuid(self,data):
        results = re.search(r'^[A-Za-z0-9]{8}\-[A-Za-z0-9]{4}\-[A-Za-z0-9]{4}\-[A-Za-z0-9]{4}\-[A-Za-z0-9]{12}$',data)
        if results:
            return True
        return False
    
    def __exists(self,path):
        file_type = ''
        if os.path.isdir(path):
            file_type='dir'
        if os.path.isfile(path):
            file_type='fil'
        return (os.path.exists(path),file_type)
        
    def __is_readable(self,path):
        return os.path.isdir("")

    def start_vm(self, data : str):
        if self.__is_valid_uuid(data):
            cmd = f'VBoxManage startvm {data}'
            returned_output = subprocess.check_output(cmd)
            return returned_output
        return f'Error - Invalid Input: {data[:100]}'
    
    def list_vms(self):
        #return list of vms
        return

    def create_vm(self, data : str):
        #accept post, create vm by specification
        return
    
    def stop_vm(self, data : str):
        #accept get request to shutdown vm
        return
    
    def get_status(self, data : str):
        #get vm status
        return
