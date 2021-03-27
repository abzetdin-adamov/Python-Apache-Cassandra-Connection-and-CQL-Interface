from cassandra.cluster import Cluster
cluster = Cluster(['192.186.10.100'], port=9042)
session = cluster.connect('ada_keyspace', wait_for_all_pools=True)
session.execute('USE ada_keyspace')
rows = session.execute('SELECT * FROM staff')
for row in rows:
    print(row.name, row.surname, row.email, row.bdate)
