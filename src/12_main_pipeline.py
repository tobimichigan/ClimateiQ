
import pandas as pd
from 03_nc_file_discovery import discover_nc_files
from 04_nc_chunk_loader import load_nc_chunked
from 05_preprocessing import preprocess
from 06_feature_engineering import engineer_features

def run_pipeline(root):

    files=discover_nc_files(root)

    dfs=[]
    for f in files:
        print("Loading:",f)
        dfs.append(load_nc_chunked(f))

    df=pd.concat(dfs)

    df=preprocess(df)
    df=engineer_features(df)

    print("Pipeline completed")
    print("Dataset shape:",df.shape)

    return df
