# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 11:43:10 2021

@author: thoma
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from numpy import loadtxt

data = np.loadtxt('data.csv', delimiter = ',')
A = list(data[:,0])
Beta2 = list(data[:,3])
Eratio = list(data[:,4])
NeutronNumber = list(data[:,5])


def DoPlot(X, Y, Xlabel, Ylabel, Title, Save):
    
    plt.clf()
    plt.plot(X, Y, color = 'k', linestyle = '--', marker = 'o', markerfacecolor = 'r')
    plt.title(Title)
    plt.xlabel(Xlabel)
    plt.ylabel(Ylabel)
    plt.grid()
    plt.savefig(Save+"Chart.png")
    plt.show()

DoPlot( A, Beta2, 'Mass Number A', r'Grodzins $\beta_{2}$',
       r'Grodzins $\beta_{2}$ values of samarium as a function' + 'of its \n corresponding mass number for different isotopes.',
       '2a')

DoPlot( NeutronNumber, Eratio, 'Neutron Number N', r'Energy Ratio $E(4^{+})$/$E(2^{+})$',
       r'The Energy ratio $E(4^{+})$/$E(2^{+})$ as a function of neutron number.',
       '2b')
