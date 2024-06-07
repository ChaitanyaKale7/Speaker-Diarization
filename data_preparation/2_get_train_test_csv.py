import csv
import random

# Read the CSV file
with open('audio_transcript_mapping.csv', 'r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Read the header
    data = list(reader)  # Read the rest of the data

# Shuffle the data to ensure randomness
random.shuffle(data)

# Define the split ratio
train_ratio = 0.6  # 60% for training and 40% for testing

# Calculate the split index
split_index = int(len(data) * train_ratio)

# Split the data
train_data = data[:split_index]
test_data = data[split_index:]

# Save the train data into train.csv
with open('train.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)  # Write the header
    writer.writerows(train_data)  # Write the train data

# Save the test data into test.csv
with open('test.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)  # Write the header
    writer.writerows(test_data)  # Write the test data

print('Data has been split into train.csv and test.csv')
