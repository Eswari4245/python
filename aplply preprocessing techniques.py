import pandas as pd
import numpy as np
df = pd.read_csv(r"C:\Users\student\Desktop\exp2.csv")
print("original dataframe:\n",df)
df_selected = df[['A','B']].copy()
print("\nafter attribute selection:\n",df_selected)
df_selected ['A'].fillna(df_selected['A'].mean())
df_selected ['B'].fillna(df_selected['B'].mean())
print("\nafter handling missing values:\n",df_selected)
df_selected ['A_bin'] = pd.cut(df_selected['A'],bins = [0,4,8],labels = ['low','high'])
df_selected ['B_bin'] = pd.cut(df_selected['B'],bins = [0,3,7],labels = ['low','high'])
print("\nafter discrerization:\n",df_selected)
df_cleaned = df_selected[np.abs(df_selected['A'] - df_selected['A'].mean()) <= (3*df_selected['A'].std())]
print("selected dataframe:\n",df_selected)
print("cleaned dataframe:\n",df_cleaned)
print("\nafter elimination of outliers:\n",df_cleaned)
