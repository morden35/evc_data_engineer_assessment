# 01 Data Wrangling

## How to run

From the /Data\ Engineer\ Assessment directory, run the following:
`$ python3 01_data_wranglin/merge_x_y_data.py`

## merge_x_y_data.py

I decided to abstract the merge_x_y_data.py file into 2 functions. I will describe the purpose of each function below.

### download_vendor_y()

download_vendor_y() downloads Vendor Y's data form the API using the requsts library. If the download is successful,
the downloaded data is passed to merge_vendor_x_y_data(). If the download fails, download_vendor_y() returns a message with the status code.

### merge_vendor_x_y_data()

merge_vendor_x_y_data() does most of the data cleaning required for this task. merge_vendor_x_y_data() takes in Vendor Y's data in json format. It then converts the json to a pandas dataframe. merge_vendor_x_y_data() then imports Vendor X's data as a pandas dataframe. It then
converts the column datatypes and renames columns for each dataframe. Finally, merge_vendor_x_y_data() merges the two dataframes into one, and saves the merged dataframe as a csv file.

#### Ambiguous dob column

It is important to note that Vendor Y's 'dob' column needed some extra cleaning/handling. This column was downloaded from the API with the following format: 'yy-mm-dd'. Since the first two digit's represent the year, we run into the issue of deciding which years fall in the 20th or 20st century. For example, the value '20-01-01' could either be January 1st, 1920 or January 1st, 2020.

In this case, it's safe to assume that years represented by the digits 24-99 are from the 20th century, since 2024 and later is in the future. That leaves us to deal with years represented by the digits 00-23.

Since we are working with voting data, and people are not allowed to vote until age 18, I made a large assumption that years 06-23 fell into the 20th century and years 00-05 fell into the 21st century. This is a very large assumption, and one that is certainly prone to errors. Additionally, this conditional will have to change over time (in the year 2024, we may want to consider dates starting with the digits 06 were born in 2006 rather than 1906). If there was more time, I could have made this conditional more robust.
