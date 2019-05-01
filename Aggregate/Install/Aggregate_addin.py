import arcpy
import pythonaddins
import numpy as np

class Button_assignID(object):
    """Implementation for Aggregate_addin.button (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        current_mxd = arcpy.mapping.MapDocument("CURRENT")
        the_only_layer = arcpy.mapping.ListLayers(current_mxd)[0]

        # DETECT IF ANY FEATURE IS SELECTED, ELSE EXIT

        if (the_only_layer.getSelectionSet()) == None:
            pythonaddins.MessageBox("No Features selected", "Error")
            exit()

        # DETECT MAX VALUE IN THAT FIELD AND ADD ONE HIGHER

        def get_max_value():

            max_value = np.amax(arcpy.da.TableToNumPyArray(
                the_only_layer.dataSource, "NewID").astype(np.int))
            return max_value + 1

        def update_value():
            new_value = get_max_value()
            with arcpy.da.UpdateCursor(arcpy.mapping.ListLayers(current_mxd)[0],
                                       ['NewID']) as AttributeTable:
                for x in AttributeTable:
                    x[0] = new_value
                    AttributeTable.updateRow(x)

        # CHECK IF A FIELD EXISTS IN THE ATTRIBUTE TABLE, IT HAS TO BE NAMED 'NewID'
        if len(arcpy.ListFields(the_only_layer, 'NewID')) > 0:

            update_value()
            print "Modified  " + str(the_only_layer)
        else:
            print("NewID does not exist")
            pythonaddins.MessageBox("NewID is missing in your attribute table",
                                    "Field not found")

class Button_dissolve(object):
    """Implementation for Aggregate_addin.button_1 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        current_mxd = arcpy.mapping.MapDocument("CURRENT")
        the_only_layer = arcpy.mapping.ListLayers(current_mxd)[0]
        arcpy.Dissolve_management(the_only_layer, "DissolvedLayer", "NewID", "",
                                  "MULTI_PART", "")