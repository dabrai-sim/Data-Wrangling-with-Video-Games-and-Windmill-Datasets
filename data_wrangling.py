#importing libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#importing datasets
vgs_df=pd.read_csv('Video_Game_Sales_dataset.csv')
wind_df=pd.read_excel('Windmill Dataset.xlsx')

#Find missing values

# finding missing values for the video games dataset
vgs_df.isna().sum()

#finding datatypes of columns in the video game dataset
vgs_df.dtypes

#finding missing values for the windmill dataset
wind_df.isna().sum()

#Fill missing values using k-nn imputation techniques
#for filling missing values in the rating column the forward fill imputation technique is used
vgs_df['Rating'].fillna(method='ffill',inplace=True)

Before_imputation_vgs_df=pd.DataFrame(data=[],columns=['Critic_Score','Critic_Count','User_Score','User_Count','Year_of_Release'])
Before_imputation_vgs_df["Critic_Score"]=vgs_df["Critic_Score"]
Before_imputation_vgs_df["Critic_Count"]=vgs_df["Critic_Count"]
Before_imputation_vgs_df["User_Score"]=vgs_df["User_Score"]
Before_imputation_vgs_df["User_Count"]=vgs_df["User_Count"]
Before_imputation_vgs_df["Year_of_Release"]=vgs_df["Year_of_Release"]

#using knn imputation technique to impute data in the  columns Critic_Score,Critic_Count,User_Score,User_Count as they have a numeric data type

#importing the knn imputer
from sklearn.impute import KNNImputer

#creating an imputation object
imputer=KNNImputer(n_neighbors=2)
#performing KNN Imputation on dataset
After_imputation_vgs=imputer.fit_transform(Before_imputation_vgs_df)
After_imputation_vgs_df=pd.DataFrame(After_imputation_vgs,columns=Before_imputation_vgs_df.columns)

After_imputation_vgs_df

vgs_df["Critic_Score"]=After_imputation_vgs_df["Critic_Score"]
vgs_df["Critic_Count"]=After_imputation_vgs_df["Critic_Count"]
vgs_df["User_Score"]=After_imputation_vgs_df["User_Score"]
vgs_df["User_Count"]=After_imputation_vgs_df["User_Count"]
vgs_df["Year_of_Release"]=After_imputation_vgs_df["Year_of_Release"]
vgs_df.dropna(inplace=True)
vgs_df.isna().sum()

#Select all the Sports video games from the video games dataset.
vgs_df[vgs_df.Genre=='Sports']

#Which video games had global sales greater than 50?
vgs_df[vgs_df['Global_Sales']>50.00]

#Load the video games dataframe in descending order by Name
vgs_df.sort_values(by='Name', ascending=False)

#What genre games have been made the most?
vgs_df['Genre'].max()

#Which year had the most game release?
vgs_df['Year_of_Release'].max()

#Which year had the highest sales worldwide?
vgs_df.Year_of_Release[vgs_df['Global_Sales']==vgs_df['Global_Sales'].max()]

#Which genre game has been released the most in a single year?
vgs_df.groupby(['Year_of_Release', 'Genre'])['Genre'].count().idxmax()
#vgs_df.Genre[vgs_df['Year_of_Release'] == vgs_df['Year_of_Release'].count().max()]
#h_sales=dict(vgs_df.groupby('Year_of_Release')['Global_Sales'].size())

#Which genre game has the highest sale price globally?
vgs_df.Genre[vgs_df['Global_Sales']==vgs_df['Global_Sales'].max()]

#Plot a scatter plot of Wind speed vs Power Output
plt.scatter(wind_df['Wind Speed (m/s)'],wind_df['Power output (MW)'])
plt.show()

#Which windmill had maximum and minimum windspeed?
#maximum windspeed
wind_df[wind_df['Wind Speed (m/s)']==wind_df['Wind Speed (m/s)'].max()]
#minimum windspeed
wind_df[wind_df['Wind Speed (m/s)']==wind_df['Wind Speed (m/s)'].min()]

#Which windmill had maximum and minimum power output
#maximum power output
wind_df[wind_df['Power output (MW)']==wind_df['Power output (MW)'].max()]
#minimum power output
wind_df[wind_df['Power output (MW)']==wind_df['Power output (MW)'].min()]
