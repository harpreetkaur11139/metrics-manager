import metrics
import datetime 
import socket
import time  
import json
import requests 

host_name=socket.gethostname()

class DateTimeEncoder(json.JSONEncoder):
    def default(self, z):
        if isinstance(z, datetime.datetime):
            return (str(z))
        else:
            return super().default(z)

def collect_data():
    dct={"Timestamp":"", "Hostname": "", "Metrics":{}}
    dct["Timestamp"]=datetime.datetime.now()
    dct["Hostname"]=host_name
    dct["Metrics"]["CPU"]=metrics.cpu_usage()
    dct["Metrics"]["Memory"]=metrics.memory_usage()
    dct["Metrics"]["Network"]=metrics.network_usage()
    dct["Metrics"]["Disk"]=metrics.disk_usage()
    dct["Metrics"]["Inode"]=metrics.inode_usage()
    dct["Metrics"]["Port"]=metrics.open_ports()
    dct["Metrics"]["LoadAverage"]=metrics.load_average()
    return dct

def send_data(data):
    """
    API_Endpoint = "http://maps.googleapis.com/maps/api/geocode/json"
    API_KEY = "XXXXXXXXXXXXXXXXX"
    r = requests.post(url = API_ENDPOINT, data = data)
    pastebin_url = r.text
    print("The pastebin URL is:%s"%pastebin_url)"""

    API_ENDPOINT = "http://localhost:5001/metrics"
    headers = {'content-type': 'application/json'}
    r = requests.post(API_ENDPOINT, data = json.dumps(data,cls=DateTimeEncoder), headers = headers)
    return r
    
def store_data():
    while True:
        data=collect_data()
        send_data(data)
        time.sleep(60)
