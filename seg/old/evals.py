import matplotlib.pyplot as plt
import numpy as np

# step=5 存在引入不稳定，因为每次引入的数据量太少了?
# 但是 step=10 同样 percent 数据，性能要低于 step=5
steps = list(range(10, 41, 5))

evals = {
    'CamVid': {
        'mIoUs': {
            'error': [53.26, 56.53, 58.50, 59.33, 60.52, 61.28, 61.72],  # region ratio
            'softmax_entropy': [53.27, 55.97, 57.13, 58.72, 60.24, 60.98, 61.07],
            'core-set': [53.25, 56.00, 58.05, 58.87, 59.66, 60.42, 60.98],
            'mc_dropout': [53.26, 55.86, 56.89, 58.50, 59.17, 60.83, 61.06],
            'random': [53.20, 55.29, 57.23, 58.19, 58.88, 59.24, 60.28],
        },
        'full': 65.33
    },
    'Cityscapes': {
        'mIoUs': {
            'error': [54.22, 57.72, 60.50, 62.04, 62.62, 63.15, 64.23],  # region ratio
            'softmax_entropy': [54.17, 57.32, 60.23, 61.78, 62.34, 62.89, 63.02],
            'core-set': [53.87, 57.27, 58.59, 60.81, 61.75, 63.23, 63.71],
            'mc_dropout': [53.92, 57.41, 58.79, 59.75, 61.49, 62.90, 63.88],
            'random': [53.84, 57.12, 59.25, 59.99, 61.30, 61.33, 61.87],
        },
        'full': 65.81
    }
}


def plt_results(data, full_upper, title):
    plt.figure(figsize=(6, 6))
    plt.grid()
    plt.title(title)

    for method, evals in data.items():
        plt.plot(steps, evals, '-', label=method)

    plt.hlines(y=full_upper, xmin=10, xmax=40, colors='black', linestyles='--')
    plt.text(10.3, full_upper - 0.8, s=f'Full data\n{full_upper}')

    plt.xlabel('% of Labeled Data')
    plt.ylabel('mIoU')
    plt.legend(loc='lower right')
    plt.show()


if __name__ == '__main__':
    dataset = 'Cityscapes'
    # dataset = 'CamVid'
    plt_results(evals[dataset]['mIoUs'], evals[dataset]['full'], dataset)
