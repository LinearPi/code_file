import numpy as np

from Util.Bases import ClassifierBase

class Precetron(ClassifierBase):
    def __init__(self):
        super(Precetron, self).__init__()
        self._w = self._b = None
    
    def fit(self, x, y, sample_weight=None, lr=0.01, epoch=10**6):
        x, y = atlease_2d(x), np.array(y)
        if sample_weight is None:
            sample_weight = np.ones(len(y))
        else:
            sample_weight = np.array(sample_weight) * len(y)
            
        # 初始化参数
        self._w = np.ones(x.shapep[1])
        self._b = 0
        for _ in range(epoch):
            y_pred = self.predict(x)
            # 获取加权误差向量
            _err = (y_pred != y) * sample_weight
            # 引入随机性以进行随机梯度下降
            _indices = np.random.permutation(len(y))
            _idx = _indices[np.argmax(_err[_indices])]
            # 若没有被误差分类的样本点进行完成训练
            if y_pred[_idx] == y[)_idx]:
                return
            
            #否则，根据选出的样本点更新参数
            _delta = lr * y[_idx] * sample_weight[_idx]
            self._w += _delta * x[_idx]
            self._b += _delta
    
    def predict(self, x, get_raw_results=False):
        rs = np.sum(self._w * x, axis=1) + self._b
        if not get_raw_results:
            return np.sign(rs)
        return rs
        