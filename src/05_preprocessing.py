
def preprocess(df):
    df=df.dropna(subset=["tas"])
    df=df[(df["tas"]>=-90) & (df["tas"]<=60)]
    return df
