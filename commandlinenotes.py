import hashlib
import binascii

import evernote.edam.userstore.constants as UserStoreConstants
import evernote.edam.type.ttypes as Types

from evernote.api.client import EvernoteClient
import datetime

auth_token = "S=s1:U=8ea11:E=14d84b05591:C=1462cff2998:P=1cd:A=en-devtoken:V=2:H=693f535266f3161f98266da76170487f"
client = EvernoteClient(token=auth_token, sandbox=True)
noteStore = client.get_note_store()
    
prompt = input('\nWelcome to EVERNOTE!\nRemember to encase all command line input in quotes since it must be a string.\nWhat would you like to do? Type "1" to add a note to an existing notebook, "2" to create a notebook, or "3" to make a daily journal entry.')
if prompt == '1':
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
elif prompt == '2':
    notebook = Types.Notebook()
    notebook.name = input('Choose a title  (encased in quotations since it is a string): ')
    notebook = noteStore.createNotebook(notebook)
elif prompt == '3':
    now = datetime.datetime.now()
    dailyGuid = None
    for notebook in noteStore.listNotebooks(auth_token):
        if ('daily' in notebook.name.lower()) and ('journal' in notebook.name.lower()):
            dailyGuid = notebook.guid
    if dailyGuid is None:
        notebook = Types.Notebook()
        notebook.name = 'Daily Journal'
        notebook = noteStore.createNotebook(notebook)
        for notebook in noteStore.listNotebooks(auth_token):
            if notebook.name is 'Daily Journal':
                dailyGuid = notebook.guid
    note = Types.Note()
    note.notebookGuid = dailyGuid
    note.title = '{0}/{1}/{2} {3}:{4}:{5}'.format(now.month, now.day, now.year, now.hour, now.minute, now.second)
    #now.strftime("%Y-%m-%d %H:%M")
    note.content = '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE en-note SYSTEM "http://xml.evernote.com/pub/enml2.dtd">'
    note.content += '<en-note>'
    note.content += input('Type the body of your note (encased in quotations since it is a string): ')
    note.content += '</en-note>'
    note = noteStore.createNote(note)
print 'Your additions have been made!\nRun this script again to make further changes.\nGoodbye!'


#import subprocess
#print "start"
#subprocess.call("sleep.sh", shell=True)
#print "end"




