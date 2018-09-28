from __future__ import print_function
from vconnector.core import VConnector

client = VConnector(
    user='root',
    pwd='Djmb78xz#',
    host='192.168.100.199'
)
client.connect()
vms = client.perf_counter
print(vms)
