import random
import json
# Set seed for reproducibility
random.seed(42)
data = []

# Read lines from file
with open('review.json', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f, 1):
        line = line.strip()  # remove leading/trailing whitespace
        if not line:
            continue  # skip empty lines
        try:
            data.append(json.loads(line))
        except json.JSONDecodeError as e:
            print(f"Skipping line {i} due to error: {e}")

random.shuffle(data)

# Split percentages
train_ratio = 0.8
val_ratio = 0.1
test_ratio = 0.1

# Compute split indices
n = len(data)
train_end = int(train_ratio * n)
val_end = train_end + int(val_ratio * n)

# Split the data
train_data = data[:train_end]
val_data = data[train_end:val_end]
test_data = data[val_end:]

# Write to files
with open("train.json", "w") as f:
    for review in train_data:
        f.write(json.dumps(review) + '\n')

with open("val.json", "w") as f:
    for review in val_data:
        f.write(json.dumps(review) + '\n')

with open("test.json", "w") as f:
    for review in test_data:
        f.write(json.dumps(review) + '\n')
