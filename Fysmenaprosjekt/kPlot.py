# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 08:01:54 2018

@author: Erlendo
"""


import numpy as np
import matplotlib.pyplot as plt


energy_clean = [-17.881325, -18.387349, -18.440797, -18.441924, -18.443413, -18.442497]
force_clean = np.zeros(len(energy_clean))
pressure_clean = [6.790000, 1.240000, 0.420000, 0.370000, 0.320000, 0.340000]
bandgap_clean = [0.0, 0.0, 1.9662, 1.5019, 1.5325, 1.2297]
k = [1,2,3,4,5,6]

energy_o1 = [-20.197424, -20.415565, -20.423315, -20.425876, -20.425560, -20.425846]
force_o1 = [2.368, 2.294 , 2.348, 2.307, 2.317, 2.317]
pressure_o1 = [90.370000, 87.230000, 86.910000, 86.870000, 86.880000, 86.860000]
bandgap_o1 = [-2.2717, -2.2757, -1.905 , -2.0717 , -2.152, -2.1963]

energy_almostclose = [-19.812897, -20.048335, -20.048804, -20.048574, -20.048783, -20.049061]
force_almostclose = [5.593, 5.740, 5.765, 5.778, 5.779, 5.777]
pressure_almostclose = [155.080000, 150.040000, 149.820000, 149.810000, 149.810000, 149.810000]
bandgap_almostclose = [1.286, 1.0774, 1.1518, 1.1226, 1.1084, 1.1004]

rel_energy = np.zeros(len(energy_clean))
rel_force = np.zeros(len(energy_clean))
rel_pressure = np.zeros(len(energy_clean))
rel_bandgap = np.zeros(len(energy_clean))


for i in range(0, len(energy_clean)):
    rel_energy[i] = energy_almostclose[i]-energy_clean[i]
    rel_force[i] = force_almostclose[i]-force_clean[i]
    rel_pressure[i] = pressure_almostclose[i]-pressure_clean[i]
    rel_bandgap[i] = bandgap_almostclose[i]-bandgap_clean[i]
    
    
    
 
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2)

ax1.set_title('Relative Total energy')
ax1.plot(k, rel_energy, '-o') 

ax2.set_title('Bandgap')
ax2.plot(k, rel_bandgap, '-o')

ax3.set_title('Relative Pressure')
ax3.plot(k, rel_pressure, '-o')

ax4.set_title('Relative Force') 
ax4.plot(k, rel_force, '-x') 

plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
