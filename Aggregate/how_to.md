## Aggregate Zones
#### __version__ 0.1

This tool is to be used for aggregating zones by manual selection. From the selected features, the plugin will assign an incremented ID to the selected features.


> Mandatory: Your shapefile must contain a field named `NewID` . You must follow use of this tool with the *Dissolve* tool available in ArcGIS toolbox. Dissolve tool will be added to this toolbar later.

### Installation

- Double click the `.esriaddin` file and follow the instructions.
- Open ArcGIS and right click anyhwere in the empty toolbar space and select `Renumbering Toolbar`
- A toolbar with a button `Assign newID` is now available.

##### Activate the toolbar...
![Activate Toolbar](https://github.com/sriramab/ArcGISAddins/images/renumbering.png)

##### After activating the toolbar...
![Button](https://github.com/sriramab/ArcGISAddins/images/tool_renumbering.png)

### Use

- Bring the shapefile to the top of your TOC.
- Add a field `NewID` to your shapefile if it does not exist already.
- Edit mode is not required.
- Label the features on `NewID`.
- Select one or more features (but not all), and click the tool.
- If you have labelled the layer (step 4), you will notice the changes.

### Errors

- No `NewID` field in your shapefile will result in an error.
- Not selecting any feature, the tool does nothing, (logs error invisible to the user).
- Selecting all features, the tool does nothing, (logs error invisible to the user).

