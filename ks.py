#False Acceptance and False Rejection rate at threshold=0.5 for N=100
from scipy.spatial.distance import cityblock 
#import numpy as np
import pandas

path = "/Users/yash/Desktop/kdata.csv" 
data = pandas.read_csv(path)
subjects = data["subject"].unique()
user_scores = []
imposter_scores = []
mean_vector = []
thr=0.5
user_scores_df = pandas.DataFrame()

for subject in subjects:        
    genuine_user_data = data.loc[data.subject == subject,"H.period":"H.Return"]
    imposter_data = data.loc[data.subject != subject, :]

    train = genuine_user_data[:200]
    test_genuine = genuine_user_data[200:]
    test_imposter = imposter_data.groupby("subject").head(5).loc[:, "H.period":"H.Return"]
    
    #Calculate mean-vector
    mean_vector = train.mean().values
    
    #Calculate Imposter
    for i in range(test_genuine.shape[0]):
        cur_score = cityblock(test_genuine.iloc[i].values,mean_vector)
        user_scores.append(cur_score)
    
    for i in range(test_imposter.shape[0]):
        cur_score = cityblock(test_imposter.iloc[i].values,mean_vector)
        imposter_scores.append(cur_score)
    
    genuine_samples_rejected = 0
    genuine_samples = user_scores[:200]
    for sample in genuine_samples:
        if sample <= thr:
            genuine_samples_rejected+=1
    frr = genuine_samples_rejected/200.00
    imposter_samples_rejected = 0
    imposter_samples = imposter_scores[:10000]
    for sample in imposter_samples:
        if sample > thr:
            imposter_samples_rejected+=1
    far = imposter_samples_rejected/10000.00
    user_scores_df_temp = pandas.DataFrame({'false_acceptance':far,'false_rejection':frr},index = [subject]);
    user_scores_df = pandas.concat([user_scores_df,user_scores_df_temp])
    user_scores=[]
    imposter_scores=[]
print user_scores_df