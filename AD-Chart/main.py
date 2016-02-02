"""LdapDir

Usage:
    LdapDir.py --goog
    LdapDir.py --json
    LdapDir.py (-h|--help)

Options:
    -h --help   Show this screen.
    --goog      Use the Google Charts API output format
    --json      Use the JSON output format

"""

from docopt import docopt
from writer import *
from ldapConn import ldap_search

arguments = ""
if __name__ == '__main__':
    arguments = docopt(__doc__, version='LdapDir')


# Get AD credentials from file creds.dat
tmpFile = open('creds.dat', 'r')
username, password = eval(tmpFile.readline())
tmpFile.close()

# Set AD connection details and specify get all users that are not disabled
link = 'ldap://cpt-dc-01'
base = 'dc=visionoss,dc=int'
query = '(&(objectCategory=person)(objectclass=user)(!(UserAccountControl:1.2.840.113556.1.4.803:=2)))'

# Set root node (CEO)
root = "Mike Frayne"

# Execute the ldap query and format data
if arguments['--json']:
    Formatted = ldap_search(link, base, query, username, password, 1)
else:
    Formatted = ldap_search(link, base, query, username, password, 0)

# Create tree from user data
for k in Formatted.keys():
    userObj = Formatted[k]
    currentUserManager = Formatted[k].getMan()
    managerObj = ''
    if currentUserManager != '':
        managerObj = Formatted[currentUserManager]
        if arguments['--json']:
            managerObj.addChild(userObj.__dict__)
            userObj.__dict__.pop("parent", None)
            userObj.__dict__.pop("manager", None)
        else:
            managerObj.addChild(userObj)

# Run script to create either json object or generate google chart api html page
if arguments['--json']:
    Formatted[root].__dict__.pop("parent", None)
    Formatted[root].__dict__.pop("manager", None)
    json_create(Formatted, "Mike Frayne")
else:
    hugo_create(Formatted, "Mike Frayne")
