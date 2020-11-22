#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 16:12:51 2020

@author: Boyuan-Tian
"""

import os
import sys
import numpy as np
import matplotlib.pyplot as plt

plot_option = sys.argv[1]
path = sys.argv[2]
app_name = sys.argv[3]
def readSSIMGPU(path):
    skipline = 1
    index, score = [], []

    f = open(path)
    for line in f.readlines()[skipline:]:
        num = int((line.strip().split(" ")[0]).split(".")[0])
#        print num
        index.append(num)
        if plot_option == "flip":
            score.append(1.0-float(line.strip().split(" ")[2]))
        elif plot_option == "weight_flip":
            score.append(1.0-float(line.strip().split(" ")[1]))
        elif plot_option == "color":
            score.append(1.0-float(line.strip().split(" ")[3]))
        elif plot_option == "feature":
            score.append(1.0-float(line.strip().split(" ")[4]))
    f.close()

    return index, score



sponza_index, sponza_score = readSSIMGPU(path)


round_idx = 3200
plt.figure(figsize=(25, 5))

#============================================================================================

sponza = plt.subplot(111)

if plot_option =="flip":
    sponza.set_title('FLIP Inverse Avg Score - App: %s' % app_name, fontsize = 24)
    plt.ylabel("FLIP Inverse score", fontsize = 24)
elif plot_option =="weight_flip":
    sponza.set_title('FLIP Weight Avg Score - App: %s' % app_name, fontsize = 32)
    plt.ylabel("FLIP Weighted score", fontsize = 40)
elif plot_option =="color":
    sponza.set_title('FLIP Color Score - App: %s' % app_name, fontsize = 32)
    plt.ylabel("FLIP Color score", fontsize = 40)
elif plot_option =="feature":
    sponza.set_title('FLIP Feature Score - App: %s' % app_name, fontsize = 32)
    plt.ylabel("FLIP Feature score", fontsize = 40)


sponza.plot(sponza_index[0 : round_idx], sponza_score[0 : round_idx], 'g', label = app_name)

sponza.set_xlim([0, 3201])
sponza.set_ylim([0.6, 1])

sponza.spines["top"].set_linewidth(3)
sponza.spines["bottom"].set_linewidth(3)
sponza.spines["left"].set_linewidth(3)
sponza.spines["right"].set_linewidth(3)

#============================================================================================


plt.tick_params(labelsize = 32)

plt.xticks(np.arange(0, 3201, step=400))
plt.yticks(np.arange(0.6, 1.01, step=0.1))

plt.xlabel("frame index", fontsize = 40)

plt.subplots_adjust(left = 0.08, right = 0.97, top = 0.88, bottom = 0.12)

plt.show()
