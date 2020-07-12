import matplotlib.pyplot as plt
import numpy as np

# step=5 存在引入不稳定，因为每次引入的数据量太少了?
# 但是 step=10 同样 percent 数据，性能要低于 step=5
steps = list(range(10, 41, 5))

eval_mIoUs_bs8 = {
    'error_mask_ceal': [52.43, 60.81, 61.89, 62.69, 62.79, 62.98, 63.35],  # 12h17m47s
    'error_mask': [52.44, 61.11, 62.31, 64.02, 64.48, 64.81, 63.64],  # 9h46m39s
    'error_image_human': [52.29, 54.96, 56.25, 56.18, 59.31, 60.61, 60.47],
    'error_image_target': [52.25, 55.20, 57.08, 56.79, 59.02, 60.51, 60.30],
    'random': [51.95, 54.05, 56.21, 55.96, 57.71, 58.74, 60.12],  # 1h37m16s
    'softmax_confidence': [52.05, 54.74, 55.19, 57.47, 58.83, 59.08, 59.46],  # 2h36m54s
    'softmax_entropy': [51.85, 55.85, 55.77, 57.32, 59.41, 59.70, 60.64],  # 2h5m35s
    'mc_dropout_entropy': [52.01, 54.84, 55.88, 57.17, 58.59, 59.55, 61.13],  # 1h30m16s，应该更慢一些
    'core-set': [52.35, 53.59, 56.34, 57.61, 59.05, 58.54, 59.83],
    'ceal': [52.23, 57.21, 55.67, 58.87, 59.91, 60.88, 61.74],
}
full_bs8 = 62.85

eval_mIoUs_bs4 = {
    # 'error_image_human': [54.22, 56.84, 58.95, 59.20, 60.72, 61.10, 62.63],
    # 'error_coreset': [54.23, 57.29, 57.61, 59.34, 60.42, 61.36, 62.32],
    'error_level': [54.25, 56.53, 58.50, 59.33, 60.52, 61.28, 61.72],  # region ratio
    'core-set': [53.25, 56.00, 58.05, 58.87, 59.66, 60.42, 60.98],
    'softmax_entropy': [53.27, 55.97, 57.13, 58.72, 60.24, 60.98, 61.07],
    'mc_dropout_entropy': [53.26, 55.86, 56.89, 58.50, 59.17, 60.83, 61.06],
    'random': [53.20, 55.29, 57.23, 58.19, 58.88, 59.24, 60.28],
}
full_bs4 = 65.33


def plt_results(data, full_upper):
    plt.figure(figsize=(6, 6))
    plt.grid()
    plt.title('CamVid')

    for method, evals in data.items():
        plt.plot(steps, evals, '-', label=method)

    plt.hlines(y=full_upper, xmin=10, xmax=40, colors='black', linestyles='--')
    plt.text(10.3, full_upper - 0.8, s=f'Full data\n{full_upper}')

    plt.xlabel('% of Labeled Data')
    plt.ylabel('mIoU')
    plt.legend(loc='lower right')
    plt.show()


pam_class = {
    # 'region_size': [54.01, 56.24, 58.44, 57.46, 59.91, 59.72, 61.03],  # human 不稳定
    'region_mean': [54.02, 57.13, 58.06, 58.68, 59.52, 60.13, 61.35],  # target
    'region_sum': [54.33, 56.68, 57.21, 58.70, 60.18, 61.17, 61.37],  # target
    'region_level': [54.14, 56.53, 58.50, 59.33, 60.52, 61.28, 61.72],  # region ratio
}

pam_noclass = {  # target > human，但前期不是很稳定
    'region_ratio': [53.32, 56.01, 57.08, 58.77, 59.69, 60.42, 62.16],  # error_size / valid_size
}


def plt_pam(data):
    plt.figure(figsize=(6, 6))
    plt.grid()
    plt.title('CamVid')

    for method, evals in data.items():
        plt.plot(steps, evals, '-', label=method)

    plt.xlabel('% of Labeled Data')
    plt.ylabel('mIoU')
    plt.legend(loc='lower right')
    plt.show()


if __name__ == '__main__':
    plt_results(eval_mIoUs_bs4, full_bs4)
    # plt_pam(pam_class)
