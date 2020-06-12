#!/usr/bin/env python3

import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

# custom plot colors
GLD = [1.0, 0.698, 0.063]

# read in data
df = pd.read_csv(r'./data/Baltimore_City_Employees_Salaries.csv')

# included years in data, shorten FY20XX to FYXX
years = df['FiscalYear'].unique()
years = sorted(years)
yrs = [year[4:] for year in years]

# total gross pay in billions
gross_sum = [df.loc[df['FiscalYear']==year,'GrossPay'].sum() for year in years]
gross_sum_billion = np.array(gross_sum)/1E9

fig, ax = plt.subplots(nrows=1, ncols=1)
fig.patch.set_facecolor('k')
ax.set_facecolor('k')
ax.plot(yrs, gross_sum_billion, color=GLD, linewidth=5, marker='o', markersize='15')

ax.set_xlabel('Fiscal Year', color='w', fontsize=16)
ax.set_ylabel('Billions of US Dollars', color='w', fontsize=16)
ax.set_title('Baltimore City Total Employees Gross Pay', color='w', fontsize=16, fontweight='bold')

# Set the borders to a given color...
ax.tick_params(color='w', labelcolor='w', size=10.0, labelsize=14, width=3, direction='in')
for spine in ax.spines.values():
    spine.set_edgecolor('w')
    spine.set_linewidth(3.0)

plt.show()