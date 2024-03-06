#!/bin/bash

import numpy as np
import pandas as pd

sites = pd.read_csv('./CTCF_sites.bed', sep='\t', header=None)

f_chr = sites[sites[4] == "+"][0].values
f_start = sites[sites[4] == "+"][1].values
f_end = sites[sites[4] == "+"][2].values

r_chr = sites[sites[4] == "-"][0].values
r_start = sites[sites[4] == "-"][1].values
r_end = sites[sites[4] == "-"][2].values

with open("./con_pairs_ctcf.bedpe", "w") as output:
    for p in range(len(f_chr)):
        spaceStart = int(f_end[p]) + (50*1000)
        spaceEnd = int(f_end[p]) + (1*1000*1000)
        for m in range(len(r_chr)):
            if f_chr[p] == r_chr[m]:
                if spaceStart <= r_start[m] and r_end[m] <= spaceEnd:
                    output.write(f_chr[p], f_start[p], f_end[p], r_chr[m], r_start[m], r_end[m], sep='\t')
