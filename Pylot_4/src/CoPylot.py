from steward import *


class Pylot_Component():
    """
    This is a shell class that all Components are derived from.
    """ 
    def __init__(self):
        pass
    
    ## assert(0) because this class should never be directly used.
    def Deploy(self):
        assert(0)
    
    def Configure(self):
        assert(0)
    
    def Run(self):
        assert(0)

def _get_component(path, target, unzip):
    """
    Gets the requested components, and unzips if it asked.
    path: directory where component can be found
    target: name of file to copy
    unzip: True/False, whether or not to unzip the file
    """
    echo('Grabbing component from ' + path + target + ' and putting it in: ' + pylot_cfg.working_directory)
    call('cp ' + path + target + ' ' + pylot_cfg.working_directory)
    call('chmod 777 ' + pylot_cfg.working_directory + '*.zip')
    if unzip:
        echo('Unzipping...')
        call('unzip ' + pylot_cfg.working_directory + target + ' -d ' + pylot_cfg.working_directory)


### Below moved to ComponentFunctions:
#===============================================================================
# def DeployComponents(component = "ECBuildings"):
# 
#    if (component == "ECBuildings"):
#        _get_component(path = pylot_cfg.ec_buildings_path + pylot_cfg.ec_buildings_version + '/',
#                       target = pylot_cfg.ec_buildings_name,
#                       unzip = True)
#        _ECBuildings_create_deploy()
#        subprocess.call(pylot_cfg.working_directory + '/p_deploy.sh')
#        
#        ## Modify job.properties, then run.
#        _ECBuildings_set_jobproperties()
#===============================================================================
#===============================================================================
# 
# def _ECBuildings_create_deploy():
#    #deploy_script = open(pylot_cfg.working_directory + '/p_deploy.sh', 'w')
#    
#    deploy_script = open('p_deploy.sh', 'w')
#    
#    deploy_script.write('#!/bin/bash\n')
#    deploy_script.write('jobTracker="' + pylot_cfg.hdfs_jobTracker + '"\n')
#    deploy_script.write('nameNode="' + pylot_cfg.hdfs_nameNode + '"\n')
#    deploy_script.write('ecServer="' + pylot_cfg.ec_url + '"\n')
#    deploy_script.write('demServer="' + pylot_cfg.demServer + '"\n')
#    deploy_script.write('lroServer="' + pylot_cfg.lroServer + '"\n')
#    deploy_script.write('egisServer="' + pylot_cfg.egis_url + '"\n')
#    deploy_script.write('hdfsInstallPath="' + pylot_cfg.hdfs_directory + '"\n')
#    deploy_script.write('cacheUser="' + pylot_cfg.cacheUser + '"\n')
#    deploy_script.write('cacheProduct="' + pylot_cfg.cacheProduct + '"\n')
#    deploy_script.write('countryCachePath="' + pylot_cfg.countryCachePath + '"\n')
#    deploy_script.write('rmobCacheName = "' + pylot_cfg.rmobCacheName + '"\n')
#    deploy_script.write('\n# The zip file to extract onto the current edge node\n')
#    deploy_script.write('edgeZip=`find $(dirname $0) -type f -name "ec-building-edge-*.zip"`\n')
#    deploy_script.write('\n# The zip file to extract onto HDFS\n')
#    deploy_script.write('hadoopZip=`find $(dirname $0) -type f -name "ec-building-hadoop-*.zip"`\n')
#    deploy_script.write('\n# Clears the installation directories before extracting\n')
#    deploy_script.write('"example-deploy.sh" 47L, 1726C\n')
#===============================================================================
