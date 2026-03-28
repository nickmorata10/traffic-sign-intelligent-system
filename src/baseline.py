import numpy as np
from sklearn.linear_model import LogisticRegression

# Fake dataset
X = np.random.rand(100, 5)
y = np.random.randint(0, 2, 100)

model = LogisticRegression()
model.fit(X, y)

accuracy = model.score(X, y)
print("Baseline Accuracy:", accuracy)
