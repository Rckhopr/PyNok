import pylot_cfg

### Test Settings for EC Validations        

class TestDefinition():
    """
    Gets the correct settings for the requested test.
    Parameters:
        test:                name of test to run
        region_name:         name of region to run on (mapped to bb)
        NOTE: region_name is unused as of now.
    """
    ## TODO: Create region_name mapping
    def __init__(self, test = 'DEFAULT', region_name = 'CHICAGO', rule_set = 'DEFAULT', rule_list = []):
        
        self.settings_dict = {}
        self.rules_dict = {}
        self._getValidationTest(test, region_name, rule_set)

    def _getValidationTest(self, test = 'DEFAULT', region_name = 'CHICAGO', rule_set = 'DEFAULT'):
        
        test = test.lower()
        region_name = region_name.lower()
        rule_set = rule_set.lower()
        
        if (test == 'default'):
            test = 'full'
        if (region_name == 'default'):
            region_name = 'chicago'
        if (rule_set == 'default'):
            rule_set = 'all'
        
        self.settings_dict = getValTestSettings()
        self.rules_dict = getValRules(test)


## Automatic Version:
## TODO: Add input protections
##    getValTestSettings
##    getValRules

def getValTestSettings(scope = 'DEFAULT'):
    
    settings = {}

    if (scope == 'full'):
        settings = {'tileCoverageMode' : 'FULL'}
        
    elif (scope == 'small_tile'):
        settings = {'tileCoverageMode' : 'INCREMENTAL',
                    'changeQueryMethod' : 'FILE',
                    'tileFileHdfsPath' : 'UNINIT TILE FILE'}
        
    elif (scope == 'small_boundingbox'):
        settings = {'tileCoverageMode' : 'INCREMENTAL',
                  'changeQueryMethod' : 'BOUNDING_BOX',
                  'boundingBox' : 'UNINIT BOUNDING BOX'}
        
    elif (scope == 'large_tile'):
        settings = {'tileCoverageMode' : 'INCREMENTAL',
                    'changeQueryMethod' : 'FILE',
                    'tileFileHdfsPath' : 'UNINIT TILE FILE'}
        
    elif (scope == 'large_boundingbox'):
        settings = {'tileCoverageMode' : 'INCREMENTAL',
                  'changeQueryMethod' : 'BOUNDING_BOX',
                  'boundingBox' : 'UNINIT BOUNDING BOX'}
        
    else:
        assert(0)
    return settings

def getValRules(rule = 'DEFAULT', rule_list = []):
    
    rule = rule.tolower()
    
    rule_dict = {'1' : 'Rule001_UnrealisticSlopeRule',
                 '3' : 'Rule003_BuildingOverlapRule',
                 '4' : 'Rule004_EnclosedBuildingRule',
                 '5' : 'Rule005_ConvexEnclosureBuildingRule',
                 '6' : 'Rule006_SuspiciousFootprintRule',
                 '7' : 'Rule007_DisjointBuildingPolygonsRule',
                 '8' : 'Rule008_LandmarkValidationRule',
                 '9' : 'Rule009_BuildingWithoutLroidRule',
                 '10' : 'Rule010_BuildingGeometryRule'}
    
    rule_set = {}
    
    for i in rule_dict:
        rule_set[rule_dict[i]] = 'false'
    
    if (rule == 'all'):
        for key in rule_set:
            rule_set[key] = 'true'
        
    elif (rule == 'prod'):
        rule_set[rule_dict['3']] = 'true'
        rule_set[rule_dict['4']] = 'true'
        rule_set[rule_dict['5']] = 'true'
        
    elif (rule == 'custom'):
        for r in rule_list:
            rule_set[rule_dict[r]] = 'true'
    
    else:
        rule_set[rule_dict[rule]] = 'true'