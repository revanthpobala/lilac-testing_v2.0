import os

class files():
    
    def open_file(self):
        jsondocs = {}
        open_file = open('log.txt','r')
        wite_file = open('a.json','a')        
        for i in open_file.readlines():
            a = i.split(',')
            print a[0]
            print a[1]
            final = '{'+'"'+a[0]+'":'+'"'+a[1]+'"'+"}"
            wite_file.write(final)
            
            
            
files = files()
files.open_file()