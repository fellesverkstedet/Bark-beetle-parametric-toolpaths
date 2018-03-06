#!/usr/bin/env python
#-*- coding: utf-8 -*-

# We will use the inkex module with the predefined Effect base class.
import inkex
# The simplestyle module provides functions for style parsing.
from simplestyle import *

class BarkDrillthrough(inkex.Effect):
    """
    Tag selected objects with a drill through operation
    """
    def __init__(self):
        """
        Constructor.
        Defines the "--what" option of a script.
        """
        # Call the base class constructor.
        inkex.Effect.__init__(self)

        # Define string option "--what" with "-w" shortcut
        #self.OptionParser.add_option('-w', '--pocket_depth', action = 'store',
        #  type = 'string', dest = 'what', default = 'World',
        #  help = 'Pocket depth')
		  
	
    def effect(self):
        # Get the path name
        for id_, node in self.selected.iteritems():
            pathname = node.get(inkex.addNS('id'))
            
            newopvalue = "99999" #this value will later be replaced with material thickness + 0.5mm
            #newopvalue = self.options.what
            splitchar = "-"
            # This the name of the operation we are inserting
            operationname = "drill"
            # These are other operation names that might need to be removed
            cutout = "cutout"
            pocket = "pocket"
            #drill = "drill"
            material = "material"

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
                
            #if drill in pathlist:
            #    incompindex = pathlist.index(drill)
            #    pathlist.pop(incompindex)
            #    pathlist.pop(incompindex)

            if material in pathlist:
                incompindex = pathlist.index(material)
                pathlist.pop(incompindex)
                pathlist.pop(incompindex)
                pathlist.pop(incompindex)

            #check is there the list already contain the operation name
            if operationname in pathlist:
            #    search out the index of the operation name and replace the value behind
                for i in xrange(len(pathlist)):
                    if pathlist[i] == operationname:
                        pathlist[i+1] = newopvalue

            #if there operation name is not already in the list, add both the name and value
            else:
                pathlist = pathlist + [operationname, newopvalue]

            #join list together to match the original string
            newpathname = splitchar.join( pathlist )

            # for id_, node in self.selected.iteritems():
            node.set(inkex.addNS('id'), newpathname)

# Create effect instance and apply it.
effect = BarkDrillthrough()
effect.affect()
