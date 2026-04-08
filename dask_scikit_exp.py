
from dask.distributed import Client
from dask_ml.model_selection import train_test_split
from dask_ml.linear_model import LinearRegression
import joblib
from joblib import parallel_backend
import matplotlib.pyplot as plt
import numpy as np


x = 50 * np.random.random((30, 1))
y = 0.3 * x + 1.0 + np.random.normal(size=x.shape)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, 
                                                    shuffle=True, 
                                                    random_state=2026
                                                    )
client = Client(processes=False)

model = LinearRegression()

if __name__ == "__main__":
    with parallel_backend("dask"):
        model.fit(x_train, y_train)
        y_new = model.predict(x_test)
        
    plt.figure()
    plt.scatter(x_train, y_train)
    plt.scatter(x_test, y_new, c="red")

    train_r2 = model.score(x_train, y_train)
    test_r2 = model.score(x_test, y_test)

    print(f"train_r2: {train_r2}")
    print(f"test_r2: {test_r2}")