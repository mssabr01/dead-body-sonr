import tkinter as tk
from tkinter import *
from tkinter import ttk
from dbs_helpers import *
from tkinter import filedialog

dirt_json = "./files/dirttree.json"
orgs_json = "./files/orgs.json"

# root window
root = tk.Tk()
root.geometry('500x500')
root.title('Dead Body Sonr')

def pickdir():
    dirtydir = filedialog.askdirectory()
    dir_var.set(dirtydir)


# create a notebook
notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

# create frames
dirtframe = ttk.Frame(notebook, width=500, height=500)
orgsframe = ttk.Frame(notebook, width=500, height=500)
homeframe = ttk.Frame(notebook, width=500, height=500)

dirtframe.pack(fill='both', expand=True)
orgsframe.pack(fill='both', expand=True)
homeframe.pack(fill='both', expand=True)

#Orgs Frame
org_var = tk.StringVar()
org_label = tk.Label(orgsframe, text = "Org").grid(row=0, column=0)
org_entry = tk.Entry(orgsframe, textvariable = org_var).grid(row=0, column=1)

sonr_var = tk.StringVar()
sonr_label = tk.Label(orgsframe, text = "Sonr Address").grid(row=1, column=0)
sonr_entry = tk.Entry(orgsframe, textvariable=sonr_var).grid(row=1, column=1)

orgstree = ttk.Treeview(orgsframe, column='')
orgstree.column("# 0", stretch=YES, width=400)
orgstree = populate_orgstree(filepath=orgs_json,treeview=orgstree).grid(row=3, columnspan=3)
add_btn = Button(orgsframe, 
                 text = 'Add News Org', 
                 command = lambda:add_n_refresh_orgs_tree()
                 ).grid(row=2,column=0)

def add_n_refresh_orgs_tree():
    orgstree = ttk.Treeview(orgsframe, column='c1')
    add_news_org(name=org_var.get(), sonr=sonr_var.get(), filepath=orgs_json)
    orgstree = populate_orgstree(filepath=orgs_json, 
                                 treeview=orgstree).grid(row=3,columnspan=3)

#Dirt Frame
person_var = tk.StringVar()
person_label = tk.Label(dirtframe, text = "Person").grid(row=0, column=0)
person_entry = tk.Entry(dirtframe, textvariable = person_var).grid(row=0, column=1)

dir_var = tk.StringVar()
dir_btn = Button(dirtframe, text ='Choose Directory', command = lambda:pickdir()).grid(row=1,column=0)
dir_entry = tk.Entry(dirtframe, textvariable=dir_var, state=DISABLED).grid(row=1, column=1)

dirttree = ttk.Treeview(dirtframe, column='')
dirttree.column("# 0", stretch=YES, width=400)
dirttree = populate_dirttree(filepath=dirt_json,treeview=dirttree).grid(row=3, columnspan=3)
add_btn = Button(dirtframe, 
                 text = 'Add dirty person', 
                 command = lambda:add_n_refresh_dirt_tree()
                 ).grid(row=2,column=0)

def add_n_refresh_dirt_tree():
    dirttree = ttk.Treeview(dirtframe, column='c1')
    add_dirty_person(name=person_var.get(), dirtpath=dir_var.get(), filepath=dirt_json)
    dirttree = populate_dirttree(filepath=dirt_json, 
                                 treeview=dirttree).grid(row=3,columnspan=3)

# add frames to notebook

notebook.add(homeframe, text='Dead Body Sonr')
notebook.add(orgsframe, text='News Orgs/Reporters')
notebook.add(dirtframe, text='People/Dirt')


root.mainloop()
