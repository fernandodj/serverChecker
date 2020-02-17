import subprocess
import json
import csv
import pprint
import platform

def main():
        data = dict()
        data.update(process_data = getProcessData())
        os_info = getOSData()
        data.update(os_name = os_info['name'])
        data.update(os_version = os_info['version'])
        
        getUsersData()
        #getUsersData()
        #getCPUData()


def getCPUData():
        """ cmd = "lscpu | grep -iE 'Nombre del modelo|ID de fabricante|Arquitectura'" """
        output = subprocess.Popen(['lscpu'], stdout=subprocess.PIPE).stdout.readlines()
        headers = [h for h in ' '.join(output[0].strip().split()).split() if h]
        raw_data = map(lambda s: s.strip().split(None, len(headers) - 1), output[1:])
        pprint.pprint([dict(zip(headers, r)) for r in raw_data])
        return [dict(zip(headers, r)) for r in raw_data]
        """ process = subprocess.Popen(cmd, stdout=subprocess.PIPE).communicate()[0]
        print(process) """
        


def getUsersData():
        output = subprocess.Popen(['w'], stdout=subprocess.PIPE).stdout.readlines()
        headers = [h for h in ' '.join(output[1].strip().split()).split() if h]
        raw_data = map(lambda s: s.strip().split(None, len(headers) - 1), output[1:])
        pprint.pprint([dict(zip(headers, r)) for r in raw_data])
        return [dict(zip(headers, r)) for r in raw_data]
        """ w = subprocess.Popen(['who'], stdout=subprocess.PIPE)
        data = w.stdout.read()
        print(json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))) """
    
    




def getProcessData():
        output = subprocess.Popen(['ps', '-l'], stdout=subprocess.PIPE).stdout.readlines()
        headers = [h for h in ' '.join(output[0].strip().split()).split() if h]
        raw_data = map(lambda s: s.strip().split(None, len(headers) - 1), output[1:])
        return [dict(zip(headers, r)) for r in raw_data]

def getOSData():
        os_info = dict()
        if(platform.system().lower() == 'linux' or platform.system().lower() == 'linux2'):
                os_info.update(name = platform.dist()[0])
                os_info.update(version = platform.dist()[1])
        else:
                os_info.update(name = platform.system())
                os_info.update(version = platform.release())
        return os_info

main()
