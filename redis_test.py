import uuid
import timeit
import string 
import random 
import redis

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
db = redis.Redis(host='localhost', port=6379, db=0)

inicio = timeit.default_timer()
for item in values:
    db.set(item['key'], item['value'])

fim = timeit.default_timer()

print ('duracao inserções: %f' % (fim - inicio))

# =================================================== #
random.shuffle(values)

inicio = timeit.default_timer()
for item in values:
    data = db.get(item['key'])

fim = timeit.default_timer()

print ('duracao recuperação dos dados: %f' % (fim - inicio))