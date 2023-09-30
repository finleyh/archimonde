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
            cmd = f'VBoxHeadless --startvm {data}'
            returned_output = subprocess.check_output(cmd)
            return returned_output
        return f'Error - Invalid Input: {data[:100]}'
    
    def list_vms(self):
        #return list of vms
        return
    
    def create_vm(self,data : dict):
        cmd = [
            f'''VBoxManage --name "{data['name']}" --ostype {data['ostype']} --register''',
            f'''VBoxManage createhd --filename "{data['name']}.vdi" --size {data.get('size',10000)}''',
            f'''VBoxManage storagectl "{data['name']}" --name "IDE Controller" --add ide --controller PIIX4''',
            f'''VBoxManage storageattach "{data['name']}" --storagectl "IDE Controller" --port 0 --device -0 --type hdd --medium "{data['name']}.vdi"''',
            f'''VBoxManage storageattach "{data['name']}" --storagectl "IDE Controller" --port 0 --device 1 --type dvddrive --medium {self.img_folder+'/standard_'+{data['ostype']}+'.iso'}''',
            f'''VBoxManage modifyvm "{data['name']}" --vrde on'''
        ]
        return f'TODO - Not yet implemented'
    
    def list_os_types(self):
        cmd = f'VBoxManage list ostypes'
        returned_output = subprocess.check_output(cmd)
        return returned_output
    
    def stop_vm(self, data : str):
        #accept get request to shutdown vm
        return
    
    def get_status(self, data : str):
        #get vm status
        return
