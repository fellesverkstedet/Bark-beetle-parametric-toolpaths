### prep

#import script types
import rhinoscriptsyntax as rs
import Rhino

#make input request for reset curves
#resetcurves = rs.GetCurveObject(message="Select your curves to reset", preselect=True, select=False)
resetcurves = rs.GetObject(message="Select your curve to reset", filter=rs.filter.curve, preselect=True, select=False)

#find out how many User text values to clear
keylist = rs.GetUserText(resetcurves, key=None , attached_to_geometry=False)
keylistlength = len(keylist)

# Set the User Text to nothing (thereby clearing it)
for x in range(0,  keylistlength):
    rskeys = rs.GetUserText(resetcurves, key=None , attached_to_geometry=False)
    rs.SetUserText(resetcurves, rskeys[0], value=None, attach_to_geometry=False)

### make Grasshopper recompute
gh = Rhino.RhinoApp.GetPlugInObject("Grasshopper")
gh.RunSolver(True)