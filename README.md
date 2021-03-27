# Python-Apache-Cassandra-Connection-and-CQL-Interface

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
nc -vz 192.168.1.105 9042
OR
telnet 192.168.1.105 9042
```
In case if response is negative, there may be several reasons. 
```
nc: connectx to 192.168.56.105 port 9042 (tcp) failed: Connection refused
```
Possibly, port (9042) is blocked by firewall. Using following command, firewall can be stopped. 
```
systemctl stop firewalld
```
If it doesn't help, edit Cassandra settings file ```/etc/cassandra/conf/cassandra.yaml``` to enable remote connection to cluster. Change values of ```rpc_address``` and ```broadcast_rpc_address``` accordingly
```
rpc_address: 0.0.0.0
broadcast_rpc_address: 192.168.56.105
```
