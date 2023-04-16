#import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns
sns.set(style = "white", color_codes = True)
sns.set(font_scale = 1.5)

import warnings
warnings.filterwarnings('ignore')


#Import CSV file
df = pd.read_csv(r'C:\Users\User\Documents\Python Scripts\Data Analytics GP1\heart.csv')
print(df)
print(df.head())

description = pd.read_csv(r'C:\Users\User\Documents\Python Scripts\Data Analytics GP1\heart-glossary.csv')
print(description)

#DATA CLEANING
print(df.shape)
print(df.dtypes)

#Convert 1,0 
df['sex'] = df['sex'].apply(lambda x: 'Male' if x==1 else 'Female')

#Converting datatype
columns_to_convert_bool = ['exang', 'target']
df[columns_to_convert_bool] = df[columns_to_convert_bool].astype('bool')
print(df.dtypes)

#Check for missing data
missing_data = df.isnull().values.any()
print(missing_data)

# Percentage by column of missing data 
missingdata_percentage_bycolumn = df.isnull().sum().sort_values(ascending = False)/len(df)
print(missingdata_percentage_bycolumn)

# heatmap for missing data
# plt.figure(figsize = (15, 10))
# sns.heatmap(df.isna().transpose(),
#            cmap = "YlGnBu",
#            cbar_kws = {'label':'Missing Data'})
# plt.savefig("Visualizing_missing_data_with_heatmap_Seaborn_Python.png", dpi = 100)

#Dataset Statistic
print(df.describe())

# Visualization of Data
fig, axes = plt.subplots(figsize=(12, 8), nrows=2, ncols=2)

sns.histplot(data=df, x='age', kde=True, ax=axes[0, 0])
axes[0, 0].set_title('Age Distribution')

sns.countplot(data=df, x='sex', ax=axes[0, 1])
axes[0, 1].set_title('Sex Distribution')

sns.countplot(data=df, x='exang', ax=axes[1, 0])
axes[1, 0].set_title('Exercixed Induced Chest Pain Distribution')

sns.countplot(data=df, x='cp', ax=axes[1, 1])
axes[1, 1].set_title('Chest Pain Distribution')

plt.subplots_adjust(hspace=0.5, wspace=0.3)


#data preprocessing
df['sex'] = df['sex'].apply(lambda x: 1 if x=='Male' else 0)
print(df.corr())

plt.figure(figsize = (45, 18))
sns.heatmap(df.corr(), annot = True, cmap = 'viridis_r')
plt.title("Correlation Heatmap", fontsize = 50)
plt.show()