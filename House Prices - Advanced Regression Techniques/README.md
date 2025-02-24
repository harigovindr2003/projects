# **House Prices Prediction - Multiple Linear Regression**

## **Project Overview**

This project aims to predict house prices using **multiple linear regression**. The dataset from [Kaggle](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/data) is first analyzed and cleaned to remove noise and unnecessary variables. Feature selection is done carefully to improve accuracy and avoid overfitting. Some variables are transformed to improve model performance. The final model achieves an **R² score of 0.86** and is used to predict house prices for the test dataset.

## **Steps Followed**

1. **Importing the Dataset & Understanding the Data**
    - The dataset is loaded in Python, and an initial analysis is done.
    - Categorical and numerical variables are identified.

2. **Fixing Categorical Variables**
    - Categorical variables with too much missing data are dropped.
    - For the remaining categorical variables, we check the mean difference in `SalePrice` across different categories.
    - We select the **top 10 categorical variables** that have the highest impact on `SalePrice`.
    - Adding too many variables add noise and cause overfitting, so only **ordinal categorical variables** are kept and converted to numbers.

3. **Feature Selection Using Correlation Analysis**
    - We select **only variables with correlation > 0.6** with `SalePrice`.
    - Some variables are highly correlated with each other, meaning they provide the same information.
    - In such cases, some variables are combined into a **joint feature**, and others are dropped.
    - The final selected variables are saved in a list.

4. **Outlier Detection & Log Transformation**
    - We check for **outliers** in the selected features and find that **`TotalSF` has the most outliers**.
    - The **probability distribution of `TotalSF`** is similar to that of `SalePrice`.
    - Since the distributions are **right-skewed**, we apply **log transformations** on both `TotalSF` and `SalePrice`.
    - This transformation helps improve model performance.

5. **Model Training & Evaluation**
    - We use **multiple linear regression** to train the model.
    - The model achieves an **R² score of 0.86**.

6. **Prediction & Kaggle Submission**
    - The trained model is used to predict **`SalePrice`** in the test dataset.
    - A **submission file** is generated and submitted to Kaggle and achieved a public score of 0.16670 (RMSLE). While this is a solid baseline, future improvements could include advanced feature engineering and more advanced models like ensemble methods which could further improve the score.

View the full Jupyter Notebook [here](https://github.com/harigovindr2003/projects/blob/main/House%20Prices%20-%20Advanced%20Regression%20Techniques/main.ipynb).
