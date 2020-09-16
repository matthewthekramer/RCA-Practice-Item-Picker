# RCA-Practice-Item-Picker

A simple script to create practice data to study for the RCA exam

To run:
```
python3 rca_handson_item_picker.py
```
This should produce output similar to:
```

======== Search Terms ========
Any word that starts with 'm' and ends with 'ed'
grammatical variations of the word send
Begins with Un and can differ from United by 3 characters and all grammatical variations
$78
grammatical variations of the word apply

======== Permissions ========
Override production restrictions or remove conflicts
Monitor all users that are currently logged in
View Workspace
Run existing structured analytics set
Run a Sum/Tally/Average report and export it to the desktop
```

To add search terms or permissions, edit `permissions.txt` or `searchTerms.txt` and add your new permissions or search terms on a new line anywhere in the file. Lines starting with `#` are ignored.
