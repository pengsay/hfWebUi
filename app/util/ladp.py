from ldap3 import Server, Connection, ALL, NTLM

import os

class Ldap_Connector:
    def __init__(self, username=None, password=None):
        host = os.environ.get('HOST')
        port = os.environ.get('PORT')
        base_dn = os.environ.get('LDAP_SSL')
        use_ssl = os.environ.get('BASE_DN')

        # use_ssl = False
        self.username = username
        self.password = password
        self.server = Server(host=host, port=port,
                             use_ssl=use_ssl, get_info=ALL)
        self.conn = Connection(self.server, '%s\\%s' % (
            base_dn, username), password, authentication=NTLM)

    # 认证是否通过 Ture/False
    def auth(self):
        return self.conn.bind()
