import scipy.io as sio  
import numpy as np  
  
arr = np.ones((3,3))
fileName = 'Saved.mat'
sio.savemat(fileName, {'data': arr})