#! /usr/bin/env python2
#
# Example of using Python OpenSSL bindings to create a key and self-signed cert
# with a Unicode DN. This may or may not be 100% correct, but seems to mostly
# work.
#
# Based on lots of random web sites and examples out on the web....

from OpenSSL import crypto

# Key
k = crypto.PKey()
k.generate_key(crypto.TYPE_RSA, 4096)

# Cert
c = crypto.X509()
c.get_subject().CN = u'\U00002714\U00002660\U00002663\U00002665\U00002666'
c.get_subject().OU = u'OrgUnit'
c.get_subject().O = u'Organization'
c.get_subject().L = u'City'
c.get_subject().ST = u'State'
c.get_subject().C = u'US'
c.set_serial_number(1)
c.gmtime_adj_notBefore(0)
c.gmtime_adj_notAfter(2592000) # 30 days
c.set_issuer(c.get_subject())
c.set_pubkey(k)
c.sign(k, 'sha512')

print crypto.dump_privatekey(crypto.FILETYPE_PEM, k)
print crypto.dump_certificate(crypto.FILETYPE_PEM, c)
