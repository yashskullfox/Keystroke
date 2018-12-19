#False Acceptance and False Rejection rate at threshold=0.5 for N=200
from scipy.spatial.distance import cityblock 
import numpy as np
import pandas

path = "/Users/yashpatel/Desktop/kdata.csv" 
data = pandas.read_csv(path)
subjects = data["subject"].unique()
usr = []
impr = []
mean = []
thr=15.5
uvd = pandas.DataFrame()

for subject in subjects:        
    genuine_usr_data = data.loc[data.subject == subject,"H.period":"H.Return"]
    impr_data = data.loc[data.subject != subject, :]
    training_values=[] 
    training_values = genuine_usr_data[:200]                  #training sample set of data
    test_genuine_values = genuine_usr_data[200:]              #testing sample for genuine usr data
    test_impr = impr_data.loc[:,"H.period":"H.Return"] #impostor samples
    
    #Calculate mean-vector
    mean = training_values.mean().values
    
    #Calculate genuine score
    for i in range(test_genuine_values.shape[0]):
        G_score = cityblock(test_genuine_values.iloc[i].values,mean)
        usr.append(G_score)
    #Calculate impr score
    for i in range(test_impr.shape[0]):
        I_score = cityblock(test_impr.iloc[i].values,mean)
        impr.append(I_score)
 #calculating FRR 
    genuine_samples_rejected = 0
    genuine_samples = usr[:200]
    for sample in genuine_samples:
        if sample >= thr:
            genuine_samples_rejected+=1
    frr = genuine_samples_rejected/200.00
    #calculating FAR
    impr_samples_accepted = 0
    impr_samples = impr[:10000]
    for sample in impr_samples:
        if sample > thr:
            impr_samples_accepted+=1
    far = impr_samples_accepted/10000.00
    uvd_temp = pandas.DataFrame({'false_acceptance':far,'false_rejection':frr},index = [subject]);
    uvd = pandas.concat([uvd,uvd_temp])
    usr=[]
    impr=[]
print ("threshold=0 for N=200")
print (uvd)