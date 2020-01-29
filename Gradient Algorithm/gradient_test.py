X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Y = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150]
theta0 = 0
theta1 = 0
alpha = 0.05


def gradient_descent(X, Y, theta0, theta1, alpha, iterations=100):
    for i in range(iterations):
        theta0_gradient = 0
        theta1_gradient = 0
        N = len(X)
        for i in range(0, len(X)):
            theta0_gradient -= (2/N) * (Y[i] - (theta0 + theta1 * X[i]))
            theta1_gradient -= (2/N) * (Y[i] - (theta0 + theta1 * X[i])) * X[i]

        theta0 = theta0 - (alpha * theta0_gradient)
        theta1 = theta1 - (alpha * theta1_gradient)

    return theta0, theta1


print(gradient_descent(X, Y, theta0, theta1, alpha))
