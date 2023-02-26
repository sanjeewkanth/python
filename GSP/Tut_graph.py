import numpy as np
import matplotlib.pyplot as plt
from pygsp import graphs, filters, plotting

plotting.BACKEND = 'matplotlib'
plt.rcParams['figure.figsize'] = (10, 5)


W = np.array([[0, 1, 1, 0, 0],
 [1, 0, 1, 0, 1],
 [1, 1, 0, 1, 0],
 [0, 0, 1, 0, 1],
 [0, 1, 0, 1, 0]])


#W = W + W.T
#print(W)
np.fill_diagonal(W, 0)
G = graphs.Graph(W)
#print('{} nodes, {} edges'.format(G.N, G.Ne))
G.set_coordinates('ring2D')
G.plot()
