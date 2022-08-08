import c4d
from c4d import gui

PLUGIN_ID = 1059782
PLUGIN_NAME = "Toggle Layer"

GROUP = 10000

color_vector = 10009

solo_check = 10001
view_check = 10002
render_check = 10003
manager_check = 10004
locked_check =  10005

animation_check = 10008
generators_check = 10006 
expression_check = 10007
xref_check =  10010

BTN_Apply = 20001

def GetSelLayer(layer):

    selectedlayer = []

    if layer.GetBit(c4d.BIT_ACTIVE) :
        selectedlayer.append(layer)
    
    return selectedlayer

def ToggleLayer(sel, data):
    
    for i in sel:
        
        i.SetLayerData(data)

    c4d.EventAdd()

class OptionsDialog(gui.GeDialog):

    def CreateLayout(self):

        self.SetTitle(PLUGIN_NAME)

        #CheckBox
        self.GroupBegin(GROUP, c4d.BFH_SCALEFIT, 8, 1, inith = 0)
        # self.AddColorField(color_vector)
        self.AddCheckbox(solo_check)
        self.AddCheckbox(view_check)
        self.AddCheckbox(render_check)
        self.AddCheckbox(manager_check)
        self.AddCheckbox(animation_check)
        self.AddCheckbox(generators_check)
        self.AddCheckbox(expression_check)
        self.AddCheckbox(xref_check)
        
        self.GroupEnd()

        #Apply
        self.GroupBegin(GROUP, c4d.BFH_SCALEFIT, 1, 1, inith = 0)

        self.AddButton(BTN_Apply, c4d.BFH_SCALE, name='Refresh', inith=15)

        self.GroupEnd()

    def Command(self, id, msg):

        if id == BTN_Apply :
            #Get Selected Layer
            root = doc.GetLayerObjectRoot().GetDown()
            
            sellayer = GetSelLayer(root)

            data = {
                "solo" : self.GetLong(solo_check),
                "view" : self.GetLong(view_check),
                "render" : self.GetLong(render_check),
                "manager" : self.GetLong(manager_check),
                "locked" : self.GetLong(locked_check),

                "animation" :self.GetLong(animation_check),
                "generators" :self.GetLong(generators_check),
                "expression" : self.GetLong(expression_check),
                
                # "color" : self.GetLong(color_vector),
                "xref" : self.GetLong(xref_check),
            }

            ToggleLayer(sellayer, data)


class LayerToggle(c4d.plugins.CommandData):

    def Execute(self, doc):
        
        
        self.dlg = OptionsDialog()
        return self.dlg.Open(c4d.DLG_TYPE_ASYNC, defaultw = 250, defaulth = 350)

if __name__=='__main__':

    dir, file = os.path.split(__file__)
    icon = c4d.bitmaps.BaseBitmap()
    icon.InitWith(os.path.join(dir, "res", "Icon.tif"))
    
    c4d.plugins.RegisterCommandPlugin(  id = PLUGIN_ID, 
                                        str = PLUGIN_NAME, 
                                        dat = LayerToggle(),
                                        help="Calculator",
                                        info=0,
                                        icon=icon)