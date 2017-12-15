import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets.samples_generator import make_blobs
from mpl_toolkits.mplot3d import Axes3D


X, y = make_blobs(200, 2, centers=[[-10,-10], [-10, 10], [10, 10], [10, -10]], cluster_std=4.0)
# y = [1, 2, 1, 2]
i3 = np.where(y == 2)
i4 = np.where(y == 3)
y[i3] = 0
y[i4] = 1


from sklearn.svm import SVC


def plot_svc_decision_function(model, X, y, ax=None, plot_support=True):
    """Plot the decision function for a 2D SVC"""

    ax.scatter(X[:, 0], X[:, 1], c=y, s=20, cmap='autumn')

    if ax is None:
        ax = plt.gca()
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    
    # create grid to evaluate model
    x = np.linspace(xlim[0], xlim[1], 50)
    y = np.linspace(ylim[0], ylim[1], 50)
    X, Y = np.meshgrid(x, y)
    xy = np.vstack([X.ravel(), Y.ravel()]).T
    P = model.decision_function(xy).reshape(X.shape)
    
    # plot decision boundary and margins
    contour = ax.contour(X, Y, P, levels=[-1, 0, 1], alpha=0.5,
               colors='k'
               )
    plt.clabel(contour, inline=True, fontsize=8)
    # plt.contour(X, Y, P, 20, cmap='RdGy')

    im = ax.imshow(P[::-1], extent=[xlim[0], xlim[1], ylim[0], ylim[1]],
           cmap='RdGy', alpha=0.5)
    # ax.colorbar()
    plt.gcf().colorbar(im)
    
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
    ax.set_title('rbf kernel')

def plot_3D(ax, model, X=X, Y=y):

    # create grid to evaluate model
    P = model.decision_function(X)

    ax.scatter3D(X[:, 0], X[:, 1], P, c=Y, cmap='autumn')
    ax.view_init(elev=30, azim=30)
    ax.set_title('3D')

###################################################################
figure = plt.figure(1, figsize=(15, 6))
ax1 = figure.add_subplot(121)

# fig, ax = plt.subplots(1, 2, figsize=(16, 6))

model = SVC(kernel='rbf', C=50)
model.fit(X, y)
plot_svc_decision_function(model, X, y, ax1, plot_support=False)


ax2 = figure.add_subplot(122, projection='3d')
plot_3D(ax2, model)

###################################################################
from sklearn.datasets.samples_generator import make_circles

fig2 = plt.figure(2, figsize=(14, 6))
ax3 = fig2.add_subplot(121)

X, y = make_circles(100, factor=.1, noise=.1)

clf = SVC(kernel='rbf').fit(X, y)

ax3.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='autumn')
plot_svc_decision_function(clf, X, y, ax3, plot_support=False)

ax4 = fig2.add_subplot(122, projection='3d')
plot_3D(ax4, clf, X, y)

plt.show()