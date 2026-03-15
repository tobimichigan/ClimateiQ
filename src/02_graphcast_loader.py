
import os, glob, numpy as np
from huggingface_hub import snapshot_download

def download_graphcast(repo_id="google-deepmind/graphcast"):
    path = snapshot_download(repo_id=repo_id)
    return path

def extract_graphcast_matrix(path):
    npz_files = glob.glob(os.path.join(path,"**","*.npz"),recursive=True)
    if not npz_files:
        return None
    data = np.load(npz_files[0])
    for k,v in data.items():
        if isinstance(v,np.ndarray) and v.ndim==2:
            return v
    return None
