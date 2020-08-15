# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import pickle
import numpy

#load lost list
with open('lost_list.pkl', 'rb') as f:
    lost_list = pickle.load(f)

#plot all epochs
y = lost_list
x = numpy.arange(len(y))
plt.plot(x, y, label='train')
plt.xlabel('iterations (x' + '20' + ')')
plt.ylabel('loss')
plt.show()

#plot 10 epoch
for i in range(5):
    y = lost_list[(i*9295)*10//20:((i+1)*9295)*10//20]
    x = numpy.arange(len(y))
    plt.plot(x, y, label='train')
    plt.xlabel('iterations (x' + '20' + ') in epoch' +str(i*10) +'to' +str((i+1)*10))
    plt.ylabel('loss')
    plt.show()

#plot each epoch
for i in range(50):
    y = lost_list[(i*9295)//20:((i+1)*9295)//20]
    x = numpy.arange(len(y))
    plt.plot(x, y, label='train')
    plt.xlabel('iterations (x' + '20' + ') in epoch' +str(i+1))
    plt.ylabel('loss')
    plt.show()
    
