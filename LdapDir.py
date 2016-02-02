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
import ldap
from docopt import docopt

from Formatter import *
from writer import *

arguments = ""
if __name__ == '__main__':
    arguments = docopt(__doc__, version='LdapDir')


def ldap_search(ldap_uri, base, query, user, passwd, root):
    try:
        l = ldap.initialize(ldap_uri)
        l.set_option(ldap.OPT_REFERRALS, 0)
        l.simple_bind_s(user, passwd)
        l.protocol_version = ldap.VERSION3
        search_scope = ldap.SCOPE_SUBTREE
        retrieve_attributes = None

        ldap_result_id = l.search(
            base,
            search_scope,
            query,
            retrieve_attributes
        )
        while 1:
            result_type, result_data = l.result(ldap_result_id, 0)
            if result_data == []:
                break
            else:
                if result_type == ldap.RES_SEARCH_ENTRY:
                    if arguments['--json']:
                        jsonFormatter(result_data, Formatted)
                    else:
                        formatter(result_data, Formatted)

        if len(Formatted) == 0:
            print('No results found.')
            return

        return Formatted

    except ldap.LDAPError, e:
        print('LDAPError: %s.' % e)

    finally:
        l.unbind_s()


tmpFile = open('creds.dat', 'r')
username, password = eval(tmpFile.readline())
tmpFile.close()

link = 'ldap://cpt-dc-01'
base = 'dc=visionoss,dc=int'
query = '(&(objectCategory=person)(objectclass=user)(!(UserAccountControl:1.2.840.113556.1.4.803:=2)))'

root = "Mike Frayne"
Formatted = {}
tree = []

ldap_search(link, base, query, username, password, root)

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

if arguments['--json']:
    Formatted[root].__dict__.pop("parent", None)
    Formatted[root].__dict__.pop("manager", None)
    json_create(Formatted, "Mike Frayne")
else:
    hugo_create(Formatted, "Mike Frayne")
