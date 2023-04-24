import random
import string

n1 = int(input("Password lenght: "))
l1 = string.ascii_letters + string.digits
pas = ''.join(random.choice(l1) for i in range(n1))
print("Your generated password:", pas)