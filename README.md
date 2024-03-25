# Password Strength Checker with Machine Learning

Password Strength Checker is an application that checks how strong a password is. Some popular password strength meters use machine learning algorithms to predict the strength of your password. So, if you want to learn how to use machine learning to check your password's strength, this repo is for you. In this repository, I'll take you through how to create a password strength checker with machine learning using Python.



### How to create a Password Strength Checker?

A password strength checker works by understanding the combination of digits, letters, and special symbols you use in your password. It is created by training a machine learning model on a labelled dataset of different combinations of letters and special symbols can be classified as a strong or weak password.
So, to create an application to check the strngth of passwords, we need to have a labelled dataset about different combinations of letters and symbols. I found a dataset on Kaggle to train a machine learning model to predict the strength of a password. We can use that data for this task.

We've started by importing the necessary Python libraries and the dataset that we needed for our task. The dataset has 2 columns (password and strength). In the strength column, O means the password’s strength is weak, 1 means the password’s strength is medium and 2 means the password’s strength is strong. Before moving forward, I've converted 0, 1, 2 values from strength column to weak, medium, strong.



### Password Strength Prediction Model
Now, it's time to train the machine learning model to predict the strength of the password. Before we start preparing the model, we need to tokenize the passwords as we need the model to learn from the combinations of digits, letters, and symbols to predict the password's strength and split the data into training and test sets. Later, the model is trained to predict the strength of the password using Random Forest Classifier.
The strength of the password is checked using the trained model with the help of Term Frequency – Inverse Document Frequency (tfid vectorizer).


This is how you can use machine learning to create a passwor strength checker using python. A password strength checker works by understanding the combination of digits, letters, and special symbols that are generally used in passwords. 



I hope you liked this article on creating a password strength checker with machine learning using python :)
