## debug command used to prevent actual shell calls, just logs everything.
debug = False

### Eventually replace this with a real .cfg file and parser instead of just importing

## Environment settings
user = "robottest"
working_directory = "/disk1/hadoopUsers/" + user + "/Josh/p_test/"


ec_val_url = ""
ec_pub_url = ""

## Hadoop settings

##### SACHI II ####

hdfs_jobTracker = "schisadn100.hq.navteq.com:8021"
hdfs_nameNode = "hdfs://dev3dhdfs1"

hdfs_directory = hdfs_nameNode + "/user/robottest/Josh/p_test/"

hdfs_oozie_interface = "http://schisadn101:11000/oozie/"


## Component settings
## Relocate these to component files? Hard-coded?
ec_buildings_path = "/bison/EarthCore/Buildings/"
ec_buildings_name = "ec-building-deploy-*.zip"
ec_validations_deployment = "/bison/EarthCore/Validation/"
ec_validations_name = "earthcore-*-assembly.zip"
