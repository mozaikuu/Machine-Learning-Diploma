import pandas as pd
import numpy as np

np.random.seed(0)

species_counts = np.random.randint(100, 300, size = 100)
areas = ['area' + str(i) for i in range(1, 101)]
data = {'area': areas, 'species_count': species_counts}

df = pd.DataFrame(data)


# pop mean
pop_mean = df['species_count'].mean()


# sample mean
sample = np.random.choice(df['species_count'], 10)
sample_mean = sample.mean()

# print(df.head())

print('sample: ', sample)
print('population mean: ', pop_mean)
print('sample mean: ', sample_mean)

