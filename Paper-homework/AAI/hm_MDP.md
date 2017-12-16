## 1). Discuss the similarities and differences between supervised learning, reinforcement learning and unsupervised learning.

A:  
**Supervised Learning**  

* A human builds a classifier based on input and output data
* That classifier is trained with a training set of data
* That classifier is tested with a test set of data

**Unsupervised Learning**

* A human builds an algorithm based on input data
* That algorithm is tested with a test set of data (in which the algorithm creates the classifier)

**Reinforcement Learning**

* A human builds an algorithm based on input data
* That algorithm presents a state dependent on the input data in which a user rewards or punishes the algorithm via the action the algorithm took, this continues over time
* That algorithm learns from the reward/punishment and updates itself, this continues
* It's always in production, it needs to learn real data to be able to present actions from states

## 2).What does a Bellman equation describe in MDPs?

A: the relation between the current state-value function and immediate reward, discounted value of successor state