# Python Apache Cassandra Connection and CQL Interface

This tutorial describes how to connect from Python to remote Apache Cassandra and exacute CQL commands on database. In my case Cassandra is installed on VM (VirtualBox) and my host computer is Mac. 
First of all make sure that Cassandra's system service is running and listening default port 9042 (if default port has not been changed). Run one of the following commands on the machine where Cassandra is installed to check if port is active. 
```
sudo netstat -anp | grep 9042
OR
sudo lsof -i | grep 9042 
```
The following output is what you can expect
```
java       1682 cassandra  134u  IPv4  20375      0t0  TCP *:9042 (LISTEN)
```
Now try to check if you have access to the same IP/PORT from another computer where from you want to connect. Since, in my case, my host computer is Mac, I'll try to check if my host computer sees the service running on VM. Mac computer has very useful utility ```nc``` network thin client. If host computer is running under Linux or Windows, the ```telnet``` can be employed.
```
nc -vz 192.168.10.100 9042
OR
telnet 192.168.10.100 9042
```
In case if response is negative, there may be several reasons. 
```
nc: connectx to 192.168.10.100 port 9042 (tcp) failed: Connection refused
```
Possibly, port (9042) is blocked by firewall. Using following command, firewall can be stopped. 
```
systemctl stop firewalld
```
If it doesn't help, edit Cassandra settings file ```/etc/cassandra/conf/cassandra.yaml``` to enable remote connection to cluster. Change values of ```rpc_address``` and ```broadcast_rpc_address``` accordingly
```
rpc_address: 0.0.0.0
broadcast_rpc_address: 192.168.10.100
```
After restarting the service check IP/PORT again
```
sudo systemctl restart cassandra
nc -vz 192.168.10.100
found 0 associations
found 1 connections:
     1:	flags=82<CONNECTED,PREFERRED>
	outif vboxnet0
	src 192.168.10.1 port 57799
	dst 192.168.10.100 port 9042
	rank info not available
	TCP aux info available
Connection to 192.168.10.100 port 9042 [tcp/*] succeeded!
```
Finally, connection successfully established from host computer to Cassandra service that listen specific port. 
Now, in order to connect to Cassandra through Python, let install Cassandra driver for Python
```
pip install cassandra-driver
```
Following Python snippet will retrieve records from Column Family (Table) ```staff``` associated with Keyspace (Databse) ```my_keyspace```. More details about  Cassandra data model and setting environment are available at [Install and set up Apache Cassandra on CentOS](https://github.com/abzetdin-adamov/Install-and-set-up-Apache-Cassandra-on-CentOS).
```python
from cassandra.cluster import Cluster
cluster = Cluster(['192.186.10.100'], port=9042)
session = cluster.connect('ada_keyspace', wait_for_all_pools=True)
session.execute('USE ada_keyspace')
rows = session.execute('SELECT * FROM staff')
for row in rows:
    print(row.name, row.surname, row.email, row.bdate)
```
