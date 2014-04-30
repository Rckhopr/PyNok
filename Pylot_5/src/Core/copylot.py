import re

class TestComponent():
    """
    Base component class.
    Other components, e.g. EC-Val, will inherit from this. 
    """
    def __init__(self, steward):
        """
        Requires a Steward and a Pylot_Config
        """
        self.steward = steward
    
    ## assert(0) because this class should never be directly used.
    def Deploy(self):
        """
        Deploy the component. Required function.
        """
        assert(0)
    
    def Configure(self):
        """
        Configure the environment. Required function.
        """
        assert(0)
    
    ## TODO: Rename Test or RunTest?
    def Run(self):
        """
        Execute the component.
        Do run configurations (e.g. set up test scenario)
        Run tests
        """
        assert(0)

    #### Generic Functions
    ## TODO: Consider moving file read/write to steward for running in debug?
    ## May not be valuable. Perhaps giving a fake file set to use in debug?

    def _config_xml(self, source, dest, setting_dict):
        """
        Reproduces the source file as the dest file, using
        setting_dict to define what should be changed.
        
        For "xml" files where contents take the form:
        <name>KEY</name>
        <value>VALUE</value>
        
        source:       Original / template file
        dest:         name of the destination file (same as source to overwrite)
        setting_dict: dictionary of the key/value pairs to modify
                      keys not in this dict will retain their original value
        """
        # Grab the source lines
        myfile = open(source, 'r')
        lines_in = myfile.readlines()
        myfile.close()

        # Build the output
        lines_out = ""
        key_found = 'null'
        for line in lines_in:
            if key_found in setting_dict:
                value = setting_dict.pop(key_found)
                line = re.sub("<value>.*?</value>", '<value>' + value + '</value>', line)
                
                self.steward.echo('Setting ' + key_found + ' to ' + value)
                key_found = 'null'
            else:
                print key_found
                for key in setting_dict:
                    if "<name>" + key + "</name>" in line:
                        key_found = key
                        break
            lines_out += line#.strip('\n') + '\n'
        # Write the output
        myfile = open(dest, 'w')
        myfile.write(lines_out)
        myfile.close()

    def _config_properties(self, source, dest, setting_dict):
        """
        Reproduces the source file as the dest file, using
        setting_dict to define what should be changed.
        
        For "properties" files where contents take the form:
        key=value
        
        source:       Original / template file
        dest:         name of the destination file (same as source to overwrite)
        setting_dict: dictionary of the key/value pairs to modify
                      keys not in this dict will retain their original value
        """

        # Grab the source lines
        myfile =  open(source, 'r')
        lines_in = myfile.readlines()
        myfile.close()

        # Build the output
        lines_out = ""
        for line in lines_in:
            for key in setting_dict:
                if line.startswith(line + '='):
                    line = key + '=' + setting_dict[key] + '\n'
                    self.steward.echo('Setting ' + key + ' to ' + setting_dict[key])
                    break
            lines_out += line

        # Write the output
        myfile = open(dest, 'w')
        myfile.write(lines_out)
        myfile.close()

    def _get_component(self, path, target, unzip):
        """
        Gets the requested components, and unzips if it asked.
        path: directory where component can be found
        target: name of file to copy
        unzip: True/False, whether or not to unzip the file
        """
        self.steward.echo('Grabbing component from ' + path + target + ' and putting it in: ' + self.steward.pylot_cfg.dir_testrun)
        self.steward.call('cp ' + path + target + ' ' + self.steward.pylot_cfg.dir_testrun)
        self.steward.call('chmod 777 ' + self.steward.pylot_cfg.dir_testrun + target)
        if unzip:
            self.steward.echo('Unzipping...')
            self.steward.call('unzip ' + self.steward.pylot_cfg.dir_testrun + target + ' -d ' + self.steward.pylot_cfg.dir_testrun)