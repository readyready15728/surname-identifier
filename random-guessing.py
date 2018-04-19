import pandas as pd

surnames = pd.read_csv('surnames.csv')
ethnicities = surnames['ethnicity']
probabilities = []

for ethnicity in ethnicities.unique():
    probabilities.append((ethnicities == ethnicity).sum() / len(ethnicities))

total = 0

for p in probabilities:
    total += p**2

print('Accuracy of randoming guessing: {:.2f}%'.format(100 * total))
