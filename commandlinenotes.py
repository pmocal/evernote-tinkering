import hashlib
import binascii
import evernote.edam.userstore.constants as UserStoreConstants
import evernote.edam.type.ttypes as Types

from evernote.api.client import EvernoteClient
auth_token = "S=s1:U=8ea11:E=14d84b05591:C=1462cff2998:P=1cd:A=en-devtoken:V=2:H=693f535266f3161f98266da76170487f"
client = EvernoteClient(token=auth_token, sandbox=True)

prompt = input('What would you like to do? Type "a" to add a note to an existing notebook or "c" to create a notebook. ')
if prompt == 'a':
    noteStore = client.get_note_store()
    print "The existing notebooks are as follows:"
    for notebook in noteStore.listNotebooks(auth_token):
        print "Name: " + notebook.name + "; GUID: " + notebook.guid
    note = Types.Note()
    note.notebookGuid = input('Choose a notebook (type the GUID encased in quotations since it is a string): ')
    note.title = input('Choose a title (encased in quotations since it is a string): ')
    note.content = '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE en-note SYSTEM "http://xml.evernote.com/pub/enml2.dtd">'
    note.content += '<en-note>'
    note.content += input('Type the body of your note (encased in quotations since it is a string): ')
    note.content += '</en-note>'
    note = noteStore.createNote(note)
elif prompt == 'c':
    noteStore = client.get_note_store()
    notebook = Types.Notebook()
    notebook.name = input('Choose a title  (encased in quotations since it is a string): ')
    notebook = noteStore.createNotebook(notebook)



#import subprocess
#print "start"
#subprocess.call("sleep.sh", shell=True)
#print "end"




