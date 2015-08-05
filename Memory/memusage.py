import os
import psutil
import time
import datetime
import matplotlib.pyplot as plt
import numpy as np
class memory():
    
    def get_pids(self):
        pid_proc = {}
        for proc in psutil.process_iter():
            try:
                pinfo = proc.as_dict()
                if pinfo['name']=='node':
                    a = pinfo['pid']
                    pid_proc[str(a)] = pinfo['memory_percent']
            except psutil.NoSuchProcess:
                pass

        return  pid_proc 
    
    
    def get_multiple(self,iterations,times):
        total_pids = []
        interval = 3
        node1 = []
        node2 = []
        node3 = []
        
        for i in range(iterations):
            dic = mem.get_pids()
            time.sleep(times)
            for k,v in dic.iteritems():
                total_pids.append(v)
        
        length = len(total_pids)
        iter = length/3
        for i in range(0,length):
            for j in range(iter):
                if i==0:
                    node1.append(total_pids[j*interval])
                if i==1:
                    node2.append(total_pids[1+(j*interval)])
                if i==2:
                    node3.append(total_pids[2+(j*interval)])
        print total_pids
        print node1, "\n",node2,"\n",node3
        return node1,node2,node3
    
    
    def another_method(self):
        final = {}
        starting = datetime.datetime.now()
        print starting
        for i in range(100):
           print i
           current = mem.get_pids()
           time.sleep(10)
           for k in current:
               if k not in final: final[k] = []
               final[k].append(current[k])
        ending = datetime.datetime.now()
        for i in final:
            plt.ylabel('Memory Percentage ')
            plt.xlabel('Number of recordings')
            plt.plot(final[i],'-')                
            plt.show()
        open_file = open('memdata.log','a')
        open_file.write(str(starting))
        open_file.write('\n')
        open_file.write(str(final))
        open_file.write('\n')                            
        print final          
    
    
    def draw_graphs(self):
        arr1,arr2,arr3 = mem.get_multiple(100,60)
        plt.ylabel('$Memory Percentage $')
        plt.xlabel('$Number of recordings$')
        plt.plot(arr1,'-')
        plt.show()
        plt.plot(arr2,'green')
        plt.ylabel('$Memory Percentage $')
        plt.xlabel('$Number of recordings$')
        plt.show()
        plt.plot(arr3,'red')
        plt.ylabel('$Memory Percentage $')
        plt.xlabel('$Number of recordings$')
        plt.show()
    
        
mem = memory()

mem.another_method()