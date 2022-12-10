# Trends of COVID-19 Clusters in Malaysia
International Medical University HIA122 - Health Data Collections and Preparation (302) Group C Official Group Project

This repo focuses on clusters data that are publicly available in https://github.com/MoH-Malaysia/covid19-public
Project output was written in Jupyter notebook file named main.ipynb

The last fork was done until 2nd December 2022.

## General Information:
  1. Data Preparation using ELT:
      - Extracting and Loading the Clusters dataset from https://github.com/MoH-Malaysia/covid19-public and Viewing in Jupyter Notebook
      - Transformation of data includes 3 aspects:
          a). Dropping columns that are not necessary for the analysis
          b). Transform categorical columns in the dataset
          c). Determine the null values and return null statement
          
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
          a). Bar chart - Total number of Clusters in each Category
          b). Bar chart - Total number of Deaths in each Category
          c). Bar chart - To visualize the 'Active' and 'Ended' Clusters according to each Category
          d). Correlation Heatmap - Pearson Test for Multivariate Features of COvid-19 Clusters
          e). Heatmap - Distribution of Cases in Clusters according to each Category

## Technologies:
The project created with:
  - Jupyter Notebook
  - PyCharm
  - Python 3.10 
