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
m['SSAAL']='o'
m['Multilabel']='o'
m['VAAL']='o'
m['Random']='o'
m['Coreset']='o'




BLEU4_ratios = [item for item in [2, 3, 4, 5, 6, 7, 8, 9]]
BLEU4_coreset = [54.8,75.7,80.02,82.22,84.64,86.56,89,90.34]
BLEU4_coreset_error = [0, 0, 0, 0, 0, 0, 0, 0]
BLEU4_SSAAL = [54.8,79.5,87.5,89.9,93.4,94.4,95.6,97.8]
BLEU4_SSAAL_error = [0, 0, 0, 0, 0, 0, 0, 0]
BLEU4_Multilabel = [54.8,76.34,82.83,86.85,88.94,90.51,92.41,94.13]
BLEU4_Multilabel_error = [0, 0, 0, 0, 0, 0, 0, 0]
BLEU4_VAAL = [54.8,74.4,78.92,81.23,83.98,86.43,88.17,89.54]
BLEU4_VAAL_error = [0, 0, 0, 0, 0, 0, 0, 0]
BLEU4_random = [54.8,70.78,74.87,77.53,80.94,83.37,85.15,86.86]
BLEU4_random_error = [0, 0, 0, 0, 0, 0, 0, 0]

fig, ax = plt.subplots(dpi=500)
plt_props()
#plt.rc('font',family='Times New Roman') 
BLEU4_SSAAL_plot = plt.plot(BLEU4_ratios, BLEU4_SSAAL, label='SSAAL', marker=m['SSAAL'] )
BLEU4_Multilabel_plot = plt.plot(BLEU4_ratios, BLEU4_Multilabel, label='Multi-label', marker=m['Multilabel'])
BLEU4_coreset_plot = plt.plot(BLEU4_ratios, BLEU4_coreset, label='Core-set', marker=m['Coreset'])
BLEU4_VAAL_plot = plt.plot(BLEU4_ratios, BLEU4_VAAL, label='VAAL',marker=m['VAAL'])
BLEU4_random_plot = plt.plot(BLEU4_ratios, BLEU4_random, label='Random', marker=m['Random'])


ax.yaxis.set_major_formatter(FormatStrFormatter('%.f'))
plt.legend(loc=4)

font1 = {'family' : 'Times New Roman',
'weight' : 'normal'
}

ax.set_xlim(1.5, 9.5)
ax.set_ylim(53, 110)
#plt.plot([], [], ' ', label= r"CIDEr for 100% data"  r"=113.5 ")
plt.legend(ncol=2, loc='lower right', prop=font1)
fig.tight_layout()
plt.xlabel('% of labeled data',font1, size = 15.5)
plt.ylabel('CIDEr',font1, size = 12) 
plt.text(4.9, 53+57*0.95 , r"CIDEr for 100% labeled data = 113.5 ", size = 14.5) 
plt.title(' ')
plt.grid(True, color = 'gray', linewidth = 0.5)
fig.savefig('CIDEr.pdf',dpi=600,format='pdf')

