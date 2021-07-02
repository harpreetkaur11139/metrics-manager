import os 

def cpu_usage():
    cpu=open("/proc/stat")
    temp=cpu.readlines()[0].split()
    total_time= sum(map(int,temp[1:]))
    idle_time=int(temp[4])
    cpu_per=(1-(idle_time/total_time))*100
    return {"CPU_Usage" : cpu_per }

def load_average():
    return {"load_avg" : os.getloadavg() }

def disk_usage():
    return 
    

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