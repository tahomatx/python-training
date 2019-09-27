from sklearn.datasets import load_digits

digits = load_digits()

print(digits.data.shape)
print(digits.data)

print(digits.target.shape)
print(digits.target)
print(digits.target_names)

from sklearn.model_selection import train_test_split
(train_X, test_X, train_Y, test_Y) = train_test_split(digits.data, digits.target, test_size=0.2)

print(test_X)
print(test_Y)

from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report

model = Perceptron()

model.fit(train_X, digits.target_names[train_Y])

pred = model.predict(test_X)

score = accuracy_score(digits.target_names[test_Y], pred)
print('検証用データ(20%のデータ)の正解率: {}%'.format(score * 100))