import matplotlib.pyplot as plt
import numpy as np

steps = list(range(10, 41, 5))

eval_mIoUs = {
    'error_mask_ceal': [52.43, 60.81, 61.89, 62.69, 62.79, 62.98, 63.35],  # 12h17m47s
    'error_mask': [52.44, 61.11, 62.31, 64.02, 64.48, 64.81, 63.64],  # 9h46m39s
    'random': [51.95, 54.05, 56.21, 55.96, 57.71, 58.74, 60.12],  # 1h37m16s
    'softmax_confidence': [52.05, 54.74, 55.19, 57.47, 58.83, 59.08, 59.46],  # 2h36m54s
    'softmax_entropy': [51.85, 55.85, 55.77, 57.32, 59.41, 59.70, 60.64],  # 2h5m35s
    'mc_dropout_entropy': [52.01, 54.84, 55.88, 57.17, 58.59, 59.55, 61.13],  # 1h30m16s，应该更慢一些
    'core-set': [52.35, 53.59, 56.34, 57.61, 59.05, 58.54, 59.83],
    'ceal': [52.23, 57.21, 55.67, 58.87, 59.91, 60.88, 61.74],
}


def plt_results():
    plt.figure()
    plt.grid()
    plt.title('CamVid')

    for method, evals in eval_mIoUs.items():
        plt.plot(steps, evals, '-', label=method)

    plt.hlines(y=62.85, xmin=10, xmax=40, colors='black', linestyles='--')
    plt.text(10.3, 63, s='Full data')

    plt.xlabel('% of Labeled Data')
    plt.ylabel('mIoU')
    plt.legend(loc='best')
    plt.show()


plt_results()
