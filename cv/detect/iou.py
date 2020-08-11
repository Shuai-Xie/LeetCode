import numpy as np


def box_area(box):
    if isinstance(box, np.ndarray) and len(box.shape) > 1:  # 2D
        return (box[:, 2] - box[:, 0] + 1) * (box[:, 3] - box[:, 1] + 1)
    else:
        return (box[2] - box[0] + 1) * (box[3] - box[1] + 1)


def get_IoU(pred_box, gt_box):
    # x1,y1,x2,y2
    xmin = max(pred_box[0], gt_box[0])  # left-top max
    ymin = max(pred_box[1], gt_box[1])
    xmax = min(pred_box[2], gt_box[2])  # right-bottom min
    ymax = min(pred_box[3], gt_box[3])

    inter_w = max(xmax - xmin + 1, 0)
    inter_h = max(ymax - ymin + 1, 0)

    inter = inter_w * inter_h
    union = box_area(pred_box) + box_area(gt_box) - inter

    return inter / union


def get_max_IoU(pred_boxes, gt_box):
    """
    pred_boxes: N * 4
    gt_box: 4
    """
    if pred_boxes.shape[0] > 0:
        # 同时计算 N 个 box 的 inter box
        xmin = np.maximum(pred_boxes[:, 0], gt_box[0])  # left-top max
        ymin = np.maximum(pred_boxes[:, 1], gt_box[1])
        xmax = np.minimum(pred_boxes[:, 2], gt_box[2])  # right-bottom min
        ymax = np.minimum(pred_boxes[:, 3], gt_box[3])

        inter_ws = np.maximum(xmax - xmin + 1, 0)
        inter_hs = np.maximum(ymax - ymin + 1, 0)

        inters = inter_ws * inter_hs  # element-wise
        unions = box_area(pred_boxes) + box_area(gt_box) - inters
        ious = inters / unions  # 不会出现 nan

        imax = np.argmax(ious)
        return pred_boxes[imax], ious[imax]


class IoU_metric:

    def __init__(self, num_classes):
        # 过滤掉除法的 RuntimeWarning: invalid value encountered in true_divide, 容许 nan 出现在计算结果
        np.seterr(divide='ignore', invalid='ignore')
        self.num_classes = num_classes
        self.confusion_matrix = np.zeros((num_classes, num_classes))

    def _fast_hist(self, gt, pred):
        """
        通过快速直方图 计算 confusion matrix 每个 grid 取值
        可直接计算 batch img 结果，因为 np.bincount 会自动拉平
        """
        mask = (gt >= 0) and (gt < self.num_classes)  # valid mask
        # 以 gt 为行，pred 为列
        # gt   行 -> recall     gt=1 的数量中，实际 pred=1 的数量
        # pred 列 -> precision  pred=1 的数量中，实际 gt=1 的数量
        label = self.num_classes * gt[mask] + pred[mask]  # 前1项乘积，将元素引导到gt所在行，+ pred 得到 pred 估计的列
        count = np.bincount(label, minlength=self.num_classes ** 2)  # minlength 从0开始计数
        return count.reshape((self.num_classes, self.num_classes))  # 再按行展开

    def add_batch(self, gt, pred):
        assert pred.shape == gt.shape
        self.confusion_matrix += self._fast_hist(gt, pred)

    def reset(self):
        self.confusion_matrix = np.zeros((self.num_classes, self.num_classes))

    def get_classs_IoU(self):
        inter = np.diag(self.confusion_matrix)
        union = self.confusion_matrix.sum(0) + self.confusion_matrix.sum(1) - inter  # gt + pred - inter
        return inter / union

    def get_mIoU(self):
        return np.nanmean(self.get_classs_IoU())  # iou 计算有 nan 可能

    # 除法计算 P,R,IoU 都有 nan 可能 (0/0), 所以计算均值用 nanmean
    # c[np.isnan(c)] = 0 可将结果中 nan 置 0，但计算 mean 用 nanmean 更合理
    def accuracy(self):  # pixel acc
        return np.diag(self.confusion_matrix).sum() / self.confusion_matrix.sum()

    def get_class_Precision(self):
        return np.diag(self.confusion_matrix) / self.confusion_matrix.sum(1)

    def get_class_Recall(self):
        return np.diag(self.confusion_matrix) / self.confusion_matrix.sum(0)

    def get_mPrecision(self):
        return np.nanmean(self.get_class_Precision())

    def get_mRecall(self):
        return np.nanmean(self.get_class_Recall())


if __name__ == "__main__":
    # test1
    pred_bbox = np.array([50, 50, 90, 100])  # top-left: <50, 50>, bottom-down: <90, 100>, <x-axis, y-axis>
    gt_bbox = np.array([70, 80, 120, 150])
    print(get_IoU(pred_bbox, gt_bbox))

    # test2
    pred_bboxes = np.array([[15, 18, 47, 60],
                            [50, 50, 90, 100],
                            [70, 80, 120, 145],
                            [130, 160, 250, 280],
                            [25.6, 66.1, 113.3, 147.8]])
    gt_bbox = np.array([70, 80, 120, 150])
    print(get_max_IoU(pred_bboxes, gt_bbox))
