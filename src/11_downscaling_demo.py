
import torch

def run_downscaling(model,X):
    X_t=torch.tensor(X).float()
    preds=model(X_t).detach().numpy()
    return preds
