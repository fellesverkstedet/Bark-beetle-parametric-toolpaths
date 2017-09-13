#this script creates an interface for selecting material outline curve, define the material type and the material thickness


### prep

#import script types
import rhinoscriptsyntax as rs
import Rhino

#define User Key (so that the GH definition will know that this curve object is representing the material outline)
matkey = "CNCmaterial"

#define list of material options as strings
foam_wax = "Foam_Wax"
soft_wood = "SoftWood"
hard_wood = "HardWood"
plastic = "Plastic"
aluminium_brass = "Aluminium_Brass"
bronze = "Bronze"
soft_steel = "SoftSteel"
stainless_steel = "StainlessSteel"
printed = "3DprintedPlasticStock"

#format strings into a list
matoptions = [foam_wax,soft_wood,hard_wood,plastic,aluminium_brass,bronze,soft_steel,stainless_steel,printed]


### inputs

#make input request for material outline curve
materialcurve = rs.GetObject(message="Select your material outline curve", filter=rs.filter.curve, preselect=True, select=False)
#if(materialcurve==None):return ..not working

#make command line input for material type with options
materialtype = rs.GetString(message="Choose your material type", defaultString=None, strings=matoptions)

#make command line input for material thickness
materialthickness = rs.GetReal(message="What is the thickness of your material in mm?", number=None, minimum=0.01, maximum=120)


### clear old values

#find out how many old User text values to clear
keylist = rs.GetUserText(materialcurve, key=None , attached_to_geometry=False)
keylistlength = len(keylist)

# Set the User Text to nothing (thereby clearing old values)
for x in range(0,  keylistlength):
    rskeys = rs.GetUserText(materialcurve, key=None , attached_to_geometry=False)
    rs.SetUserText(materialcurve, rskeys[0], value=None, attach_to_geometry=False)


### set User Text values with the inputs given

# format our User Key value

matvalue = [materialtype,materialthickness]

# Set the User Text
rs.SetUserText(materialcurve, matkey, value=matvalue, attach_to_geometry=False)


### make Grasshopper recompute
gh = Rhino.RhinoApp.GetPlugInObject("Grasshopper")
gh.RunSolver(True)