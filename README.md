# TradaBoostWithSklearn
this TradaBoost perform well on different classifier, we shoud choose the classifier whose .fit function has parameter named *"sample_weight"*, and the classifier also should have a predict_proba function.

This TradaBoost has a better performance the others on the website..


网上关于TradaBoost代码很多，但是大多是从一个来源copy过来的，而且效果不是很好。所以我就写了一个新版本，可以调用sklearn里面各类分类器的版本。使用sklearn内模型作为内核的时候，我们要注意模型的需要有predict_proba函数，模型的fit函数需要有sample_weigeht参数。

建议使用LightGBM作为内核。
