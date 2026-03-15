
import torch
import numpy as np
from sklearn.metrics import mean_squared_error

def train(model,X,y,epochs=10,lr=1e-3):
    optimizer=torch.optim.Adam(model.parameters(),lr=lr)
    loss_fn=torch.nn.MSELoss()

    X_t=torch.tensor(X).float()
    y_t=torch.tensor(y).float()

    for e in range(epochs):
        pred=model(X_t).squeeze()
        loss=loss_fn(pred,y_t)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        rmse=np.sqrt(mean_squared_error(y,pred.detach().numpy()))
        print("Epoch",e,"RMSE",rmse)
