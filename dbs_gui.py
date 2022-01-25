import tkinter as tk
from tkinter import *
from tkinter import ttk
from dbs_helpers import *

# root window
root = tk.Tk()
root.geometry('500x500')
root.title('Notebook Demo')

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

#Dirt Frame
add_person_b = Button(dirtframe, text='Add Person')
add_person_b.pack(side=LEFT)
dirttree = ttk.Treeview(dirtframe)
dirttree = populate_dirttree(filepath="./files/dirttree.json",treeview=dirttree)
dirttree.pack()


# add frames to notebook

notebook.add(homeframe, text='Dead Body Sonr')
notebook.add(orgsframe, text='News Orgs/Reporters')
notebook.add(dirtframe, text='People/Dirt')


root.mainloop()
