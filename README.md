# 📊 Big Data Comparison: Pandas vs Dask vs Chunks

# Introduction

In the age of Big Data, traditional data analysis tools are no longer sufficient when dealing with massive files that exceed RAM capacity.

This project aims to compare three methods for processing data:

## 🎯 Objective
Analyze large-scale ecommerce dataset and compare performance between:
- Pandas
- Dask
- Chunk Processing

## 📂 Dataset
~~~~
Ecommerce Behavior Data from Multi Category Store (Kaggle)
~~~~
It contains:
- Millions of rows
- User behavior data in an online store
- Product viewing and purchasing processes

## 📂 File
The file used in the experiment:
~~~~
2019-Nov.csv
~~~~

## Methodology
- > Pandas

The Pandas library relies on loading the entire file into memory (RAM).
~~~
df_pandas = pd.read_csv(file_path)
~~~
Advantages:

- High execution speed

- Suitable for small to medium-sized datasets

Disadvantages:

- Consumes a large amount of memory

- May crash if the file size exceeds the RAM limit

- > Dask

A library that supports parallel processing and does not load all data into memory.
It relies on:

~~~~
df_dask = dd.read_csv(file_path)
~~~~

- Data partitioning

- Lazy Evaluation (executes only when needed using .compute())

Advantages:

- Low memory consumption

- Suitable for large datasets

Disadvantages:

- Slightly slower than Pandas

- Some operations require .compute()
- > Chunk Size

It depends on reading the file in parts:
~~~~
for chunk in pd.read_csv(file_path, chunksize=100000):
~~~~

Advantages:

- Does not load the entire file into memory.

- Suitable for incremental data processing.

Disadvantages:

- Does not benefit from parallel processing.

- If the results are combined, they may consume the same amount of memory.

## ⚙️ Technologies Used
- Python
- Pandas
- Dask
- Time module

## 📈 Metrics Evaluated
- Execution Time
- Memory Usage
- Scalability

  | Method | Speed ​​| Memory Consumption | Best When? |
  | ------- | ----------- | ----------------- | ------------------------ |
  | Pandas | Fastest | Very High | If RAM is large |
  | Dask | Slightly Slower | Low | For large data sets |
  | Chunks | Medium | Not really beneficial | Only for partial processing |

## 🏆 Final Verdict
- Pandas: Fast but high memory consumption
- Dask: Scalable and memory efficient
- Chunks: Suitable for partial processing

  ## Conclusion

  |If the data size is suitable| use the following tools|
  | ------- | ----------- |
  |Less than 1GB| (Pandas)|
  |Between 1GB and 10GB| (Dask)|
  |Processive processing |(Chunks)|
  |Larger than RAM |(Dask)|

> [!note]
> Final Conclusion:
  
## Pandas :
- is suitable for rapid analysis.
- was the fastest but consumed the most memory.

## Dask :  
- is suitable for big data.
- consumed significantly less memory.

## Chunks  : 
- is an intermediate solution but not a complete replacement.
-  didn't offer much benefit when calculating total memory usage, as it ultimately processes all the data.
