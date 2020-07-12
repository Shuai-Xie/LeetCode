import numpy as np
from typing import List

stats = {
    'CamVid': {
        'label': np.array([
            'Sky', 'Building', 'Pole', 'Road', 'Sidewalk',
            'Tree', 'SignSymbol', 'Fence', 'Car', 'Pedestrian', 'Bicyclist'
        ]),
        # 'IoUs': np.array([
        #     0.920, 0.830, 0.319, 0.946, 0.814,
        #     0.758, 0.465, 0.536, 0.837, 0.588, 0.540
        # ]),
        'IoUs': np.array([  # class balance
            0.89483721, 0.80967903, 0.27588851, 0.9398972, 0.79933637, 0.74785056,
            0.40022362, 0.35422778, 0.84925054, 0.48538636, 0.55030455
        ]),
        'weights': np.array([
            0.16974727, 0.25941378, 0.01060619, 0.31062463, 0.07429441, 0.11992445,
            0.01154664, 0.01529717, 0.01529717, 0.00752117, 0.00572713
        ]),
        'pixel_num': np.array([7.6801e+07, 1.1737e+08, 4.7987e+06, 1.4054e+08, 3.3614e+07, 5.4259e+07,
                               5.2242e+06, 6.9211e+06, 6.9211e+06, 3.4029e+06, 2.5912e+06])
    },
    'Cityscapes': {
        'label': np.array([
            'Road', 'Sidewalk', 'Building', 'Wall', 'Fence', 'Pole',
            'Traffic Light', 'Traffic Sign', 'Vegetation', 'Terrain', 'Sky', 'Person',
            'Rider', 'Car', 'Truck', 'Bus', 'Train', 'Motorcycle', 'Bicycle'
        ]),
        # 'IoUs': np.array([
        #     0.986, 0.861, 0.935, 0.561, 0.633, 0.697,
        #     0.773, 0.813, 0.939, 0.729, 0.957, 0.873,
        #     0.729, 0.962, 0.768, 0.894, 0.865, 0.722, 0.782
        # ]),
        'IoUs': np.array([  # class balance
            0.96413158, 0.75359974, 0.87452248, 0.54463887, 0.48679499, 0.43315336,
            0.44392774, 0.59287381, 0.88387547, 0.56281888, 0.92183063, 0.67347566,
            0.47212327, 0.90051574, 0.61459615, 0.71296687, 0.64136085, 0.4425265, 0.58391299
        ]),
        'weights': np.array([
            0.36818503, 0.06110975, 0.22915053, 0.0066211, 0.0089994, 0.01229112,
            0.00208626, 0.00558671, 0.15847435, 0.01161756, 0.04019395, 0.01211275,
            0.0013659, 0.06989223, 0.00265074, 0.00228052, 0.00228782, 0.00094368, 0.00415061
        ]),
        'pixel_num': np.array([4.57384017e+08, 7.59146090e+07, 2.84666084e+08, 8.22516700e+06,
                               1.11796540e+07, 1.52688540e+07, 2.59169700e+06, 6.94019000e+06,
                               1.96867412e+08, 1.44321050e+07, 4.99316040e+07, 1.50472700e+07,
                               1.69680900e+06, 8.68247950e+07, 3.29292300e+06, 2.83300800e+06,
                               2.84208500e+06, 1.17230700e+06, 5.15615900e+06]),
    },
}

import matplotlib.pylab as plt


# exponential moving average
def smooth_ema(scalars: List[float], weight: float) -> List[float]:  # Weight between 0 and 1
    last = scalars[0]  # First value in the plot (first timestep)
    smoothed = list()
    for point in scalars:
        smoothed_val = last * weight + (1 - weight) * point  # Calculate smoothed value
        smoothed.append(smoothed_val)  # Save it
        last = smoothed_val  # Anchor the last smoothed value

    return smoothed


def plt_freq_bar(frequency, xlabels, ious=None, smooth=False):
    # plt.figure(figsize=(6, 4))
    plt.figure(figsize=(4, 4))

    x, y = range(len(frequency)), frequency
    plt.bar(x, y, label='proportion')

    if ious is not None:
        plt.plot(x, ious, linestyle=':', marker='o', label='IoU')

    if smooth:
        ious = smooth_ema(list(ious), weight=0.7)
        plt.plot(x, ious, '*-', color='darkorange', label='smoothed IoU')

    # x 轴标签
    plt.xticks(x, xlabels,
               # size='small',
               rotation=90, fontweight='normal')
    plt.ylim([0, 1.1])

    plt.legend(loc='best')

    # y 轴数字标签
    # for a, b in zip(x, y):
    #     plt.text(a, b + 0.002, '%.3f' % b, ha='center', va='bottom', fontsize=7)

    # plt.title('Cityscapes')

    plt.show()


if __name__ == '__main__':
    stat = stats['CamVid']
    # stat = stats['Cityscapes']
    weights, ious, label = stat['weights'], stat['IoUs'], stat['label']

    idxs = np.argsort(weights)[::-1].astype(int)

    weights, ious, label = weights[idxs], ious[idxs], label[idxs]

    plt_freq_bar(weights, label, ious, smooth=True)
