from ast import Continue
import c4d
from c4d import gui

# Main function

def ObjRenamebyLayer(sel):
    
    doc.StartUndo()
    
    for i in bc:
        doc.AddUndo(c4d.UNDOTYPE_CHANGE, i)

        layer = i.GetLayerObject(doc)
        
        if layer == None:
            continue

        
        i.SetName(layer.GetName())

    doc.EndUndo()
    c4d.EventAdd()

def main():

    sel = doc.GetSelection()
    ObjRenamebyLayer(sel)

if __name__=='__main__':
    main()