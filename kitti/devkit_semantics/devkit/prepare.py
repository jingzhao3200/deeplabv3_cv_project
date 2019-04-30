import scipy.misc as sp
import matplotlib.pyplot as plt

import os
os.chdir('../../data_semantics/training/')
print (os.getcwd())

# reading the instance and semantic segmentation ground truth from the combined ground truth file

imageName = '000000_10'
im = sp.imread('image_2/'+imageName+'.png')
plt.imshow(im)
plt.show()

semantic_gt = sp.imread('semantic/'+imageName+'.png')
plt.imshow(semantic_gt)
plt.show()

print(semantic_gt.shape)


