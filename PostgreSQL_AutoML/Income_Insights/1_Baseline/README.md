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

0.2 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.55108  |   nan       |
| auc       | 0.5      |   nan       |
| f1        | 0.387097 |     0.21596 |
| accuracy  | 0.24     |     0.21596 |
| precision | 0.24     |     0.21596 |
| recall    | 1        |     0.21596 |
| mcc       | 0        |     0.21596 |


## Confusion matrix (at threshold=0.21596)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                       0 |                    5700 |
| Labeled as positive |                       0 |                    1800 |

## Learning curves
![Learning curves](learning_curves.png)