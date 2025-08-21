import pandas as pd
import random

# Generate a larger dataset with name, age, and city
names = ["Alice", "Bob", "Charlie", "Diana", "Edward", "Fiona", "George", "Hannah",
         "Isaac", "Jane", "Kevin", "Laura", "Michael", "Nina", "Oscar", "Paula",
         "Quincy", "Rachel", "Sam", "Tina", "Umar", "Victoria", "William", "Xenia",
         "Yusuf", "Zara"]

cities = ["Lagos", "Ibadan", "Abuja", "Oyo", "Kano", "Port Harcourt", "Enugu", "Jos"]

# Create 100 rows of random data
data = {
    "Name": [random.choice(names) for _ in range(100)],
    "Age": [random.randint(18, 60) for _ in range(100)],
    "City": [random.choice(cities) for _ in range(100)]
}

df = pd.DataFrame(data)

# Save to CSV
df.to_csv("data/data.csv", index=False)

df.head()
