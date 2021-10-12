---
layout: post
title: "Let's Learn Machine Learning (Part 1)"
tags: code-understanding ml4code
---


I have been working on deep models of source code for bug detection for a short while now. Sometimes, however, I am not completely sure why or exactly how something works or does not work. So, a few days ago, I decided to pick up a book and start learning from scratch. The book is called ["Hands-on Machine Learning with Scikit-Learn, Keras & Tensorflow"](https://learning.oreilly.com/library/view/hands-on-machine-learning/9781492032632/). I will refer to it as *the book* for brevity.

I am going to post a series of articles explaining what I learn as I continue reading this book. I will skip topics that I find irrelevant to machine learning for code.
After reviewing some basic concepts of deep learning, I will diverge from the book and focus more on machine learning specifically for code.


## Part 1: Intro

### Perceptron
Perceptron is a small unit in neural networks. It takes _n_ inputs, computes a weighted sum of them, and applies a step function or one of its variants on the weighted sum. The goal of training is to find weights that minimize the prediction error.
```
[-------------]		-->	output layer (A)
  ..\/\/\/\/..      -->	fully connected (B)
  [---------]		-->	input layer (C)
```

We are going to create a simple classifier using Perceptron that predicts the language (among C, C#, C++, D, Haskell, Java, JS, PHP, Python, and Rust) in which a program is written. For this simple example I just use the number of occurences of 22 tokens as features.

You can download the test and train data from the following links: [proglang_test](https://github.com/pardisp/pardisp.github.io/blob/main/files/2021-10-10-Learn_ML4Code_Part1/proglang_test.csv) [proglang_train](https://github.com/pardisp/pardisp.github.io/blob/main/files/2021-10-10-Learn_ML4Code_Part1/proglang_train.csv)

The following lines of code, train a multi-class classifier and evaluate it.

```python
import pandas
from sklearn.linear_model import Perceptron

data_test = pandas.read_csv('proglang_test.csv')
data_train = pandas.read_csv('proglang_train.csv')

# feature columns
X_test = data_test.iloc[:, 0:-2]
X_train = data_train.iloc[:, 0:-2]

# labels
y_test = data_test.iloc[:, -2] 
y_train = data_train.iloc[:, -2]

# train the classifier
classifier = Perceptron()
classifier.fit(X_train, y_train)

# evaluate the classifier
print('Mean accuracy:', classifier.score(X_test, y_test))
```
```
Mean accuracy: 0.95
```


### Next Topic: Multi-layer Perceptron


## References

- [1] Géron, Aurélien. Hands-on machine learning with Scikit-Learn, Keras, and TensorFlow: Concepts, tools, and techniques to build intelligent systems. O'Reilly Media, 2019.

- [2] 