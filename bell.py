import random

# Define the number of trials and the number of measurement settings
num_trials = 1000 
num_settings = 10

# Create functions to generate random measurement outcomes
def random_outcome():
    return random.choice([1, 2])

# Initialize variables to store the outcomes
outcomes_A = []
outcomes_B = []

# Perform the Bell test experiment
for _ in range(num_trials):
    setting_A = random_outcome()
    setting_B = random_outcome()
    outcome_A = random_outcome() * setting_A
    outcome_B = random_outcome() * setting_B
    outcomes_A.append(outcome_A)
    outcomes_B.append(outcome_B)

# Calculate the correlation
correlation = sum(outcomes_A[i] * outcomes_B[i] for i in range(num_trials)) / num_trials

print(f"Correlation: {correlation}")

# Check if Bell's inequality is violated
if abs(correlation) > 2:
    print("Bell's inequality is violated!")
else:
    print("Bell's inequality is not violated.")

