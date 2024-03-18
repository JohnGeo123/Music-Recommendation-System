import pandas as pd

# Load user data
users_df = pd.read_csv('data/users.csv')

# Load listening history data
listening_history_df = pd.read_csv('data/listening_history.csv')

# Data preprocessing steps (e.g., handling missing values, encoding categorical variables)
# ...

# Save preprocessed data
users_df.to_csv('data/users_processed.csv', index=False)
listening_history_df.to_csv('data/listening_history_processed.csv', index=False)
