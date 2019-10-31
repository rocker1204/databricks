# Databricks notebook source
# MAGIC %sql 
# MAGIC show databases;

# COMMAND ----------

from datetime import datetime

now = datetime.now() # current date and time
year = now.strftime("%Y")
print("year:", year)
month = now.strftime("%m")
print("month:", month)
day = now.strftime("%d")
print("day:", day)
time = now.strftime("%H:%M:%S")
print("time:", time)
date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
print("date and time:",date_time)		

# COMMAND ----------

# MAGIC %sql
# MAGIC show tables from poc;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT customer_id, product_category FROM poc.poc_amazon_reviews where product_category = 'Books'
# MAGIC LIMIT 10

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE TEMP_TEST AS 
# MAGIC SELECT customer_id, product_category FROM poc.poc_amazon_reviews where product_category = 'Books' limit 10

# COMMAND ----------

# MAGIC %sql
# MAGIC show tables from poc;

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from poc.sample_csv

# COMMAND ----------

