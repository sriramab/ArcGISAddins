## Aggregate Zones

This tool is to be used for aggregating zones by manual choice. From the 
selected features, the plugin will add an incremented ID. 

### Installation

- Double click the `.esriaddin` file
- Open ArcGIS and right click anyhwere in the empty toolbar space
- Select Renumbering Toolbar
- A toolbar with a button `Assign newID` is now available

### Use

- Bring the shapefile to the top of your TOC.
- Add a field `NewID` to your shapefile.
- Edit mode is not required.
- Label the features on `NewID`
- Select one or more features (but not all), and click the tool.
- If you have labelled the layer (step 4), you will notice the changes.

### Errors

- No `NewID` field in your shapefile will result in an error.
- Not selecting any feature, the tool does nothing.
- Selecting all features, the tool does nothing.