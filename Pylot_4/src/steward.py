import subprocess
from pylot_cfg import *




def echo(my_string):
    subprocess.call('echo ' + my_string, shell=True)
    log(my_string)

def echo_no_log(my_string):
    subprocess.call('echo ' + my_string, shell=True)

def log(my_string):
    pass
    ## Figure out logging

def call(command_str):
    subprocess.call(command_str, shell=True)

def call_return(command_str):
    return subprocess.check_output(command_str, shell=True)

def get_oozie_status(job_id):
    echo('Checking status...')
    return call_return("oozie job -oozie " + hdfs_oozie_interface + " -info " + job_id + " | grep 'Status' | grep ':' | awk '{print $NF}'")