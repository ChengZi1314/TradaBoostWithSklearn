import pandas as pd
import numpy as np
from code.models import TradaBoostWithXGB, TradaBoostWithLGB
from sklearn import preprocessing

dfTrainTarget = pd.read_csv("../dataTransfer/11405010.csv", index_col=None)
dfTrainAssist = pd.read_csv("../dataTransfer/11406010.csv", index_col=None)
dfTest = pd.read_csv("../dataTransfer/11405010test.csv", index_col=None)

data = pd.concat([dfTrainTarget, dfTrainAssist, dfTest], copy=False)
data = data.fillna(0)

for f in data.columns:
    if data[f].dtype == 'object':
        lbl = preprocessing.LabelEncoder()
        data[f] = lbl.fit_transform(list(data[f].values))

dfTrainTarget = data[:np.array(dfTrainTarget).shape[0]]
dfTrainAssist = data[np.array(dfTrainTarget).shape[0]:np.array(dfTrainTarget).shape[0]+np.array(dfTrainAssist).shape[0]]
dfTest = data[np.array(dfTrainTarget).shape[0]+np.array(dfTrainAssist).shape[0]:]

print(TradaBoostWithXGB(dfTrainAssist, dfTrainTarget, dfTest))

