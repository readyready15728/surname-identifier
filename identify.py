from collections import Counter
import Levenshtein
import pandas as pd
from sklearn import neighbors
from sklearn.model_selection import train_test_split

surnames = pd.read_csv('surnames.csv')
N = 7

X = surnames['surname']
y = surnames['ethnicity']

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, stratify=y)

# sklearn doesn't allow string data even with a custom metric so I have to do
# this sloppy shit instead
fit = dict(zip(X_train, y_train))
hits = 0

for test_surname, label in zip(X_test, y_test):
    distances = {}

    for train_surname in fit:
        distances[train_surname] = Levenshtein.distance(train_surname, test_surname)

    nearest_neighbors = [surname for surname, _ in sorted(list(distances.items()), key=lambda pair: pair[1])][:N]
    ethnicities = Counter()

    for neighbor in nearest_neighbors:
        ethnicities[fit[neighbor]] += 1

    predicted_ethnicity = ethnicities.most_common()[0][0]
    
    if predicted_ethnicity == label:
        hits += 1

    print('Test surname: {}'.format(test_surname))
    print('Predicted ethnicity: {}'.format(predicted_ethnicity))
    print('Real ethnicity: {}'.format(label))
    print()

print('Accuracy: {:.2f}%'.format(100 * hits / len(X_test)))
