import ipinfo

# create IpInfo Object
ipapi = ipinfo.IpInfo()

# check if ipinfo.io server is up
if ipapi.isup():
    print('server is running')
else:
    print('server is down')

# get ip from a domain
ip = ipapi.getipfromdomain('github.com')
print(ip)

# request info about an ip
info = ipapi.reqinfo('8.8.8.8')
print(info)

# access specific info from container
# list of all attributes: https://ipinfo.io/developers/responses#full-response (only free plan attributes work)
print(info.country)
print(info.region)

# get full response as dictionary
full_info = info.getfullinfo()
print(full_info)
