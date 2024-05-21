import pandas as pd
import random
from faker import Faker

fake = Faker()

def generate_message(spam=True):
    if spam:
        templates = [
            "Congratulations! You've won a $1000 {} gift card. Click here to claim now.",
            "Free entry in 2 a wkly comp to win {} final tkts 21st May 2005. Text FA to 87121 to receive entry question(std txt rate)",
            "URGENT! Your Mobile number has been awarded a £2000 prize!",
            "WINNER!! As a valued network customer you have been selected to receive a £900 prize reward!",
        ]
        brand = fake.company()
        return random.choice(templates).format(brand)
    else:
        return fake.text()

# Generate the dataset
data = {
    'v1': [],
    'v2': []
}

for _ in range(1000000):
    if random.random() < 0.15:  # 15% spam, 85% ham
        data['v1'].append('spam')
        data['v2'].append(generate_message(spam=True))
    else:
        data['v1'].append('ham')
        data['v2'].append(generate_message(spam=False))

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV
output_path = 'synthetic_spam_dataset.csv'
df.to_csv(output_path, index=False)
print(f"Generated dataset saved to {output_path}")
