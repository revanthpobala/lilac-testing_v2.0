import time
import hashlib
import random
import string


class generator:
    
    
    def gen_random_message(self):
        chars = "".join( [random.choice(string.letters) for i in xrange(12)]) 
        return chars
    
    def generate(self,total_users):
        users = []
        for i in range(0,total_users):
            users1= generator.gen_random_message(self)
            users.append(users1)
        if len(users) == total_users:
            file_open = open('users.txt','w')
            for item in users:
                item = (item[1:12] + " \n")
                file_open.write(item)
            file_open.close()
        print "Done"
upload = generator()
upload.generate(3)