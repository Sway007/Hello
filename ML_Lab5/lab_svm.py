import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets.samples_generator import make_blobs

X, y = make_blobs(200, 2, centers=[[-10,-10], [-10, 10], [10, 10], [10, -10]], cluster_std=4.0)
# y = [1, 2, 1, 2]
i3 = np.where(y == 2)
i4 = np.where(y == 3)
y[i3] = 0
y[i4] = 1
print(y)

plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='autumn')


from sklearn.svm import SVC

def plot_svc_decision_function(model, ax=None, plot_support=True):
    """Plot the decision function for a 2D SVC"""
    if ax is None:
        ax = plt.gca()
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    
    # create grid to evaluate model
    x = np.linspace(xlim[0], xlim[1], 30)
    y = np.linspace(ylim[0], ylim[1], 30)
    Y, X = np.meshgrid(y, x)
    xy = np.vstack([X.ravel(), Y.ravel()]).T
    P = model.decision_function(xy).reshape(X.shape)
    
    # plot decision boundary and margins
    ax.contour(X, Y, P, colors='k',
               levels=[-1, 0, 1], alpha=0.5,
               linestyles=['--', '-', '--'])
    
    # plot support vectors
    if plot_support:
        ax.scatter(model.support_vectors_[:, 0],
                   model.support_vectors_[:, 1],
                   s=300, linewidth=1
                   , alpha=0.3
                #    , facecolors='none'
                   )
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)

model = SVC(kernel='rbf', C=0.1)
model.fit(X, y)
plot_svc_decision_function(model, plot_support=False)

plt.show()