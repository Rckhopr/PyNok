import os
### Eventually replace this with a real .cfg file and parser instead of just importing

class Pylot_Config():
    """
    Houses the configuration data for Pylot
    """
    def __init__(self, RunID):
        ## debug command used to prevent actual shell calls, just logs everything.
        self.debug = False
        
        ## Pylot settings
        ## Generate RunID -- For now a formatted timestamp. TODO: Revise RunID?
        self.runID = RunID
        
        ## Path names
        script_dir = os.path.dirname(__file__)
        self.dir_pylot = os.path.abspath(script_dir + "/../") + "/"
        self.dir_core = self.dir_pylot + "Core/"
        self.dir_settings = self.dir_pylot + "Settings/"
        self.dir_components = self.dir_pylot + "Components/"
        self.dir_tests = self.dir_pylot + "Tests/"
        self.dir_run = self.dir_tests + "TestRun_" + str(self.runID) + "/"
        self.dir_logs = self.dir_run + "Logs/"
        
        ## Hadoop settings
        ##### SACHI II ####
        self.hdfs_jobTracker = "schisadn100.hq.navteq.com:8021"
        self.hdfs_nameNode = "hdfs://dev3dhdfs1"
        self.hdfs_directory = self.hdfs_nameNode + "/user/robottest/Josh/p_test/"
        self.hdfs_oozie_interface = "http://schisadn101:11000/oozie/"

