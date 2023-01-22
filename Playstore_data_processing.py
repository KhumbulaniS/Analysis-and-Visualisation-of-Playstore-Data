#import libraries
import pandas as pd
import numpy as np
from numpy import nan

############################## PLAYSTORE APPS FILE PROCESSING #################################

#Reading the csv file

file = pd.read_csv("Data/playstoreliveproj Drive FIle/playstore_apps.csv",index_col='App')


#Removing duplicates
file.drop_duplicates(keep=False,inplace=True)

##file.info()
print(file)


#Category column
print(file['Category'].unique()) #unique values in category column
print(file[file['Category']=='1.9'])
file.drop("Life Made WI-Fi Touchscreen Photo Frame",inplace=True)
print(file['Category'].unique()) #check if irrelevant values has been removed


#consider using a while loop and or if statement in order to do each column

#Rating column
print(file['Rating'].unique()) #unique values in Rating column

#Reviews column
print(file['Reviews'].unique()) #unique values in Reviews column

#Size column
print(file['Size'].unique()) #unique values in Size column
#about 1391 / 9930 = 14% of data(after removing duplicates), therefore keep data

#Installs column
print(file['Installs'].unique()) #unique values in Installs column

#Type column
print(file['Type'].unique()) #unique values in Type column

#Price column
print(file['Price'].unique()) #unique values in Price column

#Content Rating column
print(file['Content Rating'].unique()) #unique values in Content Rating column

#Genres column
print(file['Genres'].unique()) #unique values in Genres column

#Last Updated column
print(file['Last Updated'].unique()) #unique values in Last Updated column

#Current Ver column
print(file['Current Ver'].unique()) #unique values in Current Ver column

#Android Ver column
print(file['Android Ver'].unique()) #unique values in Android Ver column
#about 1107 / 9930 = 11% of data (after removing duplicates), therefore keep data

file.to_csv("cleaned_apps_file_v1.csv")




############################## PLAYSTORE REVIEWS FILE PROCESSING #################################


#Reading the csv file

file = pd.read_csv("Data/playstoreliveproj Drive FIle/playstore_reviews.csv",index_col='App')

#Removing duplicates
file.drop_duplicates(keep=False,inplace=True) 


#Translated_Review column
print(file['Translated_Review'].unique()) #unique values in Translated_Review column

#Sentiment column
print(file['Sentiment'].unique()) #unique values in Sentiment column

#Sentiment_Polarity column
print(file['Sentiment_Polarity'].unique()) #unique values in Sentiment_Polarity column

#Sentiment_Subjectivity
print(file['Sentiment_Subjectivity'].unique()) #unique values in Sentiment_Subjectivity column

file.to_csv("cleaned_reviews_file_v1.csv")














