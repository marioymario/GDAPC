# Notes for Go Beyond Numbers: Translate Data into Insight
---

This repo has personal notes, code and data related to the third course of the 
Google Advanced Data Analytics Professional Certificate.

In this course we go about how to do do Exploratory Data Analysis, from the 
PACE (Plan, Analyze, Construct, Execute) point of view. Some of the subjects 
are:

 - **Exploring Raw data**.

     - Where de data comes from?
	 - Importing data
     - libraries and modules, Pandas, Numpy, Matplotlib, Scipy, datetime...
     - Structuring data, merge, concat, join.
  
 - **Cleaning Data, Validating as work is being done**.

    - Missing Data, De-duplication,
    - Outliers, Global, Contextual, Collective 
       - **Delete** them: If you are sure the outliers are mistakes, typos 
the dataset will be used for modeling or machine learning.  
       - **Reassign** them: If the dataset is small and/or the data will be used
 for modeling or machine learning, you are more likely to choose a path of 
deriving new values to replace the outlier values.  
       - **Leave them**: For a dataset that you plan to do EDA/analysis on and 
nothing else, or for a dataset you are preparing for a model that is resistant 
to outliers.
    - Transformations, Grouping, Sorting, label Encoding, One Hot Encoding.
    
 - **Visualizations and presentations**.
    
    - Effective data visualizations, Info, Story, Goal, Visual Form.
    - Correlation and causation.
    - Tableau, Charts, Matplotlib.
      - Comparative: Column chart, bar chart, Line Chart, Scatter plot.
      - Distribution: Histogram, Boxplot, Kernel Density plot.
      - Segmentation: Pie Charts, Stacked bar plots.
      - Relationship: Scatter Plot, Line Chart.
      - Time Series: Line Chart, Area Chart, Column Chart.

 - **Crafting compelling histories**.

    -  Consider three strategies for organizing and 
presenting data visualizations in a series. 
**Chronological**, **generic-to-specific**, and **specific-to-generic**. 
A chronological approach to data visualization is useful for 
data that is best understood in a time series. 
A generic-to-specific approach helps an audience consider an issue before 
describing how it affects them. 
And, a specific-to-generic approach is useful to highlight 
impacts the data can have on a broader scale. 
      
---
## **The six main practices of EDA and the common tools used:**


1. **Discovering**, 

	Data professionals familiarize themselves with the data so 
they can start conceptualizing how to use it. 
They review the data and ask questions about it. 
During this phase data professionals may ask what are the column headers and 
what do they mean? 
How many total data points are there?


2. **Structuring**, 

	Structuring is the process of taking raw data and organizing or 
transforming it to be more easily visualized, explained or modeled. 
Structuring refers to categorizing and 
organizing data columns based on the data already in the data set. 
In terms of the calendar data for example it might look like 
categorizing data into months or quarters rather than years.

3. **Cleaning**,

	Cleaning is the process of removing errors that may distort your data or 
make it less useful. 
Missing values, misspellings, duplicate entries or extreme outliers are all 
fairly common issues that need to be addressed during the data set cleaning.

	 
4. **Joining**, 

	Joining is the process of augmenting or 
adjusting data by adding values from other data sets. 
In other words, you might add more value or 
context to the data by adding more information from other data sources.

5. **Validating** and 

	Validating refers to the process of verifying that the data is consistent and 
high quality. 
Validating data is the process for checking for misspellings and 
inconsistent number or date formats. 
And checking that the data cleaning process didn't introduce more errors. 
Data professionals typically use digital tools such as R, JavaScript or 
python to check for inconsistencies and errors in a data set and its data types. 

	
12. **Presenting**. 

	Presenting involves making your cleaned data set or 
data visualizations available to others for analysis or further modeling. 
In other words presenting practice is sharing what you've learned through EDA. 
And asking for feedback whether in the form of a clean data set or 
data visualization. 
 