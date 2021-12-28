---
layout: post
title: "Perceptron, MLP, and Backpropagation"
tags: code-understanding ml4code
---


### Perceptron
Perceptron is a small unit in neural networks. It takes _n_ inputs, computes a weighted sum of them, and applies a step function or one of its variants on the weighted sum. The goal of training is to find weights that minimize the prediction error.

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


### Multi-layer Perceptron
A multi-layer perceptron has 1) one input layer, 2) a number of hidden layers, and 3) an output layer. The building blocks in this kind if network is the Perceptron. Each layer is fully connected to the next layer. The message passes in one direction (from lower layer to upper layers) so it is conviniently called _feed forward_ network. If there are several hidden layers then it is called a _deep_ network.

### Backpropagation
After the weights of the model is set to random values, one small batch of samples are run through the network in _forward_ direction until it makes the final predictions. Then, the error is measured in reverse---or _backwards_---for each layer with the goal of finding how much each connection contributes to the error. Finally, the weights are re-adjusted based on the computed values.
As I mentioned earlier, in the original Perceptron, a step function was used at the final step. In modern MLPs, however, this step function is replaced by other _activation_ functions such as _tanh_ and _relu_.

## References

- Géron, Aurélien. Hands-on machine learning with Scikit-Learn, Keras, and TensorFlow: Concepts, tools, and techniques to build intelligent systems. O'Reilly Media, 2019.