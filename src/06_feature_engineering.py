
import numpy as np

def engineer_features(df):
    df["sin_lat"]=np.sin(np.deg2rad(df["lat"]))
    df["cos_lat"]=np.cos(np.deg2rad(df["lat"]))
    df["sin_lon"]=np.sin(np.deg2rad(df["lon"]))
    df["cos_lon"]=np.cos(np.deg2rad(df["lon"]))
    return df
