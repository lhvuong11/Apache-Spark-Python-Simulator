# Apache Spark Python Simulator

## What is Apache Spark?

Apache Spark is a fast and scalable framework for processing large datasets. Unlike traditional MapReduce, which writes intermediate data to disk, Spark processes data in-memory, making it much faster.

## Why is Spark Important?

✅ Speed: Processes data 100x faster than MapReduce for certain workloads.

✅ Ease of Use: Supports SQL queries, structured data, and machine learning.

✅ Real-Time Processing: Can handle live data streams, unlike batch-only systems like MapReduce.

## How Does Spark Work?

Spark divides large datasets into smaller Resilient Distributed Datasets (RDDs), which can be processed across multiple machines in parallel. However, since we don’t have a Spark cluster, we will simulate Spark-like behavior using Python’s Pandas library.

### Problem Statement

You are given a dataset containing information about website visits. Each row represents a visit by a user.

Your task is to simulate Spark-like transformations using Pandas to analyze the data.

### Tasks
```
1. Load the data into a Pandas DataFrame (simulating a Spark DataFrame).
2. Perform the following Spark-like transformations:

    Calculate the total time spent per user (UserID).

    Find the most visited page using a group-by operation.

    Compute the average time spent per page.

3. Output the final results in a readable format.
``` 
