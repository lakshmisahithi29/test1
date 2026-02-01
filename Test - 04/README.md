Problem Statement :

The objective of this assignment is to perform supervised machine learning on a real-world dataset by applying multiple classification algorithms and comparing their performance.

Dataset Description :

The Adult Census Income dataset was used for this task.

Target variable: income (≤50K or >50K)

The dataset contains a mix of numerical and categorical features related to demographic and employment information.

Data Preprocessing :

Missing values represented by ? were handled using median imputation for numerical features and mode imputation for categorical features.

Duplicate records were removed.

Irrelevant features such as fnlwgt were dropped.

Outliers were treated using the IQR method on numerical features.

Categorical variables were encoded using one-hot encoding.

Feature scaling was applied using standardization to support distance-based models.

Models Implemented :

Logistic Regression

Decision Tree

Random Forest

K-Nearest Neighbors (KNN)

Support Vector Machine (SVM)

Evaluation Metrics :

Models were evaluated using:

Accuracy

Precision

Recall

F1-Score

Conclusion :

Among the evaluated models, Random Forest demonstrated the best overall performance due to its robustness and ability to capture complex patterns. Logistic Regression provided a strong baseline, while KNN and SVM benefited from proper feature scaling. This comparison highlights the importance of selecting models based on data characteristics and preprocessing steps.