# Trends of COVID-19 Clusters in Malaysia
International Medical University HIA122 - Health Data Collections and Preparation (302) Group C Official Group Project

This repo focuses on clusters data that are publicly available in https://github.com/MoH-Malaysia/covid19-public
Project output was written in Jupyter notebook file named main.ipynb

The last fork was done on 2nd December 2022.

## General Information:
  1. Data Preparation using ELT:
      - Extracting and Loading the Clusters dataset from https://github.com/MoH-Malaysia/covid19-public and Viewing in Jupyter Notebook
      - Transformation of data includes 3 aspects:
          - Removing columns that aren't required for the analysis
          - Transform categorical columns in the dataset
          - Determine the null values and return null statement
          
  2. Overview of the Transformed Cluster dataset:
      - Viewing the top 5 rows and bottom 5 rows
      - Analysis of the features
      - Detecting the datatype of each columns
      - Sorting out the Active clusters
      - Determining the maximum values of necessary informations
  
  3. Descriptive Analysis of the Transformed Cluster dataset:
      - Describing dataset to view the Mean, Standard Deviation, etc. 
      - Grouping the necessary columns into a table to have a better understanding of the important values

  4. Visualizations for the Transformed Cluster dataset:
      - A total of 5 plots to visualize 5 different aspects:
          - Bar chart - Total number of Clusters in each Category
          - Bar chart - Total number of Deaths in each Category
          - Bar chart - To visualize the 'Active' and 'Ended' Clusters according to each Category
          - Correlation Heatmap - Pearson Test for Multivariate Features of COvid-19 Clusters
          - Heatmap - Distribution of Cases in Clusters according to each Category

## Contributions from Group Members:
  - Ming.ipynb : Analysis of Total number of Clusters based on Category
  - Narmathaa.ipynb : Analysis of Total number of Deaths based on Cluster and Category
  - Nisha1.ipynb : Analysis of Total number of cases and clusters based on States
  - Naufal : get_data.py, get_visual.py and main.ipynb (Compilation and codes improvisation) 

## Technologies:
This project was created with:
  - Jupyter Notebook
  - PyCharm
  - Python 3.10 
