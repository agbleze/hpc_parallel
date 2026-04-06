from dask_saturn import SaturnCluster, RegisterFiles, sync_files
from distributed import Client
import dask.dataframe as dd
import pandas as pd
import time

cluster = SaturnCluster()
client = Client(cluster)

client.register_worker_plugin(RegisterFiles())
sync_files(client, "data")

ddf = dd.read_csv("data/prices_.sv", dtype={"volume": "float64"},
                  parse_dates = ["dates"]
                  )

ddf.compute()
ddf.info(memory_usage="deep")

del ddf["Unnamed: 0"]

mean = ddf.groupby()

mean = ddf.groupby(["symbol", ddf["date"].dt.year])[["open", "high", "low", "close", "volume"]].mean()

t1 = time.perf_counter()
mean.compute()
t2 = time.perf_counter()

print(f"Elapsed time {t2 - t1} seconds")


