# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 16:52:06 2021

@author: Admin
"""
import torch
from metric_evaluation import plot_confusion_matrix, iterate_data 


#data_dir = './source/'
data_dir = './sample/'
batchsize = 1

model = torch.load(f'./Corrosion Condition State Classification - Trained Model/l1_loss/weights_27.pt', map_location=torch.device('cuda'))
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
model.to(device)
model.eval()   # Set model to evaluate mode
##############################################################################

iOU, f1, confm_sum, y_pred = iterate_data(model, data_dir)

print('iOU: ' + str(iOU))
print('f1 score: ' + str(f1))

plot_confusion_matrix(confm_sum, target_names=['Background', 'Fair', 'Poor', 'Severe'], normalize=True, 
                      title='Confusion Matrix')
