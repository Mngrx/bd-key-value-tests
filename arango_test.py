import uuid
import timeit
import string 
import random 
from pyArango.connection import *

num_exec = 10000

values = []
string_size = 10

inicio = timeit.default_timer()
for i in range(num_exec):
    new_key = uuid.uuid4()
    some_string = ''.join(random.choices(string.ascii_letters + string.digits, k = string_size)) 
    values.append({ 'key': str(new_key), 'value': some_string })

fim = timeit.default_timer()

print ('duracao geração dos dados: %f' % (fim - inicio))

# =================================================== #
conn = Connection(username="root", password="openSesame")
db = conn.createDatabase(name="test")
collection = db.createCollection(name="execute_tests")

inicio = timeit.default_timer()
for item in values:
    doc = collection.createDocument()
    doc._key = item['key']
    doc['value'] = item['value']
    doc.save()

fim = timeit.default_timer()

print ('duracao inserções: %f' % (fim - inicio))

# =================================================== #
random.shuffle(values)

inicio = timeit.default_timer()
for item in values:
    data = collection[item['key']]

fim = timeit.default_timer()

print ('duracao recuperação dos dados mesma conexão: %f' % (fim - inicio))

# =================================================== #
conn2 = Connection(username="root", password="openSesame")
db2 = conn2["test"]
collection2 = db2["execute_tests"]


inicio = timeit.default_timer()
for item in values:
    data = collection2[item['key']]

fim = timeit.default_timer()

print ('duracao recuperação dos dados: %f' % (fim - inicio))