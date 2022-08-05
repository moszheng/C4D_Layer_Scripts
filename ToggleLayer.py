import c4d
from c4d import gui

def CloseSelectLayer(sel):
    
    for i in sel:
        
        i.SetLayerData()

    c4d.EventAdd()

def main():

    sel = 
    CloseSelectLayer(sel)

if __name__=='__main__':
    main()