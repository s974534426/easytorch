import sys
sys.path.append('..')

import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
from easytorch import tensor, optim


def generate_data(n=100, f=lambda x: 2 * x - 1):
    data = []
    for _ in range(n):
        x = np.random.uniform(-3, 3, 3)
        y = f(x) + 0.01 * np.random.randn()
        data.append([x, y])
    return data


def sgd_linear_approximation():
    train_data = generate_data(n=100, f=lambda x: x[0]+2*x[1]+3*x[2])
    x = tensor.Tensor([x for x, y in train_data])
    y = tensor.Tensor([y for x, y in train_data])
    w = tensor.random(3, requires_grad=True)
    b = tensor.Tensor(1.0, requires_grad=True)
    opt = optim.SGD([w, b], lr=0.01)
    loss_list = []

    for _ in tqdm(range(1000)):
        for data_x, data_y in zip(x, y):
            pred = data_x @ w + b
            loss = ((pred - data_y) * (pred - data_y)).mean()
            loss_list.append(loss.data)
            opt.zero_grad()
            loss.backward()
            opt.step()

    plt.plot(loss_list)
    plt.show()


if __name__ == '__main__':
    sgd_linear_approximation()
