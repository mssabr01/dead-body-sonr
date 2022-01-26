import json
import uuid
import os

def fire_the_dirt_cannon():
    #zip up each directory for each user

    #send each zip to each .snr address in orgs file

def add_wallet(address, filepath):
    f = open(filepath, 'a')
    f.write('\n' + address)
    f.close()

def populate_wallet_list(filepath):
    f = open(filepath, 'r')
    msg = "My Wallets:"
    wallets = f.read().split()
    for w in wallets:
        msg = msg + '\n' + w
    return msg

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

def add_news_org(name, sonr, filepath):
    ##
    # Adds a person to the dirt json file
    ##
    id = str(uuid.uuid4())

    #get current org tree
    f = open(filepath, 'r')
    #handle empty file
    if(os.stat(filepath).st_size == 0):
        data = []
    else:
        data = json.load(f)
    f.close()

    data.append({'id' : id, 'name' : name, '.sonr' : sonr})
    
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
        
def populate_orgstree(filepath, treeview):
    ##
    # Populates the treeview with names and dirt directories
    ##
    
    #handle empty file
    if(os.stat(filepath).st_size == 0):
        return treeview

    #open file 
    f = open(filepath, 'r')
    data = json.load(f)
    
    for org in data:
        treeview.insert('', '1', org["id"], text = org["name"])
        treeview.insert(org["id"], '1', org["id"] + '_dir', text = org[".sonr"])
        
    return treeview

        
