#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on 2020/9/13

@author Ow-woo
"""
import matplotlib.pyplot as plt
class Monitor():
    def __init__(self, total_timesteps, reset_num_timesteps, max_reward):
        self.total_timesteps = total_timesteps
        self.reset_num_timesteps = reset_num_timesteps
        self.max_reward = max_reward
        self.x = []
        self.y = []
        self.plt = plt
        self.plt.figure(figsize=(15,15))

    def plot_(self, CurEposide, EposideR):
        self.eposide_max = self.total_timesteps/self.reset_num_timesteps
        self.y_max = self.max_reward
        self.x.append(CurEposide)
        self.y.append(EposideR)
        self.plt.cla()
        self.plt.xlim(0, self.eposide_max)
        self.plt.ylim(0, self.y_max)
        self.plt.xlabel("num_episode")
        self.plt.ylabel("EpisodeR")
        self.plt.title("R_curve")
        self.plt.ion()
        self.plt.grid()
        self.plt.plot(self.x, self.y, '-r', lw=1)
        self.plt.text(0, -10, "CurEpisodeR :" + str(EposideR), fontsize=15, color='g')
        self.plt.ion()
        self.plt.show()
        self.plt.pause(0.01)
if __name__ == "__main__":
    import math
    import time
    m = Monitor(1e4, 100, 100)
    for i in range(100):
        m.plot_(i, i)
        time.sleep(0.1)
