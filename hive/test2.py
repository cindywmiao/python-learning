from pyhive import hive
from pyhive import presto

cursor = presto.connect('localhost').cursor()
cursor.execute('SELECT * FROM my_awesome_data LIMIT 10')
print cursor.fetchone()
print cursor.fetchall()