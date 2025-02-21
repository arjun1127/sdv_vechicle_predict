import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# Load the dataset
df = pd.read_csv("traffic_data.csv")

# Drop unnecessary columns (keeping only useful numerical data)
df = df[["TimeStep", "Speed", "X", "Y"]]

# Normalize the Speed, X, and Y columns
scaler = MinMaxScaler()
df[["Speed", "X", "Y"]] = scaler.fit_transform(df[["Speed", "X", "Y"]])

# Convert data into sequences for LSTM
sequence_length = 10  # Number of time steps to look back
X, y = [], []

for i in range(len(df) - sequence_length):
    X.append(df.iloc[i:i+sequence_length].values)  # Input sequence
    y.append(df.iloc[i+sequence_length]["Speed"])  # Target value (speed prediction)

# Convert to NumPy arrays
X, y = np.array(X), np.array(y)

# Save processed data
np.save("X_traffic.npy", X)
np.save("y_traffic.npy", y)

print("Preprocessing complete! Saved X_traffic.npy and y_traffic.npy")
