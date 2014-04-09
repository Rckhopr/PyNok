from steward import *


def IT_ECValidation(Pylot_Component):

    def __init__(self, version):
        """
        version: Numbers only. Ex. "4.1.4"
        """
        self.vers_num = version.strip('v')
        self.version = "v" + self.vers_num

    def Deploy(self):
        """
        Grabs the artifact.
        TODO: ...? Decide if Pylot should get into real deployment
                    E.g. -- Setting up webservice & migrating DB.
        """
        echo("Getting artifact for EC-Validation " + self.version)
        self._get_component(path = pylot_cfg.ec_validations_deployment,
                               target = pylot_cfg.ec_validations_name,
                               unzip = True)

    def Configure(self, test = "Default"):
        """
        Set up the property files.
        Push necessary files into HDFS.
        
        test: Defines the test to be configured.
        """
        self._config_xml()

    def Run(self):
        """
        Execute the oozie workflow.
        """
        pass



### Notes on running Validation:

    ### Migrate the validation database
    # cp /bison/EarthCore/Validation/v4.1/earthcore-4.1-assembly.zip
    # unzip earthcore-4.1-assembly.zip
    # flyway.sh -user=EC_VAL -password=password -url=jdbc:oracle:thin:@dchi3dcent04.hq.navteq.com:1521:yellow migrate

    ### Set up the validation server
    # ?
    # ?
    # ?

    ## Run the validation
    # Set up job.properties, config-default.xml, h_config.xml
    # Push files into HDFS (config-default, h_config, rule_configuration, rules.prop, workflow.xml, jar file (/lib))
    # oozie job -oozie http://schisadn101.hq.navteq.com:11000/oozie/ -config job.properties -run