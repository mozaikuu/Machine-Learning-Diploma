import random
import pandas as pd

users = ["User1", "User2", "User3", "User4", "User5"]
activation_types = ["light", "sound", "shock"]

# Simulate reaction times and logs for 500000 entries
data_simulated_large = {
    "user": [random.choice(users) for _ in range(50000)],
    "reaction_speed(in_ms)": [random.randint(0, 1000) for _ in range(50000)],
    "type_of_activation": [random.choice(activation_types) for _ in range(50000)],
}

# Create a DataFrame
updated_data_large = pd.DataFrame(data_simulated_large)

# Save the larger dataset to the file
updated_large_file_path = './Datasets/Fake_Shocking_medium(50000)_dataset.csv'
updated_data_large.to_csv(updated_large_file_path, index=False)

# Display the first few rows of the updated dataset
updated_data_large.head(), updated_large_file_path
