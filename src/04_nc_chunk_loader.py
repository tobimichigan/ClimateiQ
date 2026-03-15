
import xarray as xr
import pandas as pd

def kelvin_to_celsius(arr):
    return arr - 273.15 if arr.mean() > 100 else arr

def load_nc_chunked(filepath, variable="tas"):
    ds = xr.open_dataset(filepath)
    data = ds[variable].values
    lat = ds["lat"].values
    lon = ds["lon"].values

    rows=[]
    for t in range(data.shape[0]):
        vals = kelvin_to_celsius(data[t])
        for i in range(len(lat)):
            for j in range(len(lon)):
                rows.append([lat[i],lon[j],t,vals[i,j]])

    df=pd.DataFrame(rows,columns=["lat","lon","time_idx","tas"])
    ds.close()
    return df
