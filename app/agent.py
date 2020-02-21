import subprocess
import json
import platform
import requests

def main():
        os_info = getOSData()
        data = {
                "process_data": getProcessData(),
                "os_name": os_info['name'],
                "os_version": os_info['version'],
                "users": getUsersData(),
                "cpu": getCPUData()
        } 

        #doRequest(data)
        print(json.dumps(data)) 


def doRequest(server_data):
        r = requests.post(url = 'http://localhost:80/save', data = server_data)
        response = r.text
        print(response)

def getCPUData():
        cpu_type = subprocess.Popen(['uname','-p'], stdout=subprocess.PIPE).stdout.readlines()[0].strip('\n')
        model_name = subprocess.Popen(["cat /proc/cpuinfo | grep 'model name' | uniq"], stdout=subprocess.PIPE, shell=True).stdout.readlines()[0].split(':')
        usage = subprocess.Popen(["top -bn1 | awk '/Cpu/ { cpu =  100 - $8 }; END { print cpu }'"], stdout=subprocess.PIPE, shell=True).stdout.readlines()[0].split(',  ')
        uptime_active = subprocess.Popen(['uptime -p'], stdout=subprocess.PIPE, shell=True).stdout.readlines()[0].strip('up')
        cpu_data = {
                "type" : cpu_type,
                "model": model_name[1].strip('\n'),
                "usage": usage[0].replace('\n', '%'),
                "uptime": uptime_active.strip('\n')
        } 
        return cpu_data

def getUsersData():
        output = subprocess.Popen(["who | awk 'BEGIN {print \"NAME LINE DATE HOUR\"} {if(NR > 1) print $1, $2, $3, $4}'"], stdout=subprocess.PIPE, shell=True).stdout.readlines()
        headers = [h for h in ' '.join(output[0].strip().split()).split() if h]
        raw_data = map(lambda s: s.strip().split(None, len(headers) - 1), output[1:])
        return [dict(zip(headers, r)) for r in raw_data]
    
    
def getProcessData():
        output = subprocess.Popen(['ps', '-l'], stdout=subprocess.PIPE).stdout.readlines()
        headers = [h for h in ' '.join(output[0].strip().split()).split() if h]
        raw_data = map(lambda s: s.strip().split(None, len(headers) - 1), output[1:])
        return [dict(zip(headers, r)) for r in raw_data]

def getOSData():
        if(platform.system().lower() == 'linux' or platform.system().lower() == 'linux2'):
                os_info = {
                        "name": platform.dist()[0],
                        "version": platform.dist()[1]
                }
        else:
                os_info = {
                        "name": platform.system(),
                        "version": platform.release()
                }
        return os_info

main()
