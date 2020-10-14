import json
import matplotlib
import numpy as np
from matplotlib import pyplot as plt

with open('altuve2017.json', 'r') as altuve_2017:
    whenhecheat = altuve_2017.read()
with open('altuve2020.json', 'r') as altuve_2020:
    whenhenocheat = altuve_2020.read()
cheat = json.loads(whenhecheat)
nocheat = json.loads(whenhenocheat)

sabermetrics = {}
sabermetrics['BA'] = cheat['avg']
sabermetrics['OBP'] = cheat['obp']
sabermetrics['SLG'] = cheat['slg']
sabermetrics['OPS'] = cheat['obp']

sabermetrics1 = {}
sabermetrics1['BA'] = nocheat['avg']
sabermetrics1['OBP'] = nocheat['obp']
sabermetrics1['SLG'] = nocheat['slg']
sabermetrics1['OPS'] = nocheat['obp']

width = 0.35
x = np.arange(len(sabermetrics.keys()))
fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, sabermetrics.values(), width, label='cheat',color='red')
rects2 = ax.bar(x + width/2, sabermetrics1.values(), width, label='nocheat',color='green')

ax.set_xlabel('Core Hitting Stat Categories')
ax.set_ylabel('Statistics')
ax.set_xticks(x)
ax.set_xticklabels(sabermetrics.keys())
ax.legend()
plt.title("Jose Altuve's Hitting Stats - 2017 vs. 2020")
params['font.family'] = 'fantasy'

plt.show()