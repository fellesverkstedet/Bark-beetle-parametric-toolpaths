#!/usr/bin/env python
#-*- coding: utf-8 -*-

# We will use the inkex module with the predefined Effect base class.
import inkex
# The simplestyle module provides functions for style parsing.
from simplestyle import *

class BarkMaterial(inkex.Effect):
    """
    Tag selected object with material type and thickness
    """
    def __init__(self):
        """
        Constructor.
        Defines the "--what" option of a script.
        """
        # Call the base class constructor.
        inkex.Effect.__init__(self)

        # Define string option "--what" with "-w" shortcut
        self.OptionParser.add_option('-w', '--material_type', action = 'store',
          type = 'choice', choices=['1','2','3','4'], dest = 'what', default = '1',
          help = 'Material type')

        self.OptionParser.add_option('--material_thickness', action = 'store',
          type = 'string', dest = 'what2', default = 'World',
          help = 'Material thickness')
		  
	
    def effect(self):
        # Get the path name
        for id_, node in self.selected.iteritems():
            pathname = node.get(inkex.addNS('id'))
            
            #newopvalue = "99999" #this value will later be replaced with material thickness + 0.5mm
            newopvalue = self.options.what
            newopvalue2 = self.options.what2
            splitchar = "-"
            # This the name of the operation we are inserting
            operationname = "material"
            # These are other operation names that might need to be removed
            cutout = "cutout"
            pocket = "pocket"
            drill = "drill"
            #material = "material"

            # Split the string name into a list
            pathlist = pathname.split(splitchar)

            # Check if any of the items in the list should be removed
            if cutout in pathlist:
                incompindex = pathlist.index(cutout)
                pathlist.pop(incompindex)
                pathlist.pop(incompindex)

            if pocket in pathlist:
                incompindex = pathlist.index(pocket)
                pathlist.pop(incompindex)
                pathlist.pop(incompindex)
                
            if drill in pathlist:
                incompindex = pathlist.index(drill)
                pathlist.pop(incompindex)
                pathlist.pop(incompindex)

            #if material in pathlist:
            #    incompindex = pathlist.index(material)
            #    pathlist.pop(incompindex)
            #    pathlist.pop(incompindex)
            #    pathlist.pop(incompindex)

            #check is there the list already contain the operation name
            if operationname in pathlist:
            #    search out the index of the operation name and replace the value behind
                for i in xrange(len(pathlist)):
                    if pathlist[i] == operationname:
                        pathlist[i+1] = newopvalue
                        pathlist[i+2] = newopvalue2

            #if there operation name is not already in the list, add both the name and value
            else:
                pathlist = pathlist + [operationname, newopvalue, newopvalue2]

            #join list together to match the original string
            newpathname = splitchar.join( pathlist )

            # for id_, node in self.selected.iteritems():
            node.set(inkex.addNS('id'), newpathname)

# Create effect instance and apply it.
effect = BarkMaterial()
effect.affect()
