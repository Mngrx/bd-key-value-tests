import uuid
import timeit
import string 
import random 
from pymemcache.client import base

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
client = base.Client(('localhost', 11211))

inicio = timeit.default_timer()
for item in values:
    client.set(item['key'], item['value'])

fim = timeit.default_timer()

print ('duracao inserções: %f' % (fim - inicio))

# =================================================== #
random.shuffle(values)

inicio = timeit.default_timer()
for item in values:
    data = client.get(item['key'])

fim = timeit.default_timer()

print ('duracao recuperação dos dados: %f' % (fim - inicio))