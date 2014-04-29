import subprocess

class Steward():
    """
    Steward contains wrapper functions for various system calls.
    Requires the Run ID be passed in to identify the logfile
    """
    def __init__(self, pyconfig):
        """
        Requires a Pylot_Config object
        """
        self.pylot_cfg = pyconfig
        self.logfile = pyconfig.dir_logs + 'Pylot.log'
    
    def echo(self, my_string):
        """
        Prints to screen, with Pylot: prefix
        """
        my_string = "Pylot:    " + my_string
        if not (self.pylot_cfg.debug):
            print my_string
        self.log(my_string)
    
    def echo_no_log(self, my_string):
        """
        Prints to screen, with Pylot: prefix
        Note: Does not call logging function
        """
        my_string = "Pylot:    " + my_string
        if not (self.pylot_cfg.debug):
            print my_string
        else:
            self.log('(NoLog) ' + my_string)
    
    def setLogFile(self, logfile):
        """
        Change the file that log() will write to
        """
        self.log("Log set to: " + logfile)
        self.logfile = logfile
    
    def log(self, my_string):
        """
        Log to a file (pylot.log probably)
        """
        ## Open/Close each call is ridiculously inefficient.
        ## This was just a quick solution to build from
        ## TODO: Improve the logging mechanism
        logto = open(self.logfile, 'a')
        logto.write(my_string)
        logto.close()
        
    def call(self, command_str):
        """
        Wraps subprocess.call
        Does not give a return value
        """
        if not (self.pylot_cfg.debug):
            subprocess.call(command_str, shell=True)
        self.log(command_str)
    
    def call_return(self, command_str):
        """
        Wraps subprocess.check_output
        Passes return value through
        """
        self.log(command_str)
        if not (self.pylot_cfg.debug):
            return subprocess.check_output(command_str, shell=True)
        else:
            return 'Debug_Enabled'
    
    def get_oozie_status(self, job_id):
        """
        Wraps steward.call_return
        Constructs the call to get the status of an oozie job
        Returns the status
        """
        self.echo('Checking status...')
        status = self.call_return("oozie job -oozie " + self.pylot_cfg.hdfs_oozie_interface + " -info " + job_id + " | grep 'Status' | grep ':' | awk '{print $NF}'")
        status = status.strip('\n')
        return status
    
    def run_oozie_workflow(self, deploy_directory, component):
        """
        Wraps steward.call_return
        Constructs the call to start an oozie job 
        Returns the job_id
        """
        self.echo('Running ' + component)
        job_id = self.call_return("oozie job -oozie " + self.pylot_cfg.hdfs_oozie_interface + " -config " + deploy_directory + component + "/pylot_job.properties -run | awk '{print $NF}'")
        job_id = job_id.strip('\n')
        self.echo('job_id: ' + job_id)
        return job_id
    