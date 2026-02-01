Missing Value Handling:
Categorical missing values were handled using mode imputation, as it preserves the most frequent category and is suitable for nominal data. Numerical features contained no missing values; however, median imputation was demonstrated due to its robustness against outliers.

Categorical Encoding:
One-hot encoding was found to be most effective for nominal features such as workclass, occupation, and race, as it prevents the model from assuming any ordinal relationship. Ordinal encoding was appropriate for the education feature because it has a natural hierarchical order. Frequency encoding helped retain distributional information without increasing dimensionality, while target encoding was applied cautiously due to the risk of data leakage.

Feature Scaling:
Among the scaling techniques, Z-score standardization was the most effective as it centers numerical features around zero with unit variance, making it suitable for many machine learning algorithms. Min-max scaling and max absolute scaling were useful for range-based and sparse data scenarios, while vector normalization was effective for similarity-based models.

Outlier Treatment and Skewness Transformation:
Outliers were treated using the IQR method to reduce the influence of extreme values. Highly skewed features such as capital gain and capital loss were transformed using logarithmic transformation, which reduced skewness and improved feature stability.

Final Preprocessing Choice:
The final preprocessing pipeline balanced data integrity, interpretability, and model readiness by combining appropriate missing value handling, encoding strategies, scaling methods, and skewness correction.