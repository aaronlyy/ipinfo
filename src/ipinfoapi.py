'''
lib for accessing the ipinfo.io API.\n
------------------------------------\n
author: Aaron Can // aaronlyy\n
website: https://krotesq.net/\n
------------------------------------
'''

import requests
import socket

class IpInfo:
    def __init__(self):
        self.apiUrl = 'http://ipinfo.io/'
    
    def __repr__(self):
        return 'Object: IpInfo ({})'.format(self.apiUrl)
    
    def isup(self):
        '''
        checks if the ipinfo.io server is up.\n
        returns True or False.
        '''
        try:
            res = requests.get(self.apiUrl)
            if res.status_code == 200:
                return True
            else:
                return False
        except Exception as err:
            print('\nerror {}\n'.format(err))
            raise

    def reqinfo(self, ip=''):
        '''
        request ipinfo response\n
        returns full info about the given ip (no ip = own machine) as dictionary.\n
        returns None if no info is available.
        '''
        
        try:
            res = requests.get(self.apiUrl + ip)
            if res.status_code == 200:
                return IpInfoContainer(dict(res.json()))
            else:
                return None
        except:
            raise
    
    def getipfromdomain(self, domain):
        '''
        resolve ip-address from given domain
        '''
        try:
            return socket.gethostbyname(domain) 
        except:
            return None

class IpInfoContainer:
    '''
    contains info about an ip-address
    '''

    def __init__(self, infodict):
        self.infodict = infodict

    def __repr__(self):
        return 'Object: IpInfoContainer ({})'.format(self.infodict['ip'])
    
    def __getattr__(self, attr):
        if attr in self.infodict:
            return self.infodict[attr]
        else:
            return None

    def getfullinfo(self):
        return self.infodict