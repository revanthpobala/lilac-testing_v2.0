#####################################################################################
#extract.py
#Authors: Revanth Pobala and Hussain Mucklai.
#This project is about the Testing of Lilac(Lightweight low latency anonymous chat)
#This program will provide the graph for cdf(Cumulative Distribution function)
#####################################################################################
import os
import matplotlib.pyplot as plt
from pylab import *
from scipy.stats import norm
import matplotlib.patches as mpatches
from bisect import bisect_left
import numpy as np
import cdf_plot
from scipy.interpolate import spline

class discrete_cdf:
    def __init__(self,data):
        self._data = data # must be sorted
        self._data_len = float(len(data))

    def __call__(self,point):
        return (len(self._data[:bisect_left(self._data, point)]) / 
                self._data_len)

class extract():

    def __init__(self):
        self.to_draw = []    
    
    
    def read_from_file(self,filename):
        file = open(filename,'rw')
        return file
    
    
    
    def merge_files(self):
        os.system('cat /home/revanth/Projects/workspace/Lilac_Testing/src/users/logs/*.txt >/home/revanth/Projects/workspace/Lilac_Testing/src/Results/finalfile.txt')
        
        

    def add_to_dict(self):
        items = {}
        graph_values = []
        to_draw = []
        median = []
        sum = 0
        file = extract.read_from_file('finalfile.txt')
        for i in file.readlines():
            if len(i.strip()) != 0:
                content = i.split(',')
                msg = content[0].strip()
                Time = float(str(content[1].strip()))
                if msg not in items:
                    items[msg] = []
                items[msg].append(Time)
        
        for i in items:
            for j in items[i]:
                if len(items[i]) != 1:
                    items[i] = sort(items[i])
                    graph_values.append(float(items[i][1]- items[i][0]))
                
        #graph_values = set(graph_values)
        for i in graph_values:
            if i  !=0:
                to_draw.append(i*0.1)
                sum = sum+i
        avg = np.average(sum)/len(to_draw)*0.1
        print avg
        self.to_draw = np.array(to_draw)
        anthax =  np.arange(0,len(to_draw)) 
        plt.plot(anthax, self.to_draw, '-')
        plt.xticks()
        plt.ylabel('Time (Seconds)')
        plt.xlabel('Number of Messages')
        plt.title(r'Time  vs Number of messages')
        plt.show()   
 

    def draw_another(self):
        first_array = []
        sorted = sort(self.to_draw)
        summing = sorted.sum()
        for i in sorted:
            first_array.append(i/summing)
        cumsum1 = np.cumsum(first_array)
        xaxis = sorted
        yaxis = cumsum1
        plt.plot(xaxis,yaxis,'green')
        plt.title(r'Cumulative Distribution Function')
        plt.ylabel('cdf of messages')
        plt.xlabel('graph point per data point')        
        plt.show()
    
        

extract =  extract()
#extract.merge_files()
extract.add_to_dict()
extract.draw_another()



