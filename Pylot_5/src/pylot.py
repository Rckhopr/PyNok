import sys
import time
import datetime
import getopt

from Core.config import Pylot_Config
from Core.steward import Steward

def pylot(argv):
    """
    Command Line Interface for Pylot.
    """
    
    ## Create Run ID
    RunID = datetime.datetime.fromtimestamp(int(time.time())).strftime('%Y-%m-%d %H:%M:%S')
    
    ## Initialize Core
    pylot_cfg = Pylot_Config(RunID)
    steward = Steward(pylot_cfg)
    
    ## Raise error if invalid arguments are given
    try:
        opts, args = getopt.getopt(argv,"uhc:v:t:",["usage","help","component=","version=","test="])
    except getopt.GetoptError:
        Usage(1)
    
    component = "NULL"
    version = "NULL"
    test = "DEFAULT"

    for opt, arg in opts:
        if opt in ('-u', '--usage', '-h', '--help'):
            ## "Usage" or "Help"
            Usage(0)
        elif opt in ('-c', '--component'):
            component = arg
        elif opt in ('-v', '--version'):
            version = arg
        elif opt in ('-t', '--test'):
            test = arg
        else:
            Usage(0)
    
    if (component != "NULL" and version != "NULL"):
        ## TODO: Add test calls here when available
        'testComponent = CoPylot.Test(component, version, test)'
        'testComponent.Deploy()'
        'testComponent.Config()'
        'testComponent.Run()'
        print "Input:"
        print "Component: " + component
        print "Version: " + version
        print "Test: " + test
    else:
        Usage(2)


def Usage(code):
    """
    Display usage instructions.
    """
    ## TODO: Create real usage message.
    ## TODO: Possibly include error code
    print "Usage Message"
    exit(code)


if __name__ == '__main__':
    pylot(sys.argv[1:])