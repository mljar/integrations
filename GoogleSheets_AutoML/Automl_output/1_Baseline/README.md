# Summary of 1_Baseline

## Baseline Classifier (Baseline)
- **explain_level**: 2

## Validation
 - **validation_type**: split
 - **train_ratio**: 0.75
 - **shuffle**: True
 - **stratify**: True

## Optimized metric
logloss

## Training time

0.0 seconds

## Metric details
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.241157  | nan         |
| auc       | 0.5       | nan         |
| f1        | 0.122494  |   0.0587421 |
| accuracy  | 0.0652432 |   0.0587421 |
| precision | 0.0652432 |   0.0587421 |
| recall    | 1         |   0.0587421 |
| mcc       | 0         |   0.0587421 |


## Confusion matrix (at threshold=0.058742)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                       0 |                    1576 |
| Labeled as positive |                       0 |                     110 |

## Learning curves
![Learning curves](learning_curves.png)