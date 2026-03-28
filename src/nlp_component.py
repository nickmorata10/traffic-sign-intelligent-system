from sklearn.feature_extraction.text import CountVectorizer

texts = ["stop sign", "speed limit", "yield sign"]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

print("NLP Feature Shape:", X.shape)
