# easytorch

使用Python的numpy实现的简易深度学习框架，API与pytorch基本相同，实现了自动求导、基础优化器、layer等。

## 1 文档目录

[1. 自动求导基础运算实现](./doc/1自动求导基础运算实现.md)

[2. 优化器实现](./doc/2优化器.md)

[3. 损失函数](./doc/3损失函数.md)

[4. layer的实现](./doc/4layer的实现.md)

## 2 Quick Start

``` python 
from easytorch.layer import Linear, Tanh, Sequential
from easytorch.optim import SGD
import easytorch.functional as F

# Create a model, optimizer, loss function
model = Sequential(
    Linear(1, 5),
    Tanh(),
    Linear(5, 1)
)
opt = SGD(model.parameters(), lr=3e-4)
loss_fn = F.mse_loss

# train the model
for epoch in range(epochs):
    pred = model(x)
    loss = loss_fn(pred, y)
    opt.zero_grad()
    loss.backward()
    opt.step()
```

## 3 Example

1. [使用神经网络近似三角函数](./example/FunctionApproximation.ipynb)
2. [使用神经网络预测波士顿房价](./example/Predict.ipynb)
