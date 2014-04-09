from steward import *
import re


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
                line = re.sub("<value>.*?</value>", '<value>' + setting_dict[key_found] + '</value>', line)
                #line = line.replace('<value>*</value>', '<value>' + setting_dict[key_found] + '</value>')
                
                echo('Setting ' + key_found + ' to ' + setting_dict[key_found])
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
                    echo('Setting ' + key + ' to ' + setting_dict[key])
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
        echo('Grabbing component from ' + path + target + ' and putting it in: ' + pylot_cfg.working_directory)
        call('cp ' + path + target + ' ' + pylot_cfg.working_directory)
        call('chmod 777 ' + pylot_cfg.working_directory + '*.zip')
        if unzip:
            echo('Unzipping...')
            call('unzip ' + pylot_cfg.working_directory + target + ' -d ' + pylot_cfg.working_directory)

