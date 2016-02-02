#from hugo import hugo_create
#from Formatter import formatter
import ldap
from Formatter import jsonFormatter
import json
import os


root = "Mike Frayne"
Formatted = {}
tree = []

tmpFile = open('creds.dat', 'r')
username, password = eval(tmpFile.readline())
tmpFile.close()

link = 'ldap://cpt-dc-01'
base = 'dc=visionoss,dc=int'
query = '(&(objectCategory=person)(objectclass=user)(!(UserAccountControl:1.2.840.113556.1.4.803:=2)))'


def ldap_search(ldap_uri, base, query, user, passwd):

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
                    jsonFormatter(result_data, Formatted)

        if len(Formatted) == 0:
            print('No results found.')
            return

        return Formatted

    except ldap.LDAPError, e:
        print('LDAPError: %s.' % e)

    finally:
        l.unbind_s()

ldap_search(link, base, query, username, password)

for k in Formatted.keys():
    userObj = Formatted[k]
    currentUserManager = Formatted[k].getMan()
    managerObj = ''
    if currentUserManager != '':
        managerObj = Formatted[currentUserManager]
        #userObj.setParent(managerObj.__dict__)
        managerObj.addChild(userObj.__dict__)
        userObj.__dict__.pop("parent", None)
        userObj.__dict__.pop("manager", None)
Formatted[root].__dict__.pop("parent", None)
Formatted[root].__dict__.pop("manager", None)

dictVer = {}

count = 0

tmpFile = open(os.path.join('res/json/', 'voss.json'), "w")
tmpFile.write(json.dumps(Formatted[root].__dict__, indent=4, separators=(',', ': ')))
tmpFile.close()


#hugo_create(Formatted, "Mike Frayne")
#json_create(Formatted, "Mike Frayne")