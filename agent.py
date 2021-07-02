#Agent code 
import os
import click

def cpu_usage():
    cpu=open("/proc/stat")
    temp=cpu.readlines()[0].split()
    total_time= sum(map(int,temp[1:]))
    idle_time=int(temp[4])
    cpu_per=(1-(idle_time/total_time))*100
    return cpu_per

def load_average():
    return os.getloadavg()

def disk_usage():
    

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
    return {"MemoryUsagein kB": MemoryUsed, "SwapUsed in kB": SwapUsed}

@click.command()
@click.option('-c', '--cpu', is_flag=True, help='Prints CPU Percentage usage')
@click.option('-m', '--memory', is_flag=True, help='Prints Memory Percentage usage')
@click.option('-la', '--loadavg', is_flag=True, help='Prints Load average of system')
def main(cpu,memory,loadavg):
    if cpu:
        print(cpu_usage())
    if memory:
        print(memory_usage())
    if loadavg:
        print(load_average())









