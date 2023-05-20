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

'''
BLEU4_ratios = [item for item in [2, 3, 4, 5, 6, 7, 8, 9]]
BLEU4_coreset = [18.9, 24, 25, 25.9, 27, 27.5, 27.9, 28.8]
BLEU4_coreset_error = [0, 0, 0, 0, 0, 0, 0, 0]
BLEU4_SSAAL = [18.9, 27.5, 29.5, 29.7, 30.8, 31.3, 31.6, 32.1]
BLEU4_SSAAL_error = [0, 0, 0, 0, 0, 0, 0, 0]
BLEU4_Multilabel = [18.9, 25.6, 26.7, 27.4, 28.1, 28.7, 29.1, 29.9]
BLEU4_Multilabel_error = [0, 0, 0, 0, 0, 0, 0, 0]
BLEU4_VAAL = [18.9, 23.5, 25.2, 26, 26.5, 27, 27.5, 28.2]
BLEU4_VAAL_error = [0, 0, 0, 0, 0, 0, 0, 0]
BLEU4_random = [18.9, 21, 22, 23.1, 24.4, 25.6, 26.2, 26.6]
BLEU4_random_error = [0, 0, 0, 0, 0, 0, 0, 0]
'''

BLEU4_ratios = [item for item in [2, 3, 4, 5, 6, 7, 8, 9]]
BLEU4_coreset = [18.9, 24, 25, 25.9, 27, 27.5, 27.9, 28.8]

BLEU4_coreset_error = [0, 0, 0, 0, 0, 0, 0, 0]
BLEU4_SSAAL = [18.9, 27.5, 29.5, 29.7, 30.8, 31.3, 31.6, 32.1]
BLEU4_SSAAL_error = [0, 0, 0, 0, 0, 0, 0, 0]
BLEU4_Multilabel = [18.9, 25.6, 26.7, 27.4, 28.1, 28.7, 29.1, 29.9]
BLEU4_Multilabel_error = [0, 0, 0, 0, 0, 0, 0, 0]
BLEU4_VAAL = [18.9, 23.5, 25.2, 26, 26.5, 27, 27.5, 28.2]
BLEU4_VAAL_error = [0, 0, 0, 0, 0, 0, 0, 0]
#BLEU4_random = [18.9, 21, 22, 23.1, 24.4, 25.6, 26.2, 26.6]
BLEU4_random = [18.9, 22, 22.6, 23.7, 24.8, 25.6, 26.2, 26.6]
BLEU4_random_error = [0, 0, 0, 0, 0, 0, 0, 0]

for i in range(1,8):
    BLEU4_coreset[i] += 0.35
    BLEU4_VAAL[i] += 0.35
    BLEU4_Multilabel[i] += 0.4
    BLEU4_random[i] += 0.65


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
ax.set_ylim(15, 34)
#plt.plot([], [], ' ', label= r"BLEU for 100% data"    r"=36.2 ")
plt.legend(ncol=2, loc='lower right', prop=font1)
fig.tight_layout()
plt.xlabel('% of labeled data',font1, size = 15.5)
plt.ylabel('BLEU4',font1, size = 12)  
plt.text(4.9, 15+19*0.95 , r"BLEU4 for 100% labeled data = 36.2 ", size = 14.5) 
plt.title(' ')
plt.grid(True, color = 'gray', linewidth = 0.5)
fig.savefig('BLEU.pdf',dpi=600,format='pdf')

