from steward import *


class IT_ECBuildings():

    def __init__(self, components):
        self.components = components
        
        ## List of stuff I support
        self.supported_components = ["elevate", "enricher", "landmarkMatch", "buildingMatch"]
        ##self.supported_components = ["enricher"]

    def Deploy(self):
        """
        Grabs the artifact, creates the deploy.sh script and executes it.
        This pushes everything into HDFS and sets up the EC Buildings directories
        with job.property files already mostly populated.
        """
        echo('Getting artifact for ECBuildings ' + pylot_cfg.ec_buildings_version)
        CoPylot._get_component(path = pylot_cfg.ec_buildings_path + 'v' + pylot_cfg.ec_buildings_version + '/',
                       target = pylot_cfg.ec_buildings_name,
                       unzip = True)
        echo('Deploying build...')
        self._create_deploy_script()
        call(pylot_cfg.working_directory + 'ec_building_deploy/p-deploy.sh')
        ## This is where I want it.
        #self.deploy_directory = pylot_cfg.working_directory + 'ec_building_deploy/ec_building/'
        ## This is where it is.
        self.deploy_directory = '/disk1/hadoopUsers/earthcoredpl/Josh/p/ec_building/'

    def Configure(self):
        """
        Creates job.properties files and populates necessary settings.
        """
        for item in ["buildingMatch", "elevate", "enricher", "landmarkMatch"]:
            echo('Configuring ' + item)
            jobprop_orig = open(self.deploy_directory + item + '/job.properties', 'r')
            pylot_job = open(self.deploy_directory + item +'/pylot_job.properties', 'w')
            orig_lines = jobprop_orig.readlines()
            
            ## TODO: Convert to dictionary(?) and pass to a Steward function
            for line in orig_lines:
                if line == "boundingBox=\"\"\n" or line == "boundingBox=\n":
                    line = "boundingBox=\"" + pylot_cfg.bounding_box + "\"\n"
                elif line == "tileFileHdfsPath=\n":
                    line = "tileFileHdfsPath=" + pylot_cfg.hdfs_directory + item + '/' + pylot_cfg.tile_file
                elif line == "rmob1_url=username1/password1@host1:instance1\n":
                    line = 'rmob1_url=WEU_MAP_IW/password@tchirdcdb04.hq.navteq.com:WE1MPRPT\n'
                elif line == "rmob1_bbox=rmob1Bbox\n":
                    line = 'rmob1_bbox="41.9,41.8,-87.5,-87.6"\n'
                elif line == "rmob2_url=username2/password2@host2:instance2\n":
                    line = 'rmob2_url=""\n'
                elif line == "rmob2_bbox=rmob2Bbox\n":
                    line = 'rmob2_bbox=""\n'
                elif line == "rmob3_url=username3/password3@host3:instance3\n":
                    line = 'rmob3_url=""\n'
                elif line == "rmob3_bbox=rmob3Bbox\n":
                    line = 'rmob3_url=""\n'
                pylot_job.write(line)
            jobprop_orig.close()
            pylot_job.close()
        ## TODO: Learn steps for:
        ## delete
        ## extractor
        ## publication
        ## roadCollisionDetector

    def Run(self):
        """
        Execute the oozie workflows.
        One at a time, polling for completion before moving on.
        """
        for component in self.components:
            if component not in self.supported_components:
                echo(component + ' not supported.')
            else:
                job_id = run_oozie_workflow(self.deploy_directory, component)
                status = ""
                x = 0
                while (x < 120):
                    x += 1
                    time.sleep(60)
                    status = get_oozie_status(job_id)
                    echo(component + ' run ' + job_id + ': ' + status)
                    if (status == "KILLED" or status == "FAILED" or status == "SUCCEEDED"):
                        break;
                    elif (status == "RUNNING"):
                        echo('Runtime: ' + str(x) + ' minutes.')
                    else:
                        echo('Status set to "' + status + '" - Assuming something is wrong, abort.')
                        break;


    ## Custom Functions
    def _create_deploy_script(self):
        deploy_script = open(pylot_cfg.working_directory + 'ec_building_deploy/p-deploy.sh', 'w')

        deploy_script.write('#!/bin/bash\n')
        deploy_script.write('jobTracker="' + pylot_cfg.hdfs_jobTracker + '"\n')
        deploy_script.write('nameNode="' + pylot_cfg.hdfs_nameNode + '"\n')
        deploy_script.write('ecServer="' + pylot_cfg.ec_url + '"\n')
        deploy_script.write('demServer="' + pylot_cfg.demServer + '"\n')
        deploy_script.write('lroServer="' + pylot_cfg.lroServer + '"\n')
        deploy_script.write('egisServer="' + pylot_cfg.egis_url + '"\n')
        deploy_script.write('hdfsInstallPath="' + pylot_cfg.hdfs_directory + '"\n')
        deploy_script.write('cacheUser="' + pylot_cfg.cacheUser + '"\n')
        deploy_script.write('cacheProduct="' + pylot_cfg.cacheProduct + '"\n')
        deploy_script.write('countryCachePath="' + pylot_cfg.countryCachePath + '"\n')
        deploy_script.write('rmobCacheName="' + pylot_cfg.rmobCacheName + '"\n')
        deploy_script.write('\n# The zip file to extract onto the current edge node\n')
        deploy_script.write('edgeZip=`find ' + pylot_cfg.working_directory + ' -type f -name ec-building-edge-*.zip`\n')
        deploy_script.write('\n# The zip file to extract onto HDFS\n')
        deploy_script.write('hadoopZip=`find ' + pylot_cfg.working_directory + ' -type f -name ec-building-hadoop-*.zip`\n')
        deploy_script.write('\n# Clears the installation directories before extracting\n')
        deploy_script.write('clean="-clean"\n')
        deploy_script.write('\nhadoop jar ' + pylot_cfg.working_directory + 'ec_building_deploy/deploy-jar-with-dependencies.jar com.nokia.ec.HadoopExtractor -jobTracker $jobTracker -nameNode $nameNode -ecServer $ecServer -demServer $demServer -lroServer $lroServer -egisServer $egisServer -hdfsInstallPath $hdfsInstallPath -cacheUser $cacheUser -cacheProduct $cacheProduct -countryCachePath $countryCachePath -rmobCacheName $rmobCacheName -edgeZip $edgeZip -hadoopZip $hadoopZip $clean')
        
        deploy_script.close()
        call('chmod 777 ' + pylot_cfg.working_directory + 'ec_building_deploy/p-deploy.sh')
        call('chmod 777 -R ' + pylot_cfg.working_directory)

def IT_ECBuildings_f():
    subprocess.call('echo Running ECBuildings...', shell=True)

def IT_3DLRP():
    """ Probably need to interact with either BPM API or EGIS """
    subprocess.call('echo 3DLRP not yet implemented.', shell=True)

def IT_BuildingAttribution():
    subprocess.call('echo BuildingAttribution not yet implemented.', shell=True)

def IT_OTD():
    subprocess.call('echo OTD not yet implemented.', shell=True)

def IT_Earthcore():
    subprocess.call('echo Earthcore not yet implemented.', shell=True)

def BCP():
    subprocess.call('echo BCP not yet implemented', shell=True)

def IT_ECValidation():
    subprocess.call('echo Validations not yet implemented', shell=True)
    
    ### Migrate the validation database
    # cp /bison/EarthCore/Validation/v4.1/earthcore-4.1-assembly.zip
    # unzip earthcore-4.1-assembly.zip
    # flyway.sh -user=T_EC_VALIDATION_3_3 -password=password -url=jdbc:oracle:thin:@dchi3dcent04.hq.navteq.com:1521:yellow migrate

    ### Set up the validation server
    # ?
    # ?
    # ?

    ## Run the validation
    # Set up job.properties, config-default.xml, h_config.xml
    # Push files into HDFS (config-default, h_config, rule_configuration, rules.prop, workflow.xml, sofiles/(sofiles), lib/(jar file))
    # oozie job -oozie http://schisadn101.hq.navteq.com:11000/oozie/ -config job.properties -run