import environment

## Validations Settings
## These are specific to the EC-Validations pipeline

## Environment Settings
validation_url = ""
ecpub_url = ""


## Environment dictionaries
## This defines what gets changed in which files

config_default = {
"jobTracker" : environment.hdfs_jobTracker,
"nameNode" : environment.hdfs_nameNode
}

job_properties = {
"oozie.wf.application.path" : environment.hdfs_nameNode + environment.hdfs_directory,
"output" : environment.hdfs_directory + "output",
"validationServer" : validation_url,
"ecpubServer" : ecpub_url,
"ruleConfigFile" : environment.hdfs_directory + "rule_configuration_file.txt",
"ruleProps" : environment.hdfs_directory + "rules.properties"
}