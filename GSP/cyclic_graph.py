import numpy as np
import matplotlib.pyplot as plt
from pygsp import graphs, filters, plotting

plotting.BACKEND = 'matplotlib'
plt.rcParams['figure.figsize'] = (10, 5)


W = np.array([[0, 1, 0, 0, 1],
 [1, 0, 1, 0, 0],
 [0, 1, 0, 1, 0],
 [0, 0, 1, 0, 1],
 [1, 0, 0, 1, 0]])

D = ([[2, 0, 0, 0, 0],
      [0, 2, 0, 0, 0],
      [0, 0, 2, 0, 0],
      [0, 0, 0, 2, 0],
      [0, 0, 0, 0, 2]])

L = D - W
print(L)
l = (D^-1/2)*L*(D^-1/2)
print(l)

np.fill_diagonal(W, 0)
G = graphs.Graph(W)
#print('{} nodes, {} edges'.format(G.N, G.Ne))
G.set_coordinates('ring2D')
G.plot()

