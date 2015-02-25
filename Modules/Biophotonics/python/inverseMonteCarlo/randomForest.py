# -*- coding: utf-8 -*-
"""
Created on Fri Feb  6 10:49:45 2015

This is basically a wrapper for the python random forests.
It is necessary to do our preprocessing and KFold cross validation + grid search.

@author: wirkert
"""


import numpy as np
import time
from sklearn.ensemble         import RandomForestRegressor
from sklearn.grid_search      import GridSearchCV
from sklearn.cross_validation import KFold

from sklearn import decomposition



# additional things that could be checked in this study:
# 1. band selection results
# 2. effect of normalizations
# 3. parameter study
# 4. optimal image quotient

def randomForest(trainingParameters, trainingReflectances, trainingWeights):
    #%% train forest

    start = time.time()

    # transform data with pca (test)
    pca = decomposition.PCA(n_components=trainingReflectances.shape[1])
    pca.fit(trainingReflectances)
    trainingReflectances = pca.transform(trainingReflectances)

    # get best forest using k-fold cross validation and grid search
    # outcommented for now because it takes to long for quick tests

    kf = KFold(trainingReflectances.shape[0], 5, shuffle=True)
    param_grid = [
      {'max_depth': np.arange(2,40,1), 'n_estimators': np.logspace(1,11,11,base=2).astype(int)}]

    rf = GridSearchCV(RandomForestRegressor(50, max_depth=8), param_grid, cv=kf, n_jobs=11)
    rf.fit(trainingReflectances, trainingParameters)


    end = time.time()
    print "time necessary to train the forest [s]: " + str((end - start))


    return rf, pca#(rf, absErrors, rf.score(testReflectances, testParameters))



