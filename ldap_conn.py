import ldap
from jsonCreator import jsonCreator
from userNode import userNode
import json

Formatted = {}
tree = []

tmpFile = open('creds.dat', 'r')
username, password = eval(tmpFile.readline())
tmpFile.close()

BlackListTerm = ['Administrator', "Admin", "Guest", "Voss", "VOSS", "Machine", "move", "IT", "Support", "Test",
                 "Lab", "Temp", "Kiosk"]
LdapFilter = ['objectSid', 'objectGUID', 'photo']
Exclusion_list = ["owen.bridle@visionoss.int", "mario.vanriesen@visionoss.int", "jenkins@visionoss.int"]

link = 'ldap://cpt-dc-01'

base = 'dc=visionoss,dc=int'

query = '(&(objectCategory=person)(objectclass=user)(!(UserAccountControl:1.2.840.113556.1.4.803:=2)))'

def formatter(ldap_string, array):
    minor_data = ldap_string[0][0]
    major_data = ldap_string[0][1]
    if len(major_data['displayName'][0].split(" ")) < 2:
        return -1
    if any(word in major_data['displayName'][0] for word in BlackListTerm):
        return -1
    if major_data['userPrincipalName'][0] in Exclusion_list:
        return -1

    # for key, value in major_data.iteritems():
    #     if str(key) not in LdapFilter:
    #         print "'%s' | '%s'" % (key, value[0])
    fn, sn, title, mail, mobile, tel, tel1, skype, loc, man, ip = '', '', '', '', '', '', '', '', '', '', ''
    try:
        fn = major_data['givenName'][0]
    except:
        pass
    try:
        sn = major_data['sn'][0]
    except:
        pass
    try:
        mail = major_data['mail'][0]
    except:
        pass
    try:
        title = major_data['title'][0]
    except:
        pass
    try:
        mobile = major_data['mobile'][0]
    except:
        pass
    try:
        tel = major_data['facsimileTelephoneNumber'][0]
    except:
        pass
    try:
        tel1 = major_data['telephoneNumber'][0]
    except:
        pass
    try:
        skype = major_data['extensionAttribute15'][0]
    except:
        pass
    try:
        loc = major_data['physicalDeliveryOfficeName'][0]
    except:
        pass
    try:
        man = major_data['manager'][0].split(",")[0].split("=")[1]
    except:
        pass
    try:
        ip = major_data['ipPhone'][0]
    except:
        pass

    if len(tel) < 5:
        tel = tel1

    node = userNode(fn, sn, mail, title, mobile, tel, skype, loc, man, ip)
    tmpName = str(fn + " " + sn)
    array[tmpName] = node


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
                    formatter(result_data, Formatted)

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
        userObj.setParent(managerObj)
        managerObj.addChild(userObj)

