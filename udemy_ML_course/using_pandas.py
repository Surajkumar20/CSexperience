""" Pandas Series = NUMPY ARRAY """
""" Index of a series can be non-numerical"""

import numpy as np
import pandas as pd


my_list = [1,2,3,4,5]
my_labels = ['A', 'B', 'C', 'D', 'E']
np_array = np.array([10,20,30,40,50])
my_dict = {'A':10, 'B':20, 'C':30, 'D':40, "E":50}

""" Basic version of pandas series """
print("\nBasic Pandas Series")
print(pd.Series(data=my_list))

""" Giving custom labels to the data """
print("\nCustom Pandas array with my own labels")
print(pd.Series(data=my_list, index=my_labels))

""" Converting a python dictionary to a pandas series """
print("\nConverting a python dictionary into a pandas series")
print(pd.Series(my_dict))

""" Manually making my own pandas series """
print("\nMaking my own pandas series")
print(pd.Series([10, 20, 30, 60, 70], 'A B E F G'.split()))

""" Adding two pandas series together """
ser_1 = pd.Series([13, 22, 13, 64, 25], 'A B F E G'.split())
ser_2 = pd.Series(data=my_list, index=my_labels)
print("\nAdding both pandas series together")
print(ser_1 + ser_2)

""" Using a numpy random array """
print("\nCreating a pandas data frame")
a = np.random.seed(42)
df = pd.DataFrame(np.random.randn(5,4), index='A B C D E'.split(), columns='PENIS COCK DICK FAG'.split())
print(df)
print("Note: A data frame is an array, an array is two pandas series sharing the same index")

""" Adding on a column to the existing table """
df['cock + penis'] = df['COCK'] + df['PENIS']
print("\nImproved dataframe")
print(df)

""" Dropping a column/row from the table """
df.drop("FAG", axis=1, inplace=True)
print("\nRemoved a column so that I don't get cancelled")
print(df)

""" Extracting a whole row from a dataframe """
print("\nExtracting a single row ({}) from the whole dataframe".format('D'))
print(df.loc['D'])
print("\nUsing numerical index")
print(df.iloc[0])
print("\nTaking multiple rows ")
#print(df.loc(['A', 'B'], ['PENIS', 'COCK']))

""" Numerical comparison """
print("\nUsing numerical comparison, similar to in MATLAB")
print(df > 0)

""" MATLAB style logical indexing """
print("\nUsing logical indexing, similar to in MATLAB")
df_indedxed = df[(df['PENIS'] < 0) & (df['COCK'] is True)]
print(df_indedxed)

""" LEAVE SPACE FOR OTHER THINGS TO BE PUT IN """


""" Read from csv file """
print("Reading in from a CSV file")
df_csv = pd.read_csv('test_csv.csv')
print("This is the X col of the data:\n {}\n\n".format(df_csv['X']))

""" Plotting the data """
import matplotlib.pyplot as plt
plt.plot(df_csv['X'], df_csv['Y'])
plt.title("Y against randomized X values")
plt.xlabel("Randomized X values")
plt.ylabel("Y values")
plt.show()

""" Plotting the histogram of one column of data """
df['COCK'].hist()

""" Using scikit-learn """
from sklearn.linear_model import LinearRegression
x_data = np.array(df_csv['X']).reshape((-1,1))
y_data = np.array(df_csv['Y']).reshape((-1,1))
lin_reg = LinearRegression().fit(x_data, y_data)
r_sq = lin_reg.score(x_data, y_data)
gradient = lin_reg.coef_
intercept = lin_reg.intercept_
print("m = {} & c = {}".format(gradient, intercept))
x_pred = np.array([500000]).reshape((1, -1))
y_pred = lin_reg.predict(x_pred)
print('For x = {}, y = {}'.format(x_pred, y_pred))

