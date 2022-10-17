from typing import List, Union
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

def draw_smooth(   
        filepath: str, 
        x: List[Union[int, float]], y: List[Union[int, float]], 
        x_label: str, y_label: str, 
        label: str, 
        x_start: float=None, x_end: float=None, x_total: int=1000, 
        show: bool=False,
        x_other: List[Union[int, float]]=None, y_other: List[Union[int, float]]=None,
        line1_legend: str='line1', line2_legend: str='line2', grid: bool=False, factor: float=0.01):
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    
    plt.title(label)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    
    if x_start is None:
        if x_other is not None:
            ave = (sum(x) + sum(x_other)) / (len(x) + len(x_other)) if len(x) + len(x_other) != 0 else 0
            x_start = min(min(x, x_other))
            x_start = x_start - (ave - x_start) * factor
        else:
            ave = (sum(x)) / (len(x)) if len(x) != 0 else 0
            x_start = min(x, x_other)
            x_start = x_start - (ave - x_start) * factor
    if x_end is None:
        if x_other is not None:
            ave = (sum(x) + sum(x_other)) / (len(x) + len(x_other)) if len(x) + len(x_other) != 0 else 0
            x_end = max(max(x, x_other))
            x_end = x_end + (ave - x_start) * factor
        else:
            ave = (sum(x)) / (len(x)) if len(x) != 0 else 0
            x_end = max(x, x_other)
            x_end = x_end + (ave - x_start) * factor

    xc = np.linspace(x_start, x_end, x_total)

    
    
    node1State = np.array(y)
    times = np.array(x)

    if grid:
        plt.grid(True, which='both', linestyle='-.')

    model0 = make_interp_spline(times, node1State)
    ys0 = model0(xc)
    ys1 = None
    ns = None
    tms = None
    if x_other is not None and y_other is not None:
        ns = np.array(x_other)
        tms = np.array(y_other)
        model1 = make_interp_spline(ns, tms)
        ys1 = model1(xc)
    plt.plot(xc, ys0, color='black')
    plt.scatter(times, node1State, marker='o', label=line1_legend, c='black')
    if ys1 is not None:
        plt.plot(xc, ys1, color='black')
        plt.scatter(ns, tms, marker='*', label=line2_legend, c='black')

    plt.legend()
    if filepath is not None:
        plt.savefig(filepath, dpi=600)
    if show:
        plt.show()
    plt.clf()
    plt.cla()