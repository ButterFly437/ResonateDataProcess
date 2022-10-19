import data, draw
import math, os

def out(info: str='', *args, **kwargs):
    if 'file' not in kwargs:
        print(info, *args, **kwargs)
    else:
        with open(kwargs['file'], 'a') as f:
            f.write(info)

# 固有周期
T_0_bar = sum(data.LAB1) / len(data.LAB1)
out(f'T0_bar: {round(T_0_bar, 3)} s')

# 阻尼系数
tmp = data.LAB2['Z1']['10T'] / 10
out("\nln Θ: ")
out("阻尼1:\t", end='')
for i in data.LAB2['Z1']['data']:
    i[0] *= tmp;
    i.append(math.log(i[1]))
    out(f'{round(i[2], 3)}\t', end="")
out()
tmp = data.LAB2['Z3']['10T'] / 10
out("阻尼3:\t", end='')
for i in data.LAB2['Z3']['data']:
    i[0] *= tmp;
    i.append(math.log(i[1]))
    out(f'{round(i[2], 3)}\t', end="")
out()

out('\n幅频、相频特性曲线: ')
omega_0 = math.pi * 2 / T_0_bar
out(f'固有频率: {round(omega_0, 3)} Hz')
out(f'omega/omega_0: ')
out('阻尼1:\t', end='')
for i in data.LAB3['Z1']['data']:
    rate = math.pi * 2 / i[2] / omega_0
    i.append(rate)
    out(f'{round(rate, 3)}\t', end='')
out()
out('阻尼3:\t', end='')
for i in data.LAB3['Z3']['data']:
    rate = math.pi * 2 / i[2] / omega_0
    i.append(rate)
    out(f'{round(rate, 3)}\t', end='')
out()

# 图片
# 抽取
lab3_z1 = [[], [], [], []]
for i in data.LAB3['Z1']['data']:
    lab3_z1[0].append(i[0])
    lab3_z1[1].append(i[1])
    lab3_z1[2].append(round(i[3],3))
    lab3_z1[3].append(round(math.pi * 2 / i[2], 3))

lab3_z3 = [[], [], [], []]
for i in data.LAB3['Z3']['data']:
    lab3_z3[0].append(i[0])
    lab3_z3[1].append(i[1])
    lab3_z3[2].append(round(i[3],3))   
    lab3_z3[3].append(round(math.pi * 2 / i[2], 3))
OUTPUT_DIR = './outputs'
# 检查文件夹是否存在
if not os.path.isdir(OUTPUT_DIR):
    os.mkdir(OUTPUT_DIR)
draw.draw_smooth(os.path.join(OUTPUT_DIR, '受迫振动的幅频特性.png'), lab3_z1[2], lab3_z1[1], 'ω/ω0', 'θ', '受迫振动的幅频特性',
    x_other=lab3_z3[2], y_other=lab3_z3[1], line1_legend='阻尼1', line2_legend='阻尼3', grid=True, factor=0.03)
draw.draw_smooth(os.path.join(OUTPUT_DIR, '受迫振动的幅频特性.svg'), lab3_z1[2], lab3_z1[1], 'ω/ω0', 'θ', '受迫振动的幅频特性',
    x_other=lab3_z3[2], y_other=lab3_z3[1], line1_legend='阻尼1', line2_legend='阻尼3', grid=True, factor=0.03)
draw.draw_smooth(os.path.join(OUTPUT_DIR, '受迫振动的相频特性.png'), lab3_z1[3], lab3_z1[0], 'ω', 'θ', '受迫振动的相频特性',
    x_other=lab3_z3[3], y_other=lab3_z3[0], line1_legend='阻尼1', line2_legend='阻尼3', grid=True, factor=0.02)
draw.draw_smooth(os.path.join(OUTPUT_DIR, '受迫振动的相频特性.svg'), lab3_z1[3], lab3_z1[0], 'ω', '', '受迫振动的相频特性',
    x_other=lab3_z3[3], y_other=lab3_z3[0], line1_legend='阻尼1', line2_legend='阻尼3', grid=True, factor=0.02)