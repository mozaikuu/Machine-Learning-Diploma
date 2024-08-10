import polars as pr


df = pr.read_csv('./Datasets/adult.csv')

# print(df['age'])


filtered_df = df[df['age'] < 50]
print(filtered_df)