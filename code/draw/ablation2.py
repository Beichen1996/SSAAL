import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os
import matplotlib.font_manager as font_manager

from matplotlib.axes import Axes
import numpy as np
from PIL import Image
from subprocess import call
from collections import OrderedDict
import matplotlib.ticker as mticker
from matplotlib.ticker import FormatStrFormatter


sns.set()
sns.set_style("white")
def plt_props():
    plt.rcParams['font.size'] = 14
    plt.rcParams['axes.labelsize'] = 12
    plt.rcParams['font.style'] = 'normal'
    plt.rcParams['font.variant'] = 'normal' 
    plt.rcParams['xtick.labelsize'] = 12
    plt.rcParams['ytick.labelsize'] = 12
    plt.rcParams['legend.fontsize'] = 14
    plt.rcParams['figure.titlesize'] = 12
    plt.rcParams['figure.figsize'] = 6.2, 4.5
    plt.rcParams['lines.linewidth'] = 1.8
    plt.rcParams['lines.markersize'] = 6

m={}
m['700']='o'
m['500']='o'
m['300']='o'
m['100']='o'
m['random']='o'



BLEU4_ratios = [item for item in [2, 3, 4, 5, 6, 7, 8, 9]]

BLEU4_700 = [54.8,79.4,87.4,90.14,93.62,94.42,95.75,97.86]
BLEU4_700_error = [0, 0, 0, 0, 0, 0, 0, 0]

BLEU4_500 = [54.8,79.5,87.5,89.9,93.4,94.4,95.6,97.8]
BLEU4_500_error = [0, 0, 0, 0, 0, 0, 0, 0]

BLEU4_300 = [54.8,78.92,86.41,89.02,92.13,93.72,94.76,97]
BLEU4_300_error = [0, 0, 0, 0, 0, 0, 0, 0]

BLEU4_100 = [54.8,76.94,83.13,87.09,89.04,91.25,92.92,94.63]
BLEU4_100_error = [0, 0, 0, 0, 0, 0, 0, 0]

BLEU4_random = [54.8,75.34,81.56,85.92,88.31,90.7,92.13,93.1]
BLEU4_random_error = [0, 0, 0, 0, 0, 0, 0, 0]

fig, ax = plt.subplots(dpi=500)
plt_props()
#plt.rc('font',family='Times New Roman') 
BLEU4_700_plot = plt.plot(BLEU4_ratios, BLEU4_700, label='700-word', marker=m['700'])
BLEU4_500_plot = plt.plot(BLEU4_ratios, BLEU4_500, label='500-word', marker=m['500'])
BLEU4_300_plot = plt.plot(BLEU4_ratios, BLEU4_300, label='300-word', marker=m['300'])
BLEU4_100_plot = plt.plot(BLEU4_ratios, BLEU4_100, label='100-word',marker=m['100'])
BLEU4_random_plot = plt.plot(BLEU4_ratios, BLEU4_random, label='Random 500-word', marker=m['random'])


ax.yaxis.set_major_formatter(FormatStrFormatter('%.f'))
plt.legend(loc=4)

font1 = {'family' : 'Times New Roman',
'weight' : 'normal'
}

ax.set_xlim(1.5, 9.5)
ax.set_ylim(53, 100)
#plt.plot([], [], ' ', label= r"CIDEr for 100% data" 
#                            r"=113.5 ")
plt.legend(ncol=2, loc='lower right', prop=font1)
fig.tight_layout()
plt.xlabel('% of labeled data',font1, size = 15.5)
plt.ylabel('CIDEr',font1, size = 12)  
plt.title(' ')
plt.grid(True, color = 'gray', linewidth = 0.5)
fig.savefig('ablation2.pdf',dpi=600,format='pdf')

