import numpy as np

# Define input vectors
X = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0]])

# Set initial weight vector
W = np.array([[1, 0, 0, 0], [0, 1, 0, 0]])

# Set learning rate and number of epochs
alpha_initial = 0.6
num_epochs = 100

# Define function for updating learning rate
def update_learning_rate(alpha_initial, k):
    return alpha_initial / k

# Kohonen SOM algorithm
for epoch in range(num_epochs):
    alpha = update_learning_rate(alpha_initial, epoch+1)
    for x in X:
        # Calculate distances between input vector and weight vectors
        distances = np.linalg.norm(x - W, axis=1)
        # Find index of closest weight vector
        winner = np.argmin(distances)
        # Update weights of winning neuron and its neighbors
        for i in range(W.shape[0]):
            if abs(i - winner) <= 0:
                W[i] += alpha * (x - W[i])

# Display final weight vector
print("Final weight vector:")
print(W)

# Test with s(5)
s5 = np.array([1, 1, 1, 0])
distances = np.linalg.norm(s5 - W, axis=1)
winner = np.argmin(distances)
print("s(5) belongs to cluster", winner+1)
#########
Final weight vector:
[[0.76078431 0.76078431 0.22352941 0.        ]
 [0.22352941 0.22352941 0.76078431 0.76078431]]
s(5) belongs to cluster 1
