import arcpy
import pythonaddins

class ButtonClass13(object):
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

        def insert_max_value():

            my_list_1 = arcpy.da.TableToNumPyArray(the_only_layer, 'NewID')
            max_value_selection = max(my_list_1['NewID'])
           # print "NewID = " + str(max_value_selection + 1 )

            arcpy.SelectLayerByAttribute_management(the_only_layer, "SWITCH_SELECTION")
            my_list_2 = arcpy.da.TableToNumPyArray(the_only_layer, 'NewID')
            if len(my_list_2) == 0:
                pythonaddins.MessageBox("All Features selected. Use Field "
                                        "Calculator instead",
                                        "Error")
                raise Exception("All features selected, Use Field Calculator "
                                "instead")

                exit()
            else:
                max_value_selection_inverse = max(my_list_2['NewID'])
            #print "NewID = " + str(max_value_selection_inverse + 1)

            arcpy.SelectLayerByAttribute_management(the_only_layer,
                                                    "SWITCH_SELECTION")
            return max(max_value_selection,max_value_selection_inverse) + 1

        def update_value():
            new_value = insert_max_value()
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

class ButtonClass7(object):
    """Implementation for Aggregate_addin.button_1 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        current_mxd = arcpy.mapping.MapDocument("CURRENT")
        the_only_layer = arcpy.mapping.ListLayers(current_mxd)[0]
        arcpy.Dissolve_management(the_only_layer, "DissolvedLayer" ,"NewID","","MULTI_PART","")