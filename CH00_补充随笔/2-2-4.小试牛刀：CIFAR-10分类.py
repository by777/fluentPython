# -*- coding: utf-8 -*-
# @TIME : 2021/3/18 16:39
# @AUTHOR : Xu Bai
# @FILE : 2-2-4.小试牛刀：CIFAR-10分类.py
# @DESCRIPTION :
# CIFAR数据集10个类别， 3 * 32 * 32
import torch as t
import torchvision as tv
import torchvision.transforms as transforms
from torch import optim
from torch.autograd import Variable
from torchvision.transforms import ToPILImage

show = ToPILImage()  # 可以把Tensor转化为Image，方便查看

# 定义对数据的预处理
transform = transforms.Compose([
    transforms.ToTensor(),  # 转化为Tensor
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))  # mean，std归一化
])
# 训练集

trainset = tv.datasets.CIFAR10(
    root='./',
    train=True,  # If True, creates dataset from training set, otherwise creates from test set.
    download=True,
    transform=transform
)
trainloader = t.utils.data.DataLoader(
    trainset,
    batch_size=4,
    shuffle=True,
    num_workers=2
)
testset = tv.datasets.CIFAR10(
    root='./',
    train=False,
    download=True,
    transform=transform
)
testloader = t.utils.data.DataLoader(
    testset,
    batch_size=4,
    shuffle=False,
    num_workers=2
)
classes = ('plane', 'car', 'bird', 'cat', 'deer',
           'dog', 'frog', 'horse', 'ship', 'truck')

# 定义网络
import torch.nn as nn
from torch.nn import functional as F


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(3, 6, 5)
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 64)
        self.fc3 = nn.Linear(64, 10)

    def forward(self, x):
        x = F.max_pool2d(F.relu(self.conv1(x)), (2, 2))
        x = F.max_pool2d(F.relu(self.conv2(x)), 2)
        x = x.view(x.size()[0], -1)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x


if __name__ == '__main__':
    net = Net()

    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(net.parameters(), lr=0.01, momentum=0.9)
    # print(len(trainset))  # 可以按下标访问
    # (data, label) = trainset[100]
    # print(classes[label])
    # (data +1)/2 是为了还原被归一化的数据
    # show((data + 1) / 2).resize((100, 100))  # .show()

    # print('DataLoader是一个可迭代对象，它将dataset返回的每一条数据样本拼接成一个batch')

    # print('训练网络')
    for epoch in range(1):
        running_loss = 0.0
        for i, data in enumerate(trainloader, 0):
            inputs, labels = data
            inputs, labels = Variable(inputs), Variable(labels)
            # 梯度清零
            optimizer.zero_grad()
            # forward + backward
            outputs = net(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            # 更新参数
            optimizer.step()
            # 打印log信息
            running_loss += loss.item()  # 这里根据运行提示把loss.data[0]改为了.item()
            if i % 2000 == 1999:
                # 每2000个batch打印一次训练状态
                print('[%d, %5d] loss: %.3f' % (epoch + 1, i + 1, running_loss / 2000))
                running_loss = 0.0

    dataiter = iter(testloader)
    images, labels = dataiter.next()
    print('实际的label： ', ' '.join('%08s' % classes[labels[j]] for j in range(4)))
    show(tv.utils.make_grid(images / 2 - 0.5)).resize((400, 400)).show()
    # 计算图片在每个类别上的分数
    outputs = net(Variable(images))
    # 得分最高的那个类
    _, predicted = t.max(outputs.data, 1)
    print('预测结果： ', ' '.join('%5s' % classes[predicted[j]] for j in range(4)))

    # 观察在整个训练集上的结果
    correct = 0  # 预测正确的图片数
    total = 0  # 总共图片数
    for data in testloader:
        images, labels = data
        outputs = net(Variable(images))
        print(outputs.data)
        print(outputs.data.size())
        _, predicted = t.max(outputs.data, 1)  # 0是每列的最大值，1是每行的最大值
        total += labels.size(0)
        correct += (predicted == labels).sum()  # 方便
    print('10000张测试集中的准确率为： %d %%' % (100 * correct / total))
