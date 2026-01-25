import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, OrdinalEncoder

def label_encoding(df, columns):
    df_le = df.copy()
    le = LabelEncoder()
    for col in columns:
        df_le[col] = le.fit_transform(df_le[col])
    return df_le

def one_hot_encoding(df, columns):
    df_ohe = pd.get_dummies(df, columns=columns, drop_first=False)
    return df_ohe

def ordinal_encoding(df, columns, categories):
    df_ord = df.copy()
    oe = OrdinalEncoder(categories=categories)
    df_ord[columns] = oe.fit_transform(df_ord[columns])
    return df_ord

def frequency_encoding(df, columns):
    df_freq = df.copy()
    for col in columns:
        freq_map = df_freq[col].value_counts() / len(df_freq)
        df_freq[col] = df_freq[col].map(freq_map)
    return df_freq

def target_encoding(df, column, target):
    df_te = df.copy()
    target_mean = df_te.groupby(column)[target].mean()
    df_te[column] = df_te[column].map(target_mean)
    return df_te
