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
| logloss   | 0.242292 |  nan        |
| auc       | 0.5      |  nan        |
| f1        | 0.123246 |    0.059103 |
| accuracy  | 0.06567  |    0.059103 |
| precision | 0.06567  |    0.059103 |
| recall    | 1        |    0.059103 |
| mcc       | 0        |    0.059103 |


## Confusion matrix (at threshold=0.059103)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                       0 |                    1750 |
| Labeled as positive |                       0 |                     123 |

## Learning curves
![Learning curves](learning_curves.png)