# Analysis-and-Visualisation-of-Play store-Data
Analysis of over 50 00 Play store applications and reviews using Python and SQL and developing a dashboard on Tableau

## Introduction
The report presents an analysis of data from the Google Play store using a combination of Python, Excel, Power Query, SQL, and Power BI. The data processing and manipulation is done using Python and Excel, with Power Query being used for data cleaning and integration. The data is then analysed using SQL, and the findings are visualized using Power BI for easy interpretation and decision-making. The report aims to provide insights into the data and make data-driven recommendations.

You can access the raw data in the folder named "Data", also available here https://www.kaggle.com/datasets/lava18/google-play-store-apps

## Data Processing using Python

The Google Play store raw datasets was firstly pre-processed using Python. Duplicate rows and irrelevant values such as values that does not comply with data type of the column were removed using Python libraries such as Numpy and Pandas (see python script "Playstore_data_processing.py"). The resulting files was stored as csv files and was further processed using excel and power query.
 
## Data Processing using Excel and Power Query

The csv files were then processed using excel and the following operation were performed;
- Changed all datatype from General to suitable datatype
-  Rating column: replaced all null values (1454) to 0 (since its float)
-  Delete the row with a null value for columns with datatype text or string
   Type column: removed 1 column with type as zero
   Android ver: removed 2
	
- For column current ver if there is any null value, change it to NaN
	(13 changed)
 
 The following cleaning process were performed in Power Query;
 Changes made in power query

- Replaced all the "." with "," in all column numbers or floats
- Content rating column combined everyone 10+ with everyone and removed numbers at the end of each category
- Size column: Rename to Size (MB) and converted k to MB.


## Analysis using Microsoft SQL Server Management Studio (SSMS)
The analysis performed on SSMS to answer the following questions (see "Playstore_queries.sql");

- Which apps have the highest rating in the given available dataset?
- What are the number of installs and reviews for the above apps? 
- Which app has the highest number of reviews? Also, mention the number of reviews and category of the app
- What is the total amount of revenue generated by the google play store by hosting apps? (Whenever a user buys apps from the google play store, the amount is considered in the revenue)
- Which Category of google play store apps has the highest number of installs? Also, find out the total number of installs for that particular category.
- Which Genre has the most number of published apps?
- Provide the list of all games ordered in such a way that the game that has the highest number of installs is displayed on the top
- Provide the list of apps that can work on android version 4.0.3 and UP.
- How many apps from the given data set are free? Also, provide the number of paid apps.
- Which is the best dating app? (Best dating app is the one having the highest number of Reviews)
- Get the number of reviews having positive sentiment and number of reviews having negative sentiment for the app 10 best foods for you and compare them.
- Which comments of ASUS SuperNote have sentiment polarity and sentiment subjectivity both as 1?
- Get all the neutral sentiment reviews for the app Abs Training-Burn belly fat 
- Extract all negative sentiment reviews for Adobe Acrobat Reader with their sentiment polarity and sentiment subjectivity



## Data Visualisation using Power BI
The findings from the Analysis were visualised using Power BI. Here is the link to the Dashboard: https://app.powerbi.com/groups/me/reports/e385b407-01cf-4276-a6aa-8bea9a6d0560/ReportSection or Download and open the file named "Play store App Dashboard.pbix"

## Conclusion
Some of the insights from the Google Play store analysis include the following;
- Overall Revenue is currently at $10 000 with only 7.3 % of the apps are paid applications
- Overall Downloads is currently at 128 Billion. Downloads for Game and communication category are significantly higher than others are.
- The most downloaded applications are Google Photos, Hangouts and Subway surfers and both belong to either Game or Communication Category.
- Facebook is the most reviewed application with almost equal of positive (45.74%) and negative (41.09%) sentiments.
- There about 268 Apps with a Rating of 5 star and 10% of them are paid application with a combined revenue of $101.


## Acknowledgements
- Thank you to HiCounselor for the opportunity to work on this amazing live-project.
- Credit to Lavanya (https://www.kaggle.com/lava18) for creating the dataset
