
#%%
import numpy as np
import pandas as pd
import dask.dataframe as dd
import dask.array as da
import dask.bag as db
import dask

#%%
df = pd.DataFrame(np.random.rand(60).reshape(10,6))

print(df)

#%%
ddf = dd.from_pandas(df, npartitions=4)

print(ddf)

print(ddf.divisions)

#%%
#print(ddf.compute())

#%%
narr = np.random.randint(0, 10, 100).reshape(10, 10)
darr = da.from_array(narr, chunks=(5,5))
print(f"darr: {darr}")
print(f"array chunks: {darr.chunks}")

print(f"Array: {darr.compute()}")

#%% methods on collections
print(ddf.columns)
print(f"ddf[1]: {ddf[1].compute()}")
m = ddf[1].mean()

print(f"mean lazy: {m}")
print(f"array mean: {m.compute()}")


mm = np.mean(darr)
print(f"mm: {mm}")
print(f"mm.compute: {mm.compute()}")

print(f"mm task graph: {mm.dask}")

#%%
print(f"visualize task graph: {mm.visualize()}")


#%% dask delayed for creating custom parallelizable functions

@dask.delayed
def doubled(x):
    return 2*x

d = doubled(darr)

print(f"delayed dask called: {d}")

print(f"d.compute(): {d.compute()}")



