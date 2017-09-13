#this script asks the user to select pocket curves (pockets remove all material inside a boundary)

#import script types
import rhinoscriptsyntax as rs
import Rhino

#define User Key (so that the GH definition will know that this curve object is representing the material outline)
userkey = "CNCpocket"

#make input request for cutout curves
pocketcurves = rs.GetObject(message="Select a pocket curve (pockets remove all material inside a boundary)", filter=rs.filter.curve, preselect=True, select=False)

#make command line input for material thickness
pocketdepth = rs.GetReal(message="What is the pocket depth in mm?", number=None, minimum=None, maximum=120)

#find out how many old User text values to clear
keylist = rs.GetUserText(pocketcurves, key=None , attached_to_geometry=False)
keylistlength = len(keylist)

# Set the User Text to nothing (thereby clearing old values)
for x in range(0,  keylistlength):
    rskeys = rs.GetUserText(pocketcurves, key=None , attached_to_geometry=False)
    rs.SetUserText(pocketcurves, rskeys[0], value=None, attach_to_geometry=False)
    
# Set the new User Text
rs.SetUserText(pocketcurves, userkey, pocketdepth, attach_to_geometry=False)

# make Grasshopper recompute
gh = Rhino.RhinoApp.GetPlugInObject("Grasshopper")
gh.RunSolver(True)