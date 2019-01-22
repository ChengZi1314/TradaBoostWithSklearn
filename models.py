import xgboost as xgb
from sklearn.metrics import roc_auc_score
import sys
from code.TransferLearning.TrAdaboost import TradaBoostClassifier
import code.config as config
sys.path.append("..")
import lightgbm as lgb


def TradaBoostWithXGB(trainSource, trainTarget, dfTest):
    cols = [c for c in trainTarget.columns if c not in config.IGNORE_COLS]
    label_T = trainTarget['target'].values
    label_S = trainSource['target'].values
    label_test = dfTest['target'].values

    train_data_T = trainTarget[cols].values
    train_data_S = trainSource[cols].values
    test_data_T = dfTest[cols].values
    print(train_data_S.shape, train_data_T.shape, test_data_T.shape)
    xgbm =xgb.XGBClassifier()
    print(xgbm)
    trc = TradaBoostClassifier(epoch=5, learner=xgbm)
    print(trc.learner)
    trc.fit(train_data_T, train_data_S, label_T, label_S, test_data_T)
    pred = trc.predict_proba(test_data_T)
    print(pred)
    return roc_auc_score(y_true=label_test, y_score=pred)


def TradaBoostWithLGB(trainSource, trainTarget, dfTest):
    cols = [c for c in trainTarget.columns if c not in config.IGNORE_COLS]
    label_T = trainTarget['target'].values
    label_S = trainSource['target'].values
    label_test = dfTest['target'].values

    train_data_T = trainTarget[cols].values
    train_data_S = trainSource[cols].values
    test_data_T = dfTest[cols].values
    print(train_data_S.shape, train_data_T.shape, test_data_T.shape)
    lgbm =lgb.LGBMClassifier()
    trc = TradaBoostClassifier(epoch=5, learner=lgbm)
    trc.fit(train_data_T, train_data_S, label_T, label_S, test_data_T)
    pred = trc.predict_proba(test_data_T)
    print(pred)
    return roc_auc_score(y_true=label_test, y_score=pred)


