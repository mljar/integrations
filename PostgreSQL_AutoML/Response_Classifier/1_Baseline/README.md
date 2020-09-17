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

0.1 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.354508 |  nan        |
| auc       | 0.5      |  nan        |
| f1        | 0.204441 |    0.102473 |
| accuracy  | 0.113859 |    0.102473 |
| precision | 0.113859 |    0.102473 |
| recall    | 1        |    0.102473 |
| mcc       | 0        |    0.102473 |


## Confusion matrix (at threshold=0.102473)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                       0 |                    7238 |
| Labeled as positive |                       0 |                     930 |

## Learning curves
![Learning curves](learning_curves.png)