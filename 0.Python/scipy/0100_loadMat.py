import scipy.io as sio  
import numpy as np  
  
mat_path='F:/ML_EEG/08.cnn_task/data/04.stft/user1/stft1.mat'  
data=sio.loadmat(mat_path)['stft_value']

print(data.shape)