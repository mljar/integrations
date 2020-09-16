# Summary of 5_Default_Xgboost

## Extreme Gradient Boosting (Xgboost)
- **objective**: binary:logistic
- **eval_metric**: logloss
- **eta**: 0.1
- **max_depth**: 6
- **min_child_weight**: 1
- **subsample**: 1.0
- **colsample_bytree**: 1.0
- **explain_level**: 2

## Validation
 - **validation_type**: split
 - **train_ratio**: 0.75
 - **shuffle**: True
 - **stratify**: True

## Optimized metric
logloss

## Training time

30.8 seconds

## Metric details
|           |    score |     threshold |
|:----------|---------:|--------------:|
| logloss   | 0.281087 | nan           |
| auc       | 0.925999 | nan           |
| f1        | 0.723923 |   0.385268    |
| accuracy  | 0.871733 |   0.463988    |
| precision | 0.970827 |   0.831656    |
| recall    | 1        |   3.47228e-05 |
| mcc       | 0.636445 |   0.463988    |


## Confusion matrix (at threshold=0.463988)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                    5145 |                     555 |
| Labeled as positive |                     464 |                    1336 |

## Learning curves
![Learning curves](learning_curves.png)

## Permutation-based Importance
![Permutation-based Importance](permutation_importance.png)

## SHAP Importance
![SHAP Importance](shap_importance.png)

## SHAP Dependence plots

### Dependence (Fold #1)
![SHAP Dependence from fold 1](learner_1_shap_dependence.png)

## SHAP Decision plots

### Top-10 Worst decisions for class 0 (Fold #1)
![SHAP worst decisions class 0 from fold 1](learner_1_shap_class_0_worst_decisions.png)
### Top-10 Best decisions for class 0 (Fold #1)
![SHAP best decisions class 0 from fold 1](learner_1_shap_class_0_best_decisions.png)
### Top-10 Worst decisions for class 1 (Fold #1)
![SHAP worst decisions class 1 from fold 1](learner_1_shap_class_1_worst_decisions.png)
### Top-10 Best decisions for class 1 (Fold #1)
![SHAP best decisions class 1 from fold 1](learner_1_shap_class_1_best_decisions.png)