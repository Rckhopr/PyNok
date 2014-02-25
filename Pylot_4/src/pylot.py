import sys
from steward import *

def pylot_tests(argv):
    """
    Command Line Interface Coming Soon...?
    """
    ### Grab latest pylot from mercurial (or whatever)
    ### Run the requested component (e.g. ECBuildings)
    ### Clean up all created directories/files, leaving only pylot and cfg file
    
    ## Hard Coded awesomeness!!
    
    ## Remove directory (if it exists), then create it.
    subprocess.call('rm -R ' + pylot_cfg.working_directory, shell=True)
    subprocess.call('mkdir ' + pylot_cfg.working_directory, shell=True)
    
    myClass = ComponentFunctions.IT_ECBuildings(components = ["buildingMatch", "elevate", "enricher", "landmarkMatch"])
    
    myClass.Deploy()
    myClass.Configure()
    myClass.Run()
    subprocess.call('echo Run complete...', shell=True)
    subprocess.call('echo Removing .pyc files...', shell=True)
    subprocess.call('rm *.pyc', shell=True)
#    subprocess.call('echo Removing ' + pylot_cfg.working_directory, shell=True)
#    subprocess.call('rm -R ' + pylot_cfg.working_directory, shell=True)
#    subprocess.call('echo Removing ' + myClass.deploy_directory, shell=True)
#    subprocess.call('rm -R ' + myClass.deploy_directory, shell=True)
    


### Probably don't need this until I actually create a real cfg file and parse
### it into a config object to toss around. For now it's just an awk. setting
### file and doesn't need processing.
#===============================================================================
# class Pylot():
# 
#    def __init__(self):
#        """ Initialize any required variables, e.g. Component to be run."""
#        pass
# 
#    def LoadConfig(self):
#        """ Load settings from a Config File? Or pass them through CLI? """
#        pass
# 
#    def RunComponent(self):
#        """ Using CLI params and/or Config settings, run the stesp for the
#        requested component. """
#        pass
#===============================================================================


if __name__ == '__main__':
    pylot_tests(sys.argv[1:])
