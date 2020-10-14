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

altuvestats = {}
altuvestats['BA'] = cheat['avg']
altuvestats['OBP'] = cheat['obp']
altuvestats['SLG'] = cheat['slg']
altuvestats['OPS'] = cheat['obp']

altuvestats1 = {}
altuvestats1['BA'] = nocheat['avg']
altuvestats1['OBP'] = nocheat['obp']
altuvestats1['SLG'] = nocheat['slg']
altuvestats1['OPS'] = nocheat['obp']

width = 0.35
x = np.arange(len(altuvestats.keys()))
fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, altuvestats.values(), width, label='cheat',color='red')
rects2 = ax.bar(x + width/2, altuvestats1.values(), width, label='nocheat',color='green')

ax.set_xlabel('Hitting Measures')
ax.set_ylabel('Statistics')
ax.set_xticks(x)
ax.set_xticklabels(altuvestats.keys())
ax.legend()
plt.title("Jose Altuve's Hitting Stats - 2017 vs. 2020")

plt.show()