# Scikit-Learn and Shallow Learning
# Visualization
import matplotlib.pyplot as plt
# Data manipulation and processing
import pandas as pd
import seaborn as sns
# TF and Keras-related imports

df = pd.read_csv('AmesHousing.csv')
df.drop(['Order', 'PID'], axis=1, inplace=True)

print(df['SalePrice'].describe().apply(lambda x: '{:,.1f}'.format(x)))
