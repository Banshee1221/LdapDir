import ldap
from objectFormatter import *


def ldap_search(ldap_uri, base, query, user, passwd, arg):
    
    formatted = {}
    
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
                    if arg == 1:
                        jsonFormatter(result_data, formatted)
                    else:
                        formatter(result_data, formatted)

        if len(formatted) == 0:
            print('No results found.')
            return

        return formatted

    except ldap.LDAPError, e:
        print('LDAPError: %s.' % e)

    finally:
        l.unbind_s()