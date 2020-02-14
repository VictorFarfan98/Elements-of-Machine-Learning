import numpy as np
import matplotlib.pyplot as plt

X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

theta = np.random.randn(2, 1)
alpha = 0.01


def cost(theta, X, y):
    n = len(X)

    predictions = X.dot(theta)
    return (n/2) * np.sum(np.square(predictions-y))


def gradient_vectorized(X, y, theta, learning_rate=0.01, iterations=1000):
    N = len(X)
    cost_history = np.zeros(iterations)
    prediction_history = np.zeros(iterations)
    for i in range(iterations):

        prediction = np.dot(X, theta)
        theta = theta - (1/N)*learning_rate*(X.T.dot((prediction - y)))
        cost_history[i] = cost(theta, X, y)

    return theta, cost_history, prediction


X_b = np.c_[np.ones((len(X), 1)), X]

theta, cost_history, y_history = gradient_vectorized(X_b, y, theta)

print('Theta0:          {:0.2f},\nTheta1:          {:0.2f}'.format(
    theta[0][0], theta[1][0]))

"""
plt.plot(X, y, 'b.')
plt.xlabel("$x$", fontsize=18)
plt.ylabel("$y$", rotation=0, fontsize=18)
_ = plt.axis([0, 2, 0, 15])
plt.show()
"""
plt.plot(X, y_history, 'r-')
plt.plot(X, y, 'b.')
plt.xlabel("$x_1$", fontsize=18)
plt.ylabel("$y$", rotation=0, fontsize=18)
plt.axis([0, 2, 0, 15])
plt.show()

fig, ax = plt.subplots(figsize=(12, 8))

ax.set_ylabel('J(Theta)')
ax.set_xlabel('Iterations')
_ = ax.plot(range(1000), cost_history, 'b.')
plt.show()
