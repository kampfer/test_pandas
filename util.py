#coding:utf-8

import pandas as pd
import numpy as np
import math

def basicStats(data):
    return {
        'mean': data.mean(),
        'std': data.std(),
        'skew': data.skew(),
        'kurt': data.kurt(),
        'max': data.max(),
        'min': data.min()
    }

def mean(data):
    sum = 0
    for value in data:
        sum += value
    return sum / len(data)

def std(data):
    sampleMean = mean(data)
    sum = 0
    for value in data:
        sum += (value - sampleMean)**2
    return math.sqrt(sum / (len(data) - 1))

def max(data):
    max = data[0]
    for value in data:
        if value > max:
            max = value
    return max

def min(data):
    min = data[0]
    for value in data:
        if value < min:
            min = value
    return min

def skew(data):
    sampleMean = mean(data)
    sampleStd = std(data)
    sum = 0
    for value in data:
        sum += (value - sampleMean)**3
    return sum / sampleStd**3 / (len(data) - 1)

def kurt(data):
    sampleMean = mean(data)
    sampleStd = std(data)
    sum = 0
    for value in data:
        sum += (value - sampleMean)**4
    return sum / sampleStd**4 / (len(data) - 1)

def basicStats2(data):
    return {
        'mean': mean(data),
        'std': std(data),
        'skew': skew(data),
        'kurt': kurt(data) - 3,
        'max': max(data),
        'min': min(data)
    }
