#!//use/bin/env python3


#Simple python code to generate random password with user generated length.

from random import *
import string

characters = string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase + string.digits

password = "".join(choice(characters) for x in range(randint(8, 12)))

print(password)


