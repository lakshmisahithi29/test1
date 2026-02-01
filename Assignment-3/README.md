Problem Statement :

The objective of this assignment is to build and evaluate a Linear Regression model to predict house prices using a real-world dataset. The task involves data cleaning, exploratory data analysis, model training, evaluation, and interpretation of results.

Dataset Description :

The California Housing Prices dataset was used, containing over 20,000 records.

Target variable: median_house_value

Features: Median income, housing age, population statistics, and location-based attributes

The dataset includes one categorical feature (ocean_proximity) and multiple numerical features.

 Data Cleaning :


Missing values in total_bedrooms were handled using median imputation, which is robust to outliers.

Duplicate records were checked and removed.

Outliers were treated using the IQR method on numerical features.

The categorical feature ocean_proximity was converted to numeric form using one-hot encoding, as linear regression requires numeric inputs.

 Exploratory Data Analysis (EDA) :

Distribution of the target variable showed a right-skewed pattern.

Correlation analysis revealed that median_income has a strong positive relationship with house prices.

A correlation heatmap was used to check multicollinearity among features.

 Model Building :


The dataset was split into 80% training and 20% testing sets.

A Linear Regression model was trained using the training data.

Predictions were made on the test dataset.

Model Evaluation :

The model was evaluated using:

Mean Squared Error (MSE)

R² Score

A lower MSE indicated good prediction accuracy, and an R² score closer to 1 showed that the model explains a significant portion of variance in house prices.

 Interpretation & Conclusion:

Coefficient analysis showed that median income has the strongest positive influence on house prices, while location-related features also significantly affect housing value.
Overall, the Linear Regression model provided a reasonable fit and demonstrated meaningful relationships between input features and the target variable.