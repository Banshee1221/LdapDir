from objectStorer import *

BlackListTerm = ['Administrator', "Admin", "Guest", "Voss", "VOSS", "Machine", "move", "IT", "Support", "Test",
                 "Lab", "Temp", "Kiosk"]
#LdapFilter = ['objectSid', 'objectGUID', 'photo']
Exclusion_list = ["owen.bridle@visionoss.int", "mario.vanriesen@visionoss.int", "jenkins@visionoss.int"]


def formatter(ldap_string, array):
    major_data = ldap_string[0][1]
    if len(major_data['displayName'][0].split(" ")) < 2:
        return -1
    if any(word in major_data['displayName'][0] for word in BlackListTerm):
        return -1
    if major_data['userPrincipalName'][0] in Exclusion_list:
        return -1

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


def jsonFormatter(ldap_string, array):
    major_data = ldap_string[0][1]
    if len(major_data['displayName'][0].split(" ")) < 2:
        return -1
    if any(word in major_data['displayName'][0] for word in BlackListTerm):
        return -1
    if major_data['userPrincipalName'][0] in Exclusion_list:
        return -1
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

    node = userDict(fn, sn, mail, title, mobile, tel, skype, loc, man, ip)
    tmpName = str(fn + " " + sn)
    array[tmpName] = node
