import c4d
from c4d import gui

PLUGIN_ID = 1059782
PLUGIN_NAME = "Render Calculator"

GROUP = 10000
solo_check = 10001
view_check = 10002
render_check = 10003
manager_check = 10004
locked_check =  10005
generators_check = 10006 
expression_check = 10007
animation_check = 10008
color_vector = 10009
xref_check =  10010

OK = 20001

def GetSelLayer(layer):
    selectedlayer =[]
    if layer.GetBit(c4d.BIT_ACTIVE) :
        selectedlayer.append(layer)


def ToggleLayer(sel, data):
    
    for i in sel:
        
        i.SetLayerData(data)

    c4d.EventAdd()

class OptionsDialog(gui.GeDialog):
    def CreateLayout(self):

        self.SetTitle(PLUGIN_NAME)

        #CheckBox
        self.GroupBegin(GROUP, c4d.BFH_SCALEFIT, 10, 1, inith = 0)
        
        self.GroupEnd()

        #Apply
        self.GroupBegin(GROUP, c4d.BFH_SCALEFIT, 2, 1, inith = 0)
        self.GroupEnd()

    def Command(self, id, msg):
        if id == OK :
            #Get Selected Layer
            root = doc.GetLayerObjectRoot().GetDown()
            
            sellayer = GetSelLayer(root)

            data = {
                "solo" : self.GetLong(solo_check),
                "view" : self.GetLong(view_check),
                "render" : self.GetLong(render_check),
                "manager" : self.GetLong(manager_check),
                "locked" : self.GetLong(locked_check),
                "generators" :self.GetLong(generators_check),
                "expression" : self.GetLong(expression_check),
                "animation" :self.GetLong(animation_check),
                "color" : self.GetLong(color_vector),
                "xref" : self.GetLong(xref_check),
            }
            ToggleLayer(sellayer, data)


class RenderCalculator(c4d.plugins.CommandData):

    def Execute(self, doc):
        
        
        self.dlg = OptionsDialog()
        return self.dlg.Open(c4d.DLG_TYPE_ASYNC, defaultw = 250, defaulth = 350)

if __name__=='__main__':

    dir, file = os.path.split(__file__)
    icon = c4d.bitmaps.BaseBitmap()
    icon.InitWith(os.path.join(dir, "res", "Icon.tif"))
    
    c4d.plugins.RegisterCommandPlugin(  id = PLUGIN_ID, 
                                        str = PLUGIN_NAME, 
                                        dat = RenderCalculator(),
                                        help="Calculator",
                                        info=0,
                                        icon=icon)