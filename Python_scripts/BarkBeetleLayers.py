import scriptcontext as sc
import Rhino
import rhinoscriptsyntax as rs

layer = Rhino.DocObjects.Layer()
sc.doc.Views.RedrawEnabled = False

def AddCNCLayers():
    
    
    
    LayerNames = ["Work layer", "CNC drill", "CNC pocket", "CNC engrave" , "CNC cut", "CNC 3D", "CNC tabs"]
    LayerColors = [(221,221,221), (255,191,0), (253,0,255), (255,125,218), (0,163,184), (100,113,113), (191,191,255)]
    Count = 0
    for x in LayerNames:
        layer.Name = x
        sc.doc.Layers.Add(layer)
        sc.doc.Layers.Add
        
        rs.LayerColor(x, LayerColors[Count])
        Count += 1

AddCNCLayers()
sc.doc.Views.RedrawEnabled = True