import pandas as pd
import numpy as npy
import scipy as spy
import pysrt
import os

#https://dzone.com/articles/how-to-paraphrase-text-in-python-using-nlp-librari#:~:text=In%20Python%2C%20there%20are%20machine,are%20%E2%80%9CDeep%20learning%E2%80%9D%20models.

print("hello bryan")
data = pd.read_csv('onePiece_title.csv', sep=',')

f = open('onePiece_ep/ep6.txt', 'w')
f.write('fdjsljldfg')

f.close()

with open('../ep1.txt', 'r') as f:
    print(f.read())


i = 1
for fname in os.listdir('onePiece_ep_trans'):
    os.rename(fname, str(i)+'.txt')
    i=i+1





    