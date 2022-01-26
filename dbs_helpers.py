import json
import uuid
import os

def add_dirty_person(name, dirtpath, filepath):
    ##
    # Adds a person to the dirt json file
    ##
    id = str(uuid.uuid4())

    #get current dirt tree
    f = open(filepath, 'r')
    #handle empty file
    if(os.stat(filepath).st_size == 0):
        data = []
    else:
        data = json.load(f)
    f.close()

    data.append({'id' : id, 'name' : name, 'dirtdir' : dirtpath})
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def populate_dirttree(filepath, treeview):
    ##
    # Populates the treeview with names and dirt directories
    ##
    
    #handle empty file
    if(os.stat(filepath).st_size == 0):
        return treeview

    #open file 
    f = open(filepath, 'r')
    data = json.load(f)
    
    for person in data:
        treeview.insert('', '1', person["id"], text = person["name"])
        treeview.insert(person["id"], '1', person["id"] + '_dir', text = person["dirtdir"])
        
    return treeview
        

        
