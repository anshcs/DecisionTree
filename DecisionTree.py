'''
Assume df is a pandas dataframe object of the dataset given
'''

import numpy as np
import pandas as pd
import math
import random


'''Calculate the entropy of the enitre dataset'''


def get_entropy_of_dataset(df):
    # TODO
    p_count = 0
    n_count = 0
    for i in range(len(df)):
        if df.iloc[:, -1][i] == "yes":
            p_count += 1
        else:
            n_count += 1
    if p_count > 0 and n_count > 0:
        entropy = -1*((p_count/len(df))*(math.log(p_count/len(df), 2)) +
                      (n_count/len(df))*(math.log(n_count/len(df), 2)))
    elif n_count == 0:
        entropy = -1*(p_count/len(df))*(math.log(p_count/len(df), 2))
    else:
        entropy = -1*(n_count/len(df))*(math.log(n_count/len(df), 2))
    return entropy


'''Return avg_info of the attribute provided as parameter'''


def get_avg_info_of_attribute(df, attribute):
    # TODO
    pvia = []
    diff_attr = df[attribute].unique()
    for i in diff_attr:
        pvia.append(per_val_ia(df, attribute, i))
    avg_info = sum(pvia)
    return avg_info


'''Return Information Gain of the attribute provided as parameter'''
t


def get_information_gain(df, attribute):
    # TODO
    information_gain = get_entropy_of_dataset(
        df)-get_avg_info_of_attribute(df, attribute)
    return information_gain


def get_selected_attribute(df):
    '''
    Return a tuple with the first element as a dictionary which has IG of all columns 
    and the second element as a string with the name of the column selected

    example : ({'A':0.123,'B':0.768,'C':1.23} , 'C')
    '''
    # TODO
    l = []
    dict = {}
    for i in df.columns[:len(df.columns)-1]:
        dict[i] = (get_information_gain(df, i))
    l.append(dict)
    next_node = max(dict, key=dict.get)
    l.append(next_node)
    my_tup = tuple(l)
    return my_tup


def per_val_ia(df, attribute, value):
    sv = 0
    for i in range(len(df)):
        if df[attribute][i] == value:
            sv += 1
            newdf = new_df(df, attribute, value)
    per_val = (sv/len(df))*(get_entropy_of_dataset(newdf))
    return per_val


def new_df(df, attribute, value):
    new_df = pd.DataFrame(columns=df.columns)

    for i in range(len(df)):
        if df[attribute][i] == value:
            new_vals = df.iloc[i]
            new_df.loc[len(new_df)] = new_vals

    return new_df
