import string as s
from random import *

ch = s.ascii_letters + s.digits + s.punctuation

senha = ''.join(choice(ch)for j in range(randint(8,16)))

print('Senha gerada é: ' + senha)
