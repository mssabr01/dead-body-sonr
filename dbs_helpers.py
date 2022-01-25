import json

def populate_dirttree(filepath, treeview):
    ##
    # Populates the treeview with names and dirt directories
    ##
    
    #open file 
    f = open(filepath)
    data = json.load(f)

    i = 0
    for person in data:
        treeview.insert('', '1', person["id"], text = person["name"])
        treeview.insert(person["id"], '1', person["id"] + '_dir', text = person["dirtdir"])
        
    return treeview
        

        
