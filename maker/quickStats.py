from __future__ import print_function, division
from collections import defaultdict, OrderedDict
import gzip
import pickle
import json
import os
import uproot
import matplotlib.pyplot as plt
#matplotlib inline
import numpy as np
from coffea import hist, processor 
from coffea.hist import plot

hists={}
pd = []
year = '2018'
dirname = '../grinder/pods/' + year

#Input all of the pods from pods/year
for filename in os.listdir(dirname):
    if 'MET' in filename or 'SingleElectron' in filename or 'SinglePhoton' in filename or 'EGamma' in filename: continue
    if '.pkl.gz' in filename:
        if filename.split("____")[0] not in pd: pd.append(filename.split("____")[0])
        with gzip.open(dirname+'/'+filename) as fin:
            hin = pickle.load(fin)
            for k in hin.keys():
                if k in hists: hists[k]+=hin[k]
                else: hists[k]=hin[k]

for key in hists:
    print(key)


scale={}
for pdi in hists['sumw'].identifiers('dataset'):
    scale[pdi]=hists['sumw'].integrate('dataset', pdi).values(overflow='all')[()][1]
    print(pdi,scale[pdi])
