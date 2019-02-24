import random

ip_list = [
    "118.81.71.180:9797",
    "123.138.89.133:9999"
]

def gethttpIP():
    ip = random.choice(ip_list)
    return ip
print(gethttpIP())



