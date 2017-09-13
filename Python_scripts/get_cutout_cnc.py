#this script asks the user to select the curves that will cut all the way through the material (outlines of a part)

#import script types
import rhinoscriptsyntax as rs
import Rhino

#define User Key (so that the GH definition will know that this curve object is representing the material outline)
cutoutkey = "CNCcutout"

#make input request for cutout curves
cutoutcurves = rs.GetObject(message="Select a curve for cutout (an outline of a part)", filter=rs.filter.curve, preselect=True, select=False)

# Clear any previous User Text
#find out how many User text values to clear
keylist = rs.GetUserText(cutoutcurves, key=None , attached_to_geometry=False)
keylistlength = len(keylist)

# Set the User Text to nothing (thereby clearing it)
for x in range(0,  keylistlength):
    rskeys = rs.GetUserText(cutoutcurves, key=None , attached_to_geometry=False)
    rs.SetUserText(cutoutcurves, rskeys[0], value=None, attach_to_geometry=False)
    
# Set the new User Text
rs.SetUserText(cutoutcurves, cutoutkey, value="yes", attach_to_geometry=False)

# make Grasshopper recompute
gh = Rhino.RhinoApp.GetPlugInObject("Grasshopper")
gh.RunSolver(True)