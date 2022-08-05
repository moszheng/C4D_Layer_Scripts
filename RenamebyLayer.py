from ast import Continue
import c4d
from c4d import gui

# Main function

def ObjRenamebyLayer(sel):
    
    doc.StartUndo()
    
    for i in sel:
        doc.AddUndo(c4d.UNDOTYPE_CHANGE, i)

        objname = i.GetName()
        layer = i.GetLayerObject(doc)
        
        if layer == None:
            continue

        if 1 : #prefix_
            i.SetName(objname + "_" + layer.GetName())

        else :
            i.SetName(layer.GetName())

    doc.EndUndo()
    c4d.EventAdd()

def main():

    sel = doc.GetSelection()
    ObjRenamebyLayer(sel)

if __name__=='__main__':
    main()