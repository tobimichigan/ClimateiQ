
from sklearn.preprocessing import StandardScaler

def split_data(X,y,train_ratio=0.7):
    n=len(X)
    n_train=int(n*train_ratio)
    return (X[:n_train],y[:n_train]),(X[n_train:],y[n_train:])

def scale_data(X_train,X_test):
    scaler=StandardScaler()
    X_train=scaler.fit_transform(X_train)
    X_test=scaler.transform(X_test)
    return X_train,X_test,scaler
