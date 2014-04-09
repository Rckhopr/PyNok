import subprocess
import pylot_cfg
import ComponentFunctions
import CoPylot
import time




def echo(my_string):
    """
    Prints to screen, with Pylot: prefix
    """
    my_string = "Pylot:    " + my_string
    if not (pylot_cfg.debug):
        #subprocess.call('echo ' + my_string, shell=True)
        print my_string
    log(my_string)

def echo_no_log(my_string):
    """
    Prints to screen, with Pylot: prefix
    Note: Does not call logging function
    """
    my_string = "Pylot:    " + my_string
    if not (pylot_cfg.debug):
        #subprocess.call('echo ' + my_string, shell=True)
        print my_string
    else:
        log('(NoLog) ' + my_string)

def log(my_string):
    """
    TODO: Log to a file (pylot.log probably)
    """
    print my_string
    ## Figure out logging

def call(command_str):
    """
    Wraps subprocess.call
    Does not give a return value
    """
    if not (pylot_cfg.debug):
        subprocess.call(command_str, shell=True)
    log(command_str)

def call_return(command_str):
    """
    Wraps subprocess.check_output
    Passes return value through
    """
    log(command_str)
    if not (pylot_cfg.debug):
        return subprocess.check_output(command_str, shell=True)
    else:
        return 'Debug_Enabled'

def get_oozie_status(job_id):
    """
    Wraps steward.call_return
    Constructs the call to get the status of an oozie job
    Returns the status
    """
    echo('Checking status...')
    status = call_return("oozie job -oozie " + pylot_cfg.hdfs_oozie_interface + " -info " + job_id + " | grep 'Status' | grep ':' | awk '{print $NF}'")
    status = status.strip('\n')
    return status

def run_oozie_workflow(deploy_directory, component):
    """
    Wraps steward.call_return
    Constructs the call to start an oozie job 
    Returns the job_id
    """
    echo('Running ' + component)
    job_id = call_return("oozie job -oozie " + pylot_cfg.hdfs_oozie_interface + " -config " + deploy_directory + component + "/pylot_job.properties -run | awk '{print $NF}'")
    job_id = job_id.strip('\n')
    echo('job_id: ' + job_id)
    return job_id
