#Agent code 
import os
import click
import datetime 
import socket 
import metrics
from pprint import pprint

VERSION = "0.1.0"

class MetricsObject():
    def __init__(self):
        self.metric_obj = {}
        self.metric_obj["timestamp"] = datetime.datetime.now()
        self.metric_obj["hostname"] = socket.gethostname()
        self.metric_obj["metrics"] = []
    

def validate_user():
    user_id = os.getuid()
    if user_id != 0:
        return False 
    return True


@click.command()
@click.option('-c', '--cpu', is_flag=True, help='Prints CPU Percentage usage')
@click.option('-m', '--memory', is_flag=True, help='Prints Memory Percentage usage')
@click.option('-l', '--loadavg', is_flag=True, help='Prints Load average of system')
@click.option('-p', '--ports', is_flag=True, help='Prints open ports')
@click.option('-d', '--disk', is_flag=True, help='Prints disk usage')
@click.option('-i', '--inode', is_flag=True, help='Prints Inode usage')
@click.option('-n', '--network', is_flag=True, help='Prints Network packets')
def main(cpu,memory,loadavg, ports,disk,inode,network):
    """
    The utiility for metric collector... 
    """
    ctx = click.get_current_context()
    root_user = validate_user()
    if not root_user:
        click.echo(click.style("Command needs root privileges to gather metrics\nNot run with root privileges, so exiting...", fg='red'))
        ctx.exit()

    if True not in ctx.params.values():
        click.echo(ctx.get_help())
        ctx.exit()
    
    if cpu:
        print(metrics.cpu_usage())
    if memory:
        print(metrics.memory_usage())
    if loadavg:
        print(metrics.load_average())
    if ports:
        print(metrics.open_ports())
    if disk:
        print(metrics.disk_usage())
    if inode:
        print(metrics.inode_usage())
    if network:
        print(metrics.network_usage())


