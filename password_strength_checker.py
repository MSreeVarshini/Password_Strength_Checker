'''
    Created By M. Sree Varshini
'''

# Importing the necessary Python libraries and the dataset that are required for password strength checker:

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import getpass

data = pd.read_csv("PSC.csv", on_bad_lines='skip')
# print(data.head())

# Transforming integer strength of a password to verbal
data = data.dropna()
data["strength"] = data["strength"].map({0: "Weak", 1: "Medium", 2: "Strong"})


print(data.sample(10))


# Defining a machine learning model for Password Strength Prediction:
def word(password):
    character = []
    for i in password:
        character.append(i)
    return character


x = np.array(data["password"])
y = np.array(data["strength"])
tfid = TfidfVectorizer(tokenizer=word, token_pattern=None)
x = tfid.fit_transform(x)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=20, random_state=42)

model = RandomForestClassifier()
model.fit(x_train, y_train)
print(model.score(x_test, y_test))


user = getpass.getpass("Enter your password: ")
data = tfid.transform([user]).toarray()
output = model.predict(data)
assert isinstance(output, object)
print(output)
