

### Eventually replace this with a real .cfg file and parser instead of just importing



## Environment settings
user = "earthcoredpl" ## Not sure I need this
working_directory = "/disk1/hadoopUsers/" + user + "/Josh/p_test/"

ec_buildings_version = "5.2"
ec_url = "http://10.8.24.149:19990/ec-web"
demServer = "http://dtm-web.3d.solo-experiments.com/dtm-web/published/"
lroServer = "http://dchiecapp03:8080/jv-dmo-service/v1/buildingsIds"
egis_url = "http://tegissvcs01:15211/EgisServices"

###########

## Unique tags/names/etc
user_id = "JP"

cacheUser = "earthcoredpl"
cacheProduct = "3dit" + user_id + "Cache"
rmobCacheName = "3dit" + user_id + "RmobCache"
countryCachePath = "/user/earthcoredpl/3dit/CountryGeoCache"
############

## Run specific settings

## TODO: Set up presets with logical names (E.g. "Chicago")
bounding_box = "32.724600145464,32.704400963283,-117.14808449191,-117.17640716794"
tile_file = "/user/earthcoredpl/3dit/Josh/p/"

############



## Hadoop settings

##### SACHI II ####

hdfs_jobTracker = "schisadn100.hq.navteq.com:8021"
hdfs_nameNode = "hdfs://schisadn098.hq.navteq.com:8020"

hdfs_directory = hdfs_nameNode + "/user/robottest/Josh/p_test/"

hdfs_oozie_interface = "http://schisadn101:11000/oozie/"


##### SANDBOX #####

hdfs_jobTracker = "sachidn001.hq.navteq.com:8021"
hdfs_nameNode = "hdfs://sandbox3dhdfs1"

hdfs_directory = hdfs_nameNode + "/user/earthcoredpl/3dit/Josh/p_test/"

hdfs_oozie_interface = "http://sachidn002:11000/oozie/"

### oozie job -oozie http://sachidn002:11000/oozie/ -config job.properties -run

############

## Component settings
ec_buildings_path = "/bison/EarthCore/Buildings/"
ec_buildings_name = "ec-building-deploy-*.zip"


## Old stuff
#hdfs_host = "hdfs://dev3dhdfs1"
#hdfs_path = "/user/pylot"