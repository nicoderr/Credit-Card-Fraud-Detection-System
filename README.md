# Credit Card Fraud Detection System


## Project Overview

With the rapid increase in online transactions, credit card fraud has escalated into a major concern, resulting in billions of dollars in losses each year, impacting both businesses and consumers. To combat this, implementing effective fraud detection mechanisms is essential to prevent financial setbacks and protect users from unauthorized activities.

This project focuses on utilizing machine learning methodologies to identify fraudulent credit card transactions. By analyzing large volumes of transaction data, the system can pinpoint fraud patterns, facilitating early intervention and reducing the risk of financial harm. The goal is to create a robust fraud detection system that strengthens the integrity of financial systems and builds consumer confidence.

What sets this project apart is its comprehensive approach to feature selection and model fine-tuning. The dataset used contains 120 features, and through an in-depth analysis, we pinpointed the most relevant ones to ensure efficient processing while minimizing irrelevant data. In contrast to typical solutions, this project explores multiple machine learning algorithms, comparing their effectiveness in detecting fraud. Through advanced hyperparameter optimization, we achieved a substantial increase in model accuracy, improving from 88.26% to 98.37%. This improvement is critical, as even small errors in fraud detection can result in significant financial losses and diminish trust in the system. This project demonstrates the value of applying a methodical, data-driven approach to address pressing real-world issues like credit card fraud.

## Problem Statement

Due to the increase in e-commerce and online transactions, credit card fraud has surged. Traditional fraud detection methods struggle to keep pace with the growing volume and evolving tactics of fraudsters. There is a
critical need for more advanced and efficient fraud detection mechanisms that can reduce financial losses for both financial institutions and consumers.

## Datasets

### Dataset 1:

Source: Kaggle Dataset from Université Libre de Bruxelles, found [here](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)

Details:
  1. Contains 28 labels encrypted using PCA method.
  2. The dataset includes transaction data for credit card fraud detection.
  3. The dataset does not contain sensitive details but offers a reliable way to predict fraudulent activities.

### Dataset 2:
Source: Kaggle Dataset from IIIT Bangalore/UpGrad, found [here](https://www.kaggle.com/datasets/mishra5001/credit-card)
  1. Contains 120 labels and includes diverse data for classification.
  2. The dataset is derived from real-world credit card defaulter attributes.
  3. Includes encrypted sensitive data but retains the key features for classification tasks.


## Algorithms Used
The following machine learning algorithms were used to detect credit card fraud:

1. Logistic Regression
2. AdaBoost Classifier
3. Random Forest
4. Decision Tree
5. Linear Discriminant Analysis
6. Naive Bayes Classifier
7. XGBoost Classifier

## Feature Extraction
Feature extraction involves transforming raw data into a suitable format for analysis. It is crucial for improving model efficiency and performance. By identifying the most relevant features, the system can reduce complexity and improve accuracy.

Correlation Matrix:
  Helps identify the relationships between variables.
  Detects redundant or irrelevant features.
  Improves the model by selecting only the most predictive features.

## Implementation

### Tools and Technologies:

  **Programming Language:** Python
  **Machine Learning Libraries:** scikit-learn, imblearn, pandas, NumPy
  **Data Visualization:** Matplotlib, Seaborn
  **Web Framework:** Flask
  **Serialization:** Pickle (for saving models)

## Steps:
  1. Data Preprocessing: Handled missing values, scaled features, and encoded categorical variables.
  2. Model Training: Various machine learning algorithms were tested, and Random Forest was selected based on accuracy and precision.
  3. Model Deployment: The model was serialized using Pickle and deployed via a Flask web application.

## Results

The Random Forest model achieved impressive accuracy and precision and resulted as the most effective model:
**Accuracy:** 98.37%
**Precision:** 98.98%
**Recall:** 80.31%
**F1-Score:** 88.67%
These results demonstrate the high performance of the Random Forest model in detecting fraudulent transactions, with high precision reducing false positives and a strong recall value to identify fraudulent activities effectively.

## How to Run the Project:

### Clone the Repository:
git clone <repository_url>

### Download the Pre-Trained Model:
[Download the Model](https://drive.google.com/file/d/1-i6JctkggEnWqeoRd0mS-RoH7SGHwEAV/view)

### Run the Flask Application:
python app.py
