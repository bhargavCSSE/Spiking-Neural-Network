import numpy as np
import random

class LIF:
    def __init__(self):
        self.P_min = -1
        self.P_rest = 0
        self.P_thres = 10
        self.P_spike = 1
        self.pot_plot = []

        self.t_rest = 0
        self.t_refr = 5
        self.leak = 0.125

        self.mem_pot = self.P_rest
        self.out = 0
        self.out_array = []

    def output_spike(self, t):
        if self.mem_pot >= self.P_thres:
            self.mem_pot += self.P_spike
            self.t_rest = t + self.t_refr
            return self.P_spike
        else:
            return self.P_rest

    def execute(self, t, S):
        if t <= self.t_rest:
            self.mem_pot = self.P_rest
            self.pot_plot.append(self.mem_pot)

        elif t > self.t_rest:
            if self.mem_pot > self.P_min:
                self.mem_pot += S - self.leak
                self.pot_plot.append(self.mem_pot)
            else:
                self.mem_pot = self.P_rest
                self.pot_plot.append(self.mem_pot)

        self.out = self.output_spike(t)
        self.out_array.append(self.out)

    def update_threshold(self, th):
        self.P_thres = th