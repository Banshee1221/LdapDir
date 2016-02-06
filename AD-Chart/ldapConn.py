import ldap
from objectFormatter import *


def ldap_search(ldap_uri, base, query, user, passwd, arg):

    formatted = {}

    try:
        ldap_conn = ldap.initialize(ldap_uri)
        ldap_conn.set_option(ldap.OPT_REFERRALS, 0)
        ldap_conn.simple_bind_s(user, passwd)
        ldap_conn.protocol_version = ldap.VERSION3
        search_scope = ldap.SCOPE_SUBTREE
        retrieve_attributes = None

        ldap_result_id = ldap_conn.search(
            base,
            search_scope,
            query,
            retrieve_attributes
        )
        while 1:
            result_type, result_data = ldap_conn.result(ldap_result_id, 0)
            if result_data:
                break
            else:
                if result_type == ldap.RES_SEARCH_ENTRY:
                    if arg == 1:
                        jsonFormatter(result_data, formatted)
                    else:
                        formatter(result_data, formatted)

        if len(formatted) == 0:
            print('No results found.')
            return -1

        return formatted
    
    except ldap.INVALID_CREDENTIALS:
        print ("Incorrect credentials.")
        return -1

    except ldap.SERVER_DOWN:
        print ("LDAP server is unavailable.")
        return -1

    except ldap.LDAPError, e:
        print('LDAPError: %s.' % e)
        return -1

    finally:
        ldap_conn.unbind_s()
