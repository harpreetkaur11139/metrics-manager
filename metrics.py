import os 
import socket

def cpu_usage():
    cpu=open("/proc/stat")
    temp=cpu.readlines()[0].split()
    total_time= sum(map(int,temp[1:]))
    idle_time=int(temp[4])
    cpu_per=(1-(idle_time/total_time))*100
    cpu.seek(0)
    for i in cpu.readlines():
        if i.split(" ")[0] == "procs_running":
            process_count=i.split(" ")[1].strip()
    cpu.close()
    return {"CPU_Usage" : cpu_per, "Process_Running" :  process_count}

def load_average():
    return {"load_avg" : os.getloadavg() }

def disk_usage():
    return 

def open_ports():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #sock.settimeout(10)
    ls=[]
    for i in range(1,65535):
        result = sock.connect_ex(('127.0.0.1',i))
        #result == 0 for open port and not 0 for closed port
        if result == 0:
            ls.append(i)
    sock.close()
    return {"TCP_Ports_open:":ls}
    

def memory_usage():
    memory=open("/proc/meminfo")
    for i in memory.readlines():
        if i.split(":")[0] == "MemTotal":
            MT=i.split(":")[1].strip()
        if i.split(":")[0] == "MemFree":
            MF=i.split(":")[1].strip()
        if i.split(":")[0] == "SwapTotal":
            ST=i.split(":")[1].strip()
        if i.split(":")[0] == "SwapFree":
            SF=i.split(":")[1].strip()
    MemoryUsed=int(MT[:-3])-int(MF[:-3])
    SwapUsed=int(ST[:-3])-int(SF[:-3])
    return {"MemoryUsagekB": MemoryUsed, "SwapUsedkB": SwapUsed}