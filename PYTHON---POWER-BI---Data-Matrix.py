import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Assuming your data is loaded into a Pandas DataFrame named 'df'
# Modify this part according to your dataset

# Example data
data = {
    'A': np.random.rand(10),
    'B': np.random.rand(10),
    'C': np.random.rand(10),
    'D': np.random.rand(10)
}

df = pd.DataFrame(data)

# Create a matrix plot
plt.matshow(df.corr())
plt.xticks(range(len(df.columns)), df.columns)
plt.yticks(range(len(df.columns)), df.columns)
plt.colorbar()
plt.show()
