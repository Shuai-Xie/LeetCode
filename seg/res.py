import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

sns.set()
sns.set_style('whitegrid')


# sns.set_style('darkgrid')


def plt_props():
    plt.rcParams['font.size'] = 12
    plt.rcParams['axes.labelsize'] = 12
    plt.rcParams['font.family'] = 'serif'
    plt.rcParams['font.style'] = 'normal'
    plt.rcParams['font.variant'] = 'normal'
    plt.rcParams['xtick.labelsize'] = 12
    plt.rcParams['ytick.labelsize'] = 12
    plt.rcParams['legend.fontsize'] = 10
    plt.rcParams['figure.titlesize'] = 12
    plt.rcParams['figure.figsize'] = 6, 4
    plt.rcParams['lines.linewidth'] = 2.5
    plt.rcParams['lines.markersize'] = 8


# marker
m = {
    'DEAL': '^',
    'VAAL': 'o',
    'Core-set': '>',
    'Random': '*',
    'Dropout': 'd',
    'DBAL': 'p',
    'QBC': 'H',
    'Entropy': 's',
    'SA': ','
}

steps = list(range(10, 41, 5))

error_region = {
    'CamVid': {
        'level9_entropy':
            [50.64, 55.89, 56.61, 58.28, 59.90, 60.32, 60.76],
        'level9_enomask':
            [50.81, 56.57, 57.25, 59.80, 60.86, 61.36, 60.94],

        'level6_entropy':
            [50.12, 53.80, 56.37, 59.01, 60.45, 60.78, 61.49],  # baseline
        'level6_entropy_':
            [50.12, 55.31, 56.23, 58.01, 60.23, 60.44, 61.73],  # baseline
        'level6_enomask':
            [52.07, 53.79, 55.90, 58.93, 60.20, 60.78, 61.10],

        'level6_region_sum_':
            [50.12, 54.44, 55.65, 57.45, 58.59, 60.43, 60.84],

        'map_sum':
            [50.12, 55.26, 56.72, 57.88, 59.95, 60.69, 61.56],

    },
    'Cityscapes': {
        'level9_score':
            [53.55, 58.26, 60.06, 62.95, 63.74, 65.05, 65.29],
        'level9_entropy':
            [50.69, 54.40, 57.34, 58.24, 59.06, 58.84, 60.49],
        'Entropy':
            [50.49, 55.25, 56.24, 59.23, 60.74, 60.73, 61.84],

        'map_sum':
            [50.49, 57.74, 60.94, 62.18]
    }
}

Cityscapes = {
    'no_weight': {
        '701': [52.45, 58.50, 60.28],
        '100': [],
        '200': [],
        '300': [],
        '400': []
    },
    'Core-set': {
        '701': [50.39, 53.41, 54.78, 56.70, 58.28, 57.59],
        '100': [],
        '200': [],
    },
    'Entropy': {
        '701': [50.49, 55.25, 56.24, 59.23, 60.15, 60.74, 61.84],
    },
    'Dropout': {
        '701': [51.00, 54.95, 57.16, 58.41, 58.79, 59.71, 60.80],
    },
    'Random': {
        '701': [50.53, 54.39, 56.13, 57.50, 57.63, 58.64, 60.02],
    }
}

# read from txt
gamma = {
    'ori': {
        '10': [0, ]
    }
}

# no class weight
evals = {
    'CamVid': {
        'mIoUs': {
            'DEAL':
                [50.64, 55.89, 56.72, 58.28, 59.95, 60.69, 61.49],  # region_entropy, level=9
            'VAAL':
                [50.55, 55.31, 56.00, 57.68, 58.73, 60.15, 60.74],
            'Core-set':
                [50.75, 55.16, 56.13, 57.95, 58.26, 60.05, 60.66],
            'Entropy':
                [50.05, 52.69, 55.92, 57.08, 58.88, 59.79, 60.47],
            'Dropout':
                [50.42, 52.77, 56.01, 57.86, 59.23, 60.11, 60.28],
            'Random':
                [50.20, 52.29, 55.34, 56.89, 58.05, 59.24, 59.86],
        },
        'full': 64.61,
    },
    'Cityscapes': {  # level6_region_sum = [53.7,56.6,58.59,59.43,60.46]
        'mIoUs': {
            'DEAL':
                [50.50, 57.74, 60.94, 62.18, 63.67, 64.39, 65.00],
            'D':
                [52.45, 58.50, 60.28],
            'Entropy':
                [50.49, 55.25, 56.24, 59.23, 60.15, 60.74, 61.84],
            'Core-set':
                [50.39, 53.41, 54.78, 56.70, 58.28, 57.59],
            'Dropout':
                [51.00, 54.95, 57.16, 58.41, 58.79, 59.71, 60.80],
            'Random':
                [50.53, 54.39, 56.13, 57.50, 57.63, 58.64, 60.02],
        },
        'full': 65.12
    }
}

evals_weight = {
    'CamVid': {
        'mIoUs': {
            'DEAL':
                [53.26, 56.53, 58.50, 59.33, 60.52, 61.28, 61.72],  # region ratio
            'VAAL':
                [53.25, 56.12, 58.13, 59.07, 59.96, 60.50, 61.28],
            'Core-set':
                [53.25, 56.00, 58.05, 58.87, 59.66, 60.42, 60.98],
            'Entropy':
                [53.27, 55.97, 57.13, 58.72, 60.24, 60.98, 61.07],
            'Dropout':
                [53.26, 55.86, 56.89, 58.50, 59.17, 60.83, 61.06],
            'Random':
                [53.20, 55.29, 57.23, 58.19, 58.88, 59.24, 60.28],
        },
        'full': 65.33
    },
    'Cityscapes': {
        'mIoUs': {
            'DEAL':
                [54.22, 57.72, 60.50, 62.04, 62.62, 63.15, 63.72],  # region ratio
            'VAAL':
                [54.02, 57.42, 59.49, 61.11, 61.85, 62.71, 63.15],
            'Core-set':
                [53.87, 57.27, 58.59, 60.81, 61.75, 62.63, 63.21],
            'Entropy':
                [54.17, 57.32, 60.23, 61.78, 62.34, 62.89, 63.38],
            'Dropout':
                [53.92, 57.41, 58.79, 59.75, 61.49, 62.90, 63.02],
            'Random':
                [53.84, 57.12, 59.25, 59.99, 61.30, 61.33, 61.87],
        },
        'full': 65.81
    }
}


def plt_results(data, full_upper, title):
    # plt.figure(dpi=500)  # 3200x2400
    plt.figure(dpi=300)
    plt_props()  # 设置 props
    plt.title(title)

    percent = int(data['DEAL'][-1] / full_upper * 100)

    plt.plot([10, 40], [data['DEAL'][-1], data['DEAL'][-1]],
             linestyle='--', color='gray', linewidth=1.5,
             label=f"{percent}% - Full data ({full_upper})")  # $ latex 数学公式
    for method, evals in data.items():
        plt.plot(steps, evals, marker=m[method], linestyle='-', label=method)

    # plt.hlines(y=data['DEAL'][-1], xmin=10, xmax=40, colors='gray', linestyles='--',
    #            label=f"{percent}% - Full data")
    # plt.text(10.3, full_upper - 1.5, s=f'Full data\n{full_upper}')

    plt.legend(ncol=2, loc='lower right')  # 两列
    plt.xlabel('% of Labeled Data')
    plt.ylabel('mIoU')
    plt.show()


if __name__ == '__main__':
    dataset = 'Cityscapes'
    # dataset = 'CamVid'
    # eva = evals
    eva = evals_weight
    plt_results(eva[dataset]['mIoUs'], eva[dataset]['full'], title=dataset)
