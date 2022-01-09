#! /usr/bin/python3.8

#######################################################################
# This is an automation script towards creating new project folders
# organizing them and having some extra functionality over them
#######################################################################

import os 
import sys
import shutil
from datetime import date
import timeit

def create(dir):

    os.system("mkdir " + dir)

    os.system("cd" + dir)

    os.system("mkdir /public")
    os.system("touch /README.txt")
    os.system("mkdir /notes")
    os.system("touch /notes/notes.txt")
    os.system("touch /notes/resources.txt")


def remove():
    shutil.rmtree(dir, ignore_errors=True)


def info():
    os.system("touch /info.txt")

    name = input("What's your name: ")
    project = input("Name of project: ")
    createdFor = input("What is the purpose of this project: ")
    when = date.today()

    text = "This folder was created by: " + str(name) + "\n" + "Date created: " + str(when) + "Name of project: " + str(project) + "\n" + "Purpose of project: " + str(createdFor)
    os.system("echo -e" + text + ">> info.txt")
    print("Info file created!")

def showInfo(dir):
    os.system("cd" + dir)
    os.system("cat info.txt")
    #Can add a last change info line

start = timeit.default_timer()

function = sys.argv[1]
nameOfProject = sys.argv[2]
listOfFunctions = ["create","info","remove"]

#Fail safe mechanisms
if function not in listOfFunctions:
    print("Please enter a proper function" + listOfFunctions)

if len(sys.argv) < 2:
    print("Not enough arguments inserted!")
    function = input("Please enter a proper function" + listOfFunctions + ": ")
    nameOfProject = input("Please enter project name: ")

#Executing commands
if function == "create":
    create(nameOfProject)

    prompt = input("Would you like to create an info file? (y/n) ")
    if prompt == "y":
        info()
    else:
        print("ok")

if function == "info":
    info(nameOfProject)

if function == "remove":
    remove(nameOfProject)


stop = timeit.default_timer()

print('Time: ', round(stop - start,3)) 