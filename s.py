import dask.dataframe as dd  
import time
import pandas as pd
import os

dataset_name = "mkechinov/ecommerce-behavior-data-from-multi-category-store"
data_path = "/kaggle/input/ecommerce-behavior-data-from-multi-category-store"
file_path = f"{data_path}/2019-Nov.csv"  

start_time = time.time()
df_dask = dd.read_csv(file_path)

column_count = len(df_dask.columns)
print(f"Number of columns: {column_count}")

row_count = df_dask.shape[0].compute()  
print(f"Number of rows: {row_count}")

print(df_dask.head(15))

memory_dask = df_dask.map_partitions(lambda df: df.memory_usage(deep=True).sum()).compute().sum() / (1024 ** 2)
print(f"Memory usage (Dask): {memory_dask:.2f} MB")

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time (Dask): {execution_time:.2f} seconds")

# =================================
#  Data Download Speed Comparison 
# ====================================
start_time = time.time()
df_pandas = pd.read_csv(file_path)
end_time = time.time()
print(f"Pandas - Execution time: {end_time - start_time:.2f} seconds")

memory_pandas = df_pandas.memory_usage(deep=True).sum() / (1024 ** 2)
print(f"Memory usage (Pandas): {memory_pandas:.2f} MB")

start_time = time.time()
chunksize = 100000  
total_memory_chunks = 0

for chunk in pd.read_csv(file_path, chunksize=chunksize):
    total_memory_chunks += chunk.memory_usage(deep=True).sum()

total_memory_chunks = total_memory_chunks / (1024 ** 2)
end_time = time.time()
print(f"Chunksize - Execution time: {end_time - start_time:.2f} seconds")
print(f"Memory usage (Chunksize): {total_memory_chunks:.2f} MB")
