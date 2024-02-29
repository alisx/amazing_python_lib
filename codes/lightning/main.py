# 安装
'''
# 要启动你的  PyTorch Lightning  之旅，只需要简单的几行命令即可安装：

pip install lightning

# 如果需要安装具有额外功能的版本，可以运行：

pip install lightning['extra']

# 而特定环境下的安装（如 conda 环境）也有相对应的安装方式：

conda install lightning -c conda-forge
'''

import torch, torch.nn as nn, torch.utils.data as data, torchvision as tv, torch.nn.functional as F
import lightning as L

# --------------------------------
# Step 1: Define a LightningModule
# --------------------------------
# A LightningModule (nn.Module subclass) defines a full *system*
# (ie: an LLM, diffusion model, autoencoder, or simple image classifier).


class LitAutoEncoder(L.LightningModule):
    def __init__(self):
        super().__init__()
        self.encoder = nn.Sequential(nn.Linear(28 * 28, 128), nn.ReLU(), nn.Linear(128, 3))
        self.decoder = nn.Sequential(nn.Linear(3, 128), nn.ReLU(), nn.Linear(128, 28 * 28))

    def forward(self, x):
        # in lightning, forward defines the prediction/inference actions
        embedding = self.encoder(x)
        return embedding

    def training_step(self, batch, batch_idx):
        # training_step defines the train loop. It is independent of forward
        x, y = batch
        x = x.view(x.size(0), -1)
        z = self.encoder(x)
        x_hat = self.decoder(z)
        loss = F.mse_loss(x_hat, x)
        self.log("train_loss", loss)
        return loss

    def configure_optimizers(self):
        optimizer = torch.optim.Adam(self.parameters(), lr=1e-3)
        return optimizer


# -------------------
# Step 2: Define data
# -------------------
dataset = tv.datasets.MNIST(".", download=True, transform=tv.transforms.ToTensor())
train, val = data.random_split(dataset, [55000, 5000])

# -------------------
# Step 3: Train
# -------------------
autoencoder = LitAutoEncoder()
trainer = L.Trainer()
trainer.fit(autoencoder, data.DataLoader(train), data.DataLoader(val))


# 设置数据 
dataset = "# ... 省略数据设置代码"
train, val = data.random_split(dataset, [55000, 5000])

# 初始化模型和训练器 
autoencoder = LitAutoEncoder()
trainer = L.Trainer()

# 开始训练 
trainer.fit(autoencoder, data.DataLoader(train), data.DataLoader(val))


# 将模型训练在  8  个 GPUs  上
trainer = Trainer(accelerator="gpu", devices=8)

# 使用特定的分布式训练策略 
trainer = Trainer(strategy="ddp")
trainer = Trainer(strategy="fsdp")

# 混合精度训练 
trainer = Trainer(precision=16)

# 早停策略 
trainer = Trainer(callbacks=[EarlyStopping(monitor="val_loss")])

# 模型检查点 
trainer = Trainer(callbacks=[ModelCheckpoint(monitor="val_loss")])