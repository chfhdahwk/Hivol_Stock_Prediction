import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import minmax_scale
import pandas as pd
import math

def rank_measuring(df, input_size):
    for i in range(input_size): #columns nums 
        train_mean=0
        p_sum=0 
        n_sum=0 
        p_cnt=0 
        n_cnt=0  
        p_std=0 
        n_std=0 
        para=0
        histo_min, histo_max = df[i].min(), df[i].max()
        mean_val = df[i].mean()
        val = df[i].values
        
        for j in val:
            if j > 0:
                p_sum += (j-mean_val)*(j-mean_val)
                p_cnt += 1
            else:
                n_sum += (j-mean_val)*(j-mean_val)
                n_cnt += 1
        if p_cnt != 0 :
            p_std = math.sqrt(p_sum/p_cnt)
        else: 
            p_std = 0
        if n_cnt != 0 :
            n_std = math.sqrt(n_sum/n_cnt)
        else:
            n_std = 0
        max_val = mean_val + histo_max * p_std
        min_val = mean_val - histo_min * n_std
        new_para_list = []
        for k in val:
            if k > 0:
                para = (0.9999 * (k-0.0)) + 0.501*(max_val-k) / (max_val-0.0)
            else:
                para = (0.5 * (k-min_val) + 0.0001*(0.0-k)) / (0.0-min_val)
            para = math.tanh(para-0.5)
            if para > 1.0: para =  1.0
            if para < -1.0: para =  -1.0
            new_para_list.append(para)
        df[i] = new_para_list
    return df


def each_rank_measuring(df, input_size, index):
    for i in range(input_size): #columns nums 
        train_mean=0
        p_sum=0 
        n_sum=0 
        p_cnt=0 
        n_cnt=0  
        p_std=0 
        n_std=0 
        para=0
        histo_min, histo_max = df[i].min(), df[i].max()
        mean_val = df[i].mean()
        val = df[i].values
        
        for j in val:
            if j > 0:
                p_sum += (j-mean_val)*(j-mean_val)
                p_cnt += 1
            else:
                n_sum += (j-mean_val)*(j-mean_val)
                n_cnt += 1
        if p_cnt != 0 :
            p_std = math.sqrt(p_sum/p_cnt)
        else: 
            p_std = 0
        if n_cnt != 0 :
            n_std = math.sqrt(n_sum/n_cnt)
        else:
            n_std = 0
        max_val = mean_val + histo_max * p_std
        min_val = mean_val - histo_min * n_std
        new_para_list = []
        for k in val:
            if k > 0:
                para = (0.9999 * (k-0.0)) + 0.501*(max_val-k) / (max_val-0.0)
            else:
                para = (0.5 * (k-min_val) + 0.0001*(0.0-k)) / (0.0-min_val)
            para = math.tanh(para-0.5)
            if para > 1.0: para =  1.0
            if para < -1.0: para =  -1.0
            new_para_list.append(para)
        df[i] = new_para_list
    return df[index]
    
