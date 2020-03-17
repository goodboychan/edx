# -*- coding: utf-8 -*-
"""
Created on Fri May 26 22:19:06 2017

@author: kcsgo
"""

# Video 4.2.1
import pandas as pd

birddata = pd.read_csv("bird_tracking.csv")

birddata.head()

# Video 4.2.2
import matplotlib.pyplot as plt
import numpy as np

bird_names = pd.unique(birddata.bird_name)
plt.figure(figsize=(7,7))
for bird_name in bird_names:
    ix = birddata.bird_name == bird_name
    x, y = birddata.longitude[ix], birddata.latitude[ix]    
    plt.plot(x, y, ".", label=bird_name)
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.legend(loc="lower right")
plt.savefig("3traj.pdf")

# Video 4.2.3
ix = birddata.bird_name == "Eric"
speed = birddata.speed_2d[ix]
# plt.hist(speed) <- because of NaN, histogram is not generated
np.isnan(speed)
np.isnan(speed).any()

# How many NaNs in array
np.sum(np.isnan(speed))

ind = np.isnan(speed)
~ind

plt.hist(speed[~ind])

plt.figure(figsize=(8,4))
speed = birddata.speed_2d[birddata.bird_name == "Eric"]
ind = np.isnan(speed)
plt.hist(speed[~ind], bins=np.linspace(0, 30, 20), normed=True)
plt.xlabel("2D speed (m/s)")
plt.ylabel("Frequency")
plt.savefig("hist.pdf")

# Same feature in pandas
birddata.speed_2d.plot(kind='hist', range=[0, 30])
plt.xlabel("2D speed")
plt.ylabel("Frequency")
plt.savefig("pd_hist.pdf")

# video 4.2.4
import datetime

birddata.columns
birddata.date_time[0:3]

datetime.datetime.today()

time_1 = datetime.datetime.today()
time_2 = datetime.datetime.today()

time_2 - time_1

time_2 = datetime.datetime.today()

time_2 - time_1

date_str = birddata.date_time[0]
type(date_str)
date_str

# Remove end of string
date_str[:-3]

# convert string to data_time
datetime.datetime.strptime(date_str[:-3], "%Y-%m-%d %H:%M:%S")

timestamps = []
for k in range(len(birddata)):
    timestamps.append(datetime.datetime.strptime\
                      (birddata.date_time.iloc[k][:-3], "%Y-%m-%d %H:%M:%S"))

timestamps[0:3]

# Store data in pandas series
birddata["timestamp"] = pd.Series(timestamps, index = birddata.index)
birddata.head()

# Extract timestamp for eric
times = birddata.timestamp[birddata.bird_name == "Eric"]
elapsed_time = [time - times[0] for time in times]
plt.plot(np.array(elapsed_time) / datetime.timedelta(days=1))
plt.xlabel("Observation")
plt.ylabel("Elapsed time (days)")
plt.savefig("timeplot.pdf")
elapsed_time

elapsed_time[1000] / datetime.timedelta(days=1)
elapsed_time[1000] / datetime.timedelta(hours=1)

birddata.timestamp[4] - birddata.timestamp[3]

# Video 4.2.5
data = birddata[birddata.bird_name == "Eric"]
times = data.timestamp
elapsed_time = [time - times[0] for time in times]
elapsed_days = np.array(elapsed_time) / datetime.timedelta(days=1)

next_day = 1
inds = []
daily_mean_speed = []
for (i, t) in enumerate(elapsed_days):
    if t < next_day:
        inds.append(i)
    else:
        # Compute mean speed
        daily_mean_speed.append(np.mean(data.speed_2d[inds]))
        next_day += 1
        inds = []

plt.figure(figsize=(8,6))
plt.plot(daily_mean_speed)
plt.xlabel("Day")
plt.ylabel("Mean speed (m/s)")
plt.savefig("dms_Eric.pdf")

data = birddata[birddata.bird_name == "Nico"]
times = data.timestamp
elapsed_time = [time - times[19795] for time in times]
elapsed_days = np.array(elapsed_time) / datetime.timedelta(days=1)

next_day = 1
inds = []
daily_mean_speed = []
for (i, t) in enumerate(elapsed_days):
    if t < next_day:
        inds.append(i)
    else:
        # Compute mean speed
        daily_mean_speed.append(np.mean(data.speed_2d[inds]))
        next_day += 1
        inds = []

plt.figure(figsize=(8,6))
plt.plot(daily_mean_speed)
plt.xlabel("Day")
plt.ylabel("Mean speed (m/s)")
plt.savefig("dms_Nico.pdf")

data = birddata[birddata.bird_name == "Sanne"]
times = data.timestamp
elapsed_time = [time - times[40916] for time in times]
elapsed_days = np.array(elapsed_time) / datetime.timedelta(days=1)

next_day = 1
inds = []
daily_mean_speed = []
for (i, t) in enumerate(elapsed_days):
    if t < next_day:
        inds.append(i)
    else:
        # Compute mean speed
        daily_mean_speed.append(np.mean(data.speed_2d[inds]))
        next_day += 1
        inds = []

plt.figure(figsize=(8,6))
plt.plot(daily_mean_speed)
plt.xlabel("Day")
plt.ylabel("Mean speed (m/s)")
plt.savefig("dms_Sanne.pdf")

# Video 4.2.6
import cartopy.crs as ccrs
import cartopy.feature as cfeature

proj = ccrs.Mercator()

plt.figure(figsize=(10, 10))
ax = plt.axes(projection=proj)
ax.set_extent((-25.0, 20.0, 52.0, 10.0))

for name in bird_names:
    ix = birddata['bird_name'] == name
    x, y = birddata.longitude[ix], birddata.latitude[ix]
    ax.plot(x, y, '.', transform=ccrs.Geodetic(), label=name)
    
plt.legend(loc="upper left")
plt.savefig("map.pdf")

proj = ccrs.Mercator()

plt.figure(figsize=(10, 10))
ax = plt.axes(projection=proj)
ax.set_extent((-25.0, 20.0, 52.0, 10.0))
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linestyles=':')

for name in bird_names:
    ix = birddata['bird_name'] == name
    x, y = birddata.longitude[ix], birddata.latitude[ix]
    ax.plot(x, y, '.', transform=ccrs.Geodetic(), label=name)
    
plt.legend(loc="upper left")
plt.savefig("map_real.pdf")