#False Acceptance and False Rejection rate at threshold=0.5 for N=100
from scipy.spatial.distance import cityblock 
#import numpy as np
import pandas

path = "/Users/yash/Desktop/kdata.csv" 
data = pandas.read_csv(path)
subjects = data["subject"].unique()
user_value = []
imposter_value = []
mean_value = []
thr=0.50
user_value_df = pandas.DataFrame()

for subject in subjects:        
    genuine_user_data = data.loc[data.subject == subject,"H.period":"H.Return"]
    imposter_data = data.loc[data.subject != subject, :]
    training_values=[] 
    training_values = genuine_user_data[:100]                  #training sample set of data
    test_genuine_values = genuine_user_data[100:]              #testing sample for genuine user data
    test_imposter = imposter_data.loc[:,"H.period":"H.Return"] #impostor samples
    
    #Calculate mean-vector
    mean_value = training_values.mean().values
    
    #Calculate genuine score
    for i in range(test_genuine_values.shape[0]):
        G_score = cityblock(test_genuine_values.iloc[i].values,mean_value)
        user_value.append(G_score)
    #Calculate Imposter score
    for i in range(test_imposter.shape[0]):
        I_score = cityblock(test_imposter.iloc[i].values,mean_value)
        imposter_value.append(I_score)
 #calculating FRR 
    genuine_samples_rejected = 0
    genuine_samples = user_value[:300]
    for sample in genuine_samples:
        if sample >= thr:
            genuine_samples_rejected+=1
    frr = genuine_samples_rejected/300.00
    #calculating FAR
    imposter_samples_accepted = 0
    imposter_samples = imposter_value[:15000]
    for sample in imposter_samples:
        if sample > thr:
            imposter_samples_accepted+=1
    far = imposter_samples_accepted/15000.00
    user_value_df_temp = pandas.DataFrame({'false_acceptance':far,'false_rejection':frr},index = [subject]);
    user_value_df = pandas.concat([user_value_df,user_value_df_temp])
    user_value=[]
    imposter_value=[]
print 'False Acceptance and False Rejection rate at threshold=0.50 for N=200'
print user_value_df
