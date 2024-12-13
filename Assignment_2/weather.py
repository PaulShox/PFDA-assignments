# Import Pandas
import pandas as pd

# Import Matplotlib
import matplotlib.pyplot as plt

# Import Numpy
import numpy as np

# Import mplcursors https://mplcursors.readthedocs.io/en/stable/index.html
import mplcursors # https://www.youtube.com/watch?v=n5djATE1TJk


weather = pd.read_csv('weatherreadings1.csv')

temps = weather[['reportStartDateTime', 'dryBulbTemperature_Celsius']]
temps['reportStartDateTime'] = pd.to_datetime(temps['reportStartDateTime'])
temps['reportStartDateTime'] = temps['reportStartDateTime'].dt.strftime('%m-%d %H:%M')

x = temps['reportStartDateTime']
y = temps['dryBulbTemperature_Celsius']
mean_y = np.mean(y)

plt.style.use('ggplot') 
fig, ax = plt.subplots()

ax.plot(x, y,)
ax.scatter(x, y)

ax.set_title('Dry Bulb Temperature', pad=20, fontsize=18, fontweight='bold')
ax.set_xlabel('Date_Time', fontsize=14, fontweight='bold')
ax.set_ylabel('Temperature (Celsius)', fontsize=14, fontweight='bold')

ax.annotate('Highest Temp - 15.94', (0, 16), xytext=(4, 16), arrowprops=dict(facecolor='black', shrink=0.1, width=2))
ax.annotate('Lowest Temp - 9.17', (31, 9.17), xytext=(31, 10.2), arrowprops=dict(facecolor='black', shrink=0.1, width=2))
ax.annotate('Mean Temp - 11.68', (75, 11.68), xytext=(78, 12.5), arrowprops=dict(facecolor='blue', shrink=0.1, width=2))

plt.axhline(y=mean_y, color='b', linestyle='--', linewidth=2) # https://www.statology.org/matplotlib-average-line/

labels = ax.get_xticklabels()
plt.setp(labels, rotation=45, horizontalalignment='right')

mplcursors.cursor(hover=True)
plt.show()




