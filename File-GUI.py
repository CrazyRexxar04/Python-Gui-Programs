__author__ = 'CrazyRexxar04'

import Tkinter
from Tkinter import *
import os
from os import *

# Screen set-up --------------------------------------------------------------------------------------------------------

root = Tkinter.Tk()

topFrame = Frame(root)
topFrame.pack(side=TOP)

subtitleFrame = Frame(root)
subtitleFrame.pack()

choiceFrame = Frame(root)
choiceFrame.pack()

bottomFrame = Frame(root)
bottomFrame.pack()

entryFrame = Frame(root)
entryFrame.pack()

# Second screen setup --------------------------------------------------------------------------------------------------

# Functions ------------------------------------------------------------------------------------------------------------

def chosen():
    method = selected.get()
    directory = entry.get()

    if str(method) == "Make":
        make(directory)
    elif str(method) == "Remove":
        remove(directory)
    else:
        print("Unidentified")

def make(directory):
    os.mkdir(str(directory))

def remove(directory):
    os.rmdir(str(directory))

def pack():
    title.pack()
    subtitle.pack(side=LEFT)
    choiceBox.pack(side=LEFT)
    choiceBTN.pack(side=RIGHT, padx=5)
    choice_1.pack(side=LEFT)
    choice_2.pack(side=LEFT)
    guide1.pack()
    entry.pack()
    guide2.pack()


def run():
    pack()
    root.mainloop()

# Widget assigning -----------------------------------------------------------------------------------------------------

title = Label(topFrame, text="File Management")
subtitle = Label(subtitleFrame, text="Helping you create and delete directories, anywhere, any time, any place.")

choiceBox = Label(choiceFrame, text="""
Choose your option:
""")

selected = StringVar()

choice_1 = Radiobutton(bottomFrame, text="Make a file", variable=selected, value="Make")
choice_2 = Radiobutton(bottomFrame, text="Remove a file", variable=selected, value="Remove")

choiceBTN = Button(bottomFrame, text="Choose", command=chosen)

guide1 = Label(text="Enter the path")
entry = Entry(entryFrame)

guide2 = Label(text="Enter the name of the directory")


# second widgets -------------------------------------------------------------------------------------------------------



# Commands -------------------------------------------------------------------------------------------------------------

run()
