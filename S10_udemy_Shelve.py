# Shelves are read / write by default
import shelve # writes dictionary to file

#creates motorcycle.db shelve file
with shelve.open('motorcycles') as motorcycle:
    motorcycle['ducati'] = "A beautiful italian motorcycle"
    motorcycle['honda'] = "A beautiful japanese motorcycle"
    motorcycle['harley'] = "A beautiful american motorcycle"
    print(motorcycle['ducati'])
    # NO SHELVE ZERO LIKE IN DICTIONARY

