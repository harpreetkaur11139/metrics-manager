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

@click.command()
@click.option('-c', '--cpu', is_flag=True, help='Prints CPU Percentage usage')
@click.option('-m', '--memory', is_flag=True, help='Prints Memory Percentage usage')
def main(cpu,memory):
    if cpu:
        print(cpu_usage())
    if memory:
        print("memory_usage()")








