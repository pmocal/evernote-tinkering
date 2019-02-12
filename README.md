UPDATE 2/12/19:
- API key must be removed ASAP
- Currently broken
  - > MacBook-Air-4:evernote-tinkering parthivmohan$ python commandlinenotes.py
    Traceback (most recent call last):
    File "commandlinenotes.py", line 4, in <module>
    import evernote.edam.userstore.constants as UserStoreConstants
    ImportError: No module named evernote.edam.userstore.constants




Using the Evernote API for Python I wrote a script that allows the user to create notebooks and notes in their Evernote account from the command line.

I added a "Daily Journal" feature as well; it streamlines the process of keeping a daily journal through Evernote by automating intermediate steps for the user.
