# -*- coding: utf-8 -*-
"""
Created on Sat Jun 05 20:05:41 2021

v1.0 05/Jun/2021

@author: Yuan Wang (BG3MDO)

"""

import pandas as pd
import matplotlib.pyplot as plt

# Settings
csv_file = 'output_1.csv'
time_field = 'hh:mm:ss.ms'
#time_field = 'dd/mm/yyyy'
skip_data_line = 6500
fig_size_x = 12
fig_size_y = 6

# --------------------------------------------------------------
# Get data from CSV, and only keep temperature data
fields = [time_field, 'T[degC]']
df = pd.read_csv(csv_file, usecols=fields)
df = df.iloc[skip_data_line:]

# Format plot
ax = df.plot(title='Temperature Data Plot',
             x=time_field,
             figsize=(fig_size_x, fig_size_y), ylim=(0, 40))
plt.xticks(rotation=45)
ax.set_xlabel("Time")
ax.set_ylabel("Temperature [degC]")
plt.tight_layout()
plt.savefig("00_t_graph.svg")
plt.show()

# --------------------------------------------------------------
# Get data from CSV, and only keep Humidity data
fields = [time_field, 'rH[%]']
df = pd.read_csv(csv_file, usecols=fields)
df = df.iloc[skip_data_line:]

# Format plot
ax = df.plot(title='Humidity Data Plot',
             x=time_field,
             figsize=(fig_size_x, fig_size_y), ylim=(10, 90))
plt.xticks(rotation=45)
ax.set_xlabel("Time")
ax.set_ylabel("Humidity [%]")
plt.tight_layout()
plt.savefig("01_rh_graph.svg")
plt.show()

# --------------------------------------------------------------
# Get data from CSV, and only keep AccX/Y/Z data
fields = [time_field, 'accX[mg]', 'accY[mg]', 'accZ[mg]']
df = pd.read_csv(csv_file, usecols=fields)
df = df.iloc[skip_data_line:]

# Format plot
ax = df.plot(title='3-Axis Acceleration Data Plot',
             x=time_field,
             figsize=(fig_size_x, fig_size_y))
plt.xticks(rotation=45)
ax.set_xlabel("Time")
ax.set_ylabel("Acceleration [mg]")
plt.tight_layout()
plt.savefig("02_acc_graph.svg")
plt.show()

# --------------------------------------------------------------
# Get data from CSV, and only keep MagX/Y/Z data

fields = [time_field, 'magX[mG]', 'magY[mG]', 'magZ[mG]']
df = pd.read_csv(csv_file, usecols=fields)
df = df.iloc[skip_data_line:]

# Format plot
ax = df.plot(title='3-Axis Magnetometer Data Plot',
             x=time_field,
             figsize=(fig_size_x, fig_size_y), ylim=(-2000, 2000))
plt.xticks(rotation=45)
ax.set_xlabel("Time")
ax.set_ylabel("Magnetic Field [Mg]")
plt.tight_layout()
plt.savefig("03_mag_graph.svg")
plt.show()
