import random
passlength = int(input('enter the length of your password. (min.6)'))
r = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()'
p = "".join(random.sample(r,passlength))
print(p)