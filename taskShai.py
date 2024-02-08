# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 15:10:19 2024

@author: Fedaa Almomani
"""

import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("C:\\Users\\user\Downloads\Salaries.csv")

print('\n*********************\n')

print("The first rows :")
print(df.head())

print('\n***********************\n')

rows, columns = df.shape
print("Number of rows:", rows," Number of columns: ", columns)

print('\n***********************\n')

data_types = df.dtypes
print("Data types")
print(data_types)

print('\n***********************\n')

missing_values = df.isnull().sum()
print("Missing values:")
print(missing_values)

print('\n***********************\n')

basic_stats = df.describe()
print("Basic statistics:")
print(basic_stats)

print('\n***********************\n')

salary_range = df['TotalPay'].max() - df['TotalPay'].min()
print("Salary range:" ,salary_range)

print('\n***********************\n')

std_deviation = df['TotalPay'].std()
print("standard deviation: ", std_deviation)


df['Benefits'].fillna(df['Benefits'].mean(), inplace=True)


plt.hist(df['TotalPay'], bins=20, color='blue', alpha=0.7)
plt.xlabel("total salary")
plt.ylabel("Number of Employees")
plt.title("Salary distribution")
plt.show()


department_counts = df['JobTitle'].value_counts()
top_jobs = department_counts.head(10)  

plt.figure(figsize=(10, 6))
plt.pie(top_jobs, labels=top_jobs.index, autopct='%1.1f%%', startangle=90, counterclock=False, wedgeprops=dict(width=0.4))
plt.title("Percentage of employees by position")
plt.show()

print('\n***********************\n')

correlation = df['TotalPay'].corr(df['BasePay'])
print("Correlation between TotalPay and BasePay: ",correlation)

plt.scatter(df['BasePay'], df['TotalPay'])
plt.title('Scatter Plot: TotalPay vs BasePay')
plt.xlabel('BasePay')
plt.ylabel('TotalPay')
plt.show()