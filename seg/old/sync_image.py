import matplotlib.pyplot as plt

import cv2
import numpy as np


def color_code_target(target, label_colors):
    return np.array(label_colors)[target.astype('int')]


label_colors = [[128, 128, 128], [128, 0, 0], [192, 192, 128], [128, 64, 128], [60, 40, 222], [128, 128, 0], [192, 128, 128], [64, 64, 128], [64, 0, 128],
                [64, 64, 0], [0, 128, 192], [0, 0, 0]]


def quantify_spx_hard_level():
    # img_name = '0001TP_009600'
    img_name = '0016E5_08071'
    # img_name = 'Seq05VD_f04680'
    # img_name = '0016E5_08127'

    # img_root = '/nfs2/xs/Datasets/CamVid11/test/image'
    # img = cv2.imread(f'{img_root}/{img_name}.png')

    target = cv2.imread(f'npy/{img_name}_target.png', cv2.IMREAD_ANYDEPTH)
    target_error_mask = cv2.imread(f'npy/{img_name}_err.png', cv2.IMREAD_ANYDEPTH)
    pred_error_mask = np.load(f'npy/{img_name}_score.npy')

    f, ax = plt.subplots(nrows=3, ncols=3, figsize=(8, 6.5))
    axs = ax.flat
    # plt.suptitle(img_name)

    # axs[0].axis('off')
    # axs[0].imshow(img)
    # axs[0].set_title('img')

    axs[0].axis('off')
    axs[0].imshow(color_code_target(target, label_colors))
    axs[0].set_title('target')

    axs[1].axis('off')
    axs[1].imshow(color_code_target(target_error_mask, label_colors))
    # axs[1].set_title('target_error_mask')
    axs[1].set_title(img_name)

    axs[2].axis('off')
    axs[2].imshow(pred_error_mask, cmap='jet')
    axs[2].set_title('pred_error_mask')

    hard_levels = 6
    pixel_nums, score_ticks = np.histogram(pred_error_mask, bins=hard_levels)

    for i in range(hard_levels):
        if i == hard_levels - 1:
            mask = (pred_error_mask >= score_ticks[i]) & (pred_error_mask <= score_ticks[i + 1])
        else:
            mask = (pred_error_mask >= score_ticks[i]) & (pred_error_mask < score_ticks[i + 1])

        level_mask = pred_error_mask.copy()
        level_mask[~mask] = 0
        axs[i + 3].axis('off')
        axs[i + 3].imshow(level_mask, cmap='jet')
        axs[i + 3].set_title(f'level:{i + 1}')

    plt.show()


if __name__ == '__main__':
    quantify_spx_hard_level()
