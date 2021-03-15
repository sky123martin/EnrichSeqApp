from application import app
import sys
import pandas as pd
import numpy as np 
import requests 
import os.path
import random
import math
from os import path


def generate_EnrichSeq_results(ID, num_phages = 10, timesteps = 10, std_error = 10, max_initial = 100):
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    total_counts = [0]*timesteps
    data = []
    for _ in range(num_phages):
        phage_name = "".join([random.choice(alphabet) for _ in range(5)])
        # generate rate of growth and slope, assuming exponential growth
        r = np.random.uniform(low=-1, high=1) # rate of growth
        p0 = np.random.uniform(low=0, high=max_initial) # initial
        data.append([phage_name, 0, p0])
        total_counts[0] += p0
        # run forward sim
        for t in range(1,timesteps):
            y =  p0*math.e**(r*t) + np.random.normal(loc=0.0, scale=std_error)
            data.append([phage_name, t, y])
            total_counts[t] += y

    for i in range(len(data)):
        data[i].append(data[i][2]/total_counts[data[i][1]])

    
    df = pd.DataFrame(data = data, columns=["phage", "t", "reads", "fraction_total_reads"])
    df.to_csv("data/{}_result.csv".format(ID))
    return df