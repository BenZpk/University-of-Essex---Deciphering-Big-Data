#Follow the instructions on page 150-151 of the Data Wrangling with Python textbook
#to manually produce data files mn.csv and mn_headers.csv.

# First I import the necessary libraries
import pandas as pd
import numpy as np

# Read the headers file
headers_df = pd.read_csv('mn_headers.csv', encoding='utf8')

# Read the data file
data_df = pd.read_csv('mn.csv', encoding='utf8', dtype={110: str, 111: str, 112: str, 120: str})

# I drop the index columm
data_df = data_df.drop('Unnamed: 0', axis=1)

# Comparison of headers and check for differences:

# Take labels from headers file
old_headers = data_df.columns.tolist()
new_headers = headers_df['Name'].tolist()

# I check which headers only exist in the data df and not in header df
# I use NumPy's setdiff method:
diff = np.setdiff1d(old_headers, new_headers, assume_unique=False)
print(diff)

# The missing headers can be found at: https://microdata.worldbank.org/

# I now insert the new headers and describe the resulting df:

# Take names & labels from headers file
labels = headers_df['Label'].tolist()

# Replace headers in the data df, using labels for matching names
replaced_headers = []

# Loop through the old headers
for old_header in data_df.columns.tolist():
    # Check if the header exists in the headers df
    for i, name in enumerate(new_headers):
        # Both must match and label must be available
        if old_header.lower() == name.lower() and labels[i] not in [None, '']:
            replaced_headers.append(labels[i])
            break
    else:
        replaced_headers.append(old_header)

# Create a copy to keep the original dataframe
df = data_df.copy()

df.columns = replaced_headers
#Additionally, rename the columns that are missing in the headers df with the data I found on the linked website
df.rename(columns={
    "MDV1F": "If she commits infidelity: wife beating justified",
    "MTA8E": "Type of smoked tomacco product: Rolled tobacco",
    "mnweight": "Man sample weight",
    "mwelevel": "Education",
    "windex5r": "Rural wealth index quintile",
    "windex5u": "Urban wealth index quintile",
    "wscorer": "Rural wealth score",
    "wscoreu": "Urban wealth score"
}, inplace=True)

# Set the correct shape for the resulting dataframe
pd.options.display.max_columns = df.shape[1]
pd.options.display.max_rows = df.shape[0]
# Print statistical measures like, e.g., mean and standard deviation for the updated dataframe with the describe method
print(df.describe(include='all'))
# Overall, now we have fixed the first problem and inserted the correct headers and printed out main statistical measures for all variables.

# Next, we count the number of null values we have
print(df.isnull().sum())
# We see that many of the columns contain null values, some of them significant amounts of > 9,000

# I next check the data types of the variables:
print(df.dtypes)

# Dependent on the data types I can now split up the variables into numerical and categorical:
categorical = df.select_dtypes(include=['object', 'category']).columns
numeric = df.select_dtypes(include=['int', 'float']).columns

# Now I can print the distinct values for each categorical variable:
for col in categorical:
    unique_vals = df[col].unique()
    print(f"Unique values in column '{col}':")
    print(unique_vals)
    print()

# I now check for duplicate rows:
duplicate_rows = df.duplicated()
# Select only the part of the data frame with duplicate rows
duplicate_data = df[duplicate_rows]
# Print it out
print(duplicate_data)
# We see that there are no duplicate rows in the dataframe that we would need to process further.

# Change the type of the 'Start of interview - Hour' variable to datetime
# Catch ValueErrors by turning the values to Null values in case such an error is faced
problems = []
try:
    df['Start of interview - Hour'] = pd.to_datetime(df['Start of interview - Hour'], format='%H').dt.time
except ValueError as e:
    problems = df['Start of interview - Hour'][pd.to_datetime(df['Start of interview - Hour'], format='%H', errors='coerce').isnull()]

# Print the problematic values
print("Problematic values:")
print(problems)

#Create three new columns: start time, end time and duration given as difference between start and end time:
# Combine date, hour, and minute columns and create a new column for the start of the interview as datetime
df['Interview Start'] = pd.to_datetime(
    df['Year of interview'].astype(str) + '-' +
    df['Month of interview'].astype(str) + '-' +
    df['Day of interview'].astype(str) + ' ' +
    df['Start of interview - Hour'].astype(str) + ':' +
    df['Start of interview - Minutes'].astype(str), errors='coerce'
)

# Combine date, hour, and minute columns summed up in a new column for the end of interview in datetime data type
df['Interview End'] = pd.to_datetime(
    df['Year of interview'].astype(str) + '-' +
    df['Month of interview'].astype(str) + '-' +
    df['Day of interview'].astype(str) + ' ' +
    df['End of interview - Hour'].astype(str) + ':' +
    df['End of interview - Minutes'].astype(str), errors='coerce'
)

# Calculate the duration between the start and end of the interview
df['Interview Duration'] = df['Interview End'] - df['Interview Start']

# I now print out the head (fisrt 10 values only) of each of the three variables
# to show that the definition worked out correctly
print(df['Interview Start'].head(10))
print(df['Interview Duration'].head(10))
print(df['Interview End'].head(10))
# We see that we have quite a lot missing values but that the definition of the variables worked out well.