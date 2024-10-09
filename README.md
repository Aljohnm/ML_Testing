# Hybrid Machine Learning Models for Classification

## Project Description
This project implements hybrid machine learning models to classify data using various algorithms, including XGBoost, Random Forest, Support Vector Machines (SVM), and Gradient Boosting. The models are evaluated based on their accuracy, providing insights into the performance of different hybrid approaches.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Accuracy Results](#accuracy-results)
- [Screenshot](#screenshot)
- [License](#license)

## Installation
To run this project, ensure you have Python 3.6 or higher installed. You will also need to install the required packages. You can install the necessary libraries using pip:


pip install pandas scikit-learn xgboost
# Usage

To use the project, follow these steps:

## Clone the Repository:

git clone https://github.com/yourusername/yourrepository.git
cd yourrepository
Prepare Your Dataset:
Ensure your dataset is in the correct format. Adjust the CSV file path in the code if necessary to match your dataset's location.

Run the Accuracy Script:
Execute the following command to run the accuracy evaluation script:

bash
Copy code
python accuracy.py
csharp
Copy code

You can copy and paste this into your GitHub repository as well!


# Accuracy Results

The accuracy results from multiple runs of the hybrid models are summarized below. Each run demonstrates the training of different hybrid models along with their accuracy metrics.

## Run 1
### Training Hybrid 1 (XGBoost + Random Forest):
- **Hybrid 1 (XGBoost + Random Forest) Accuracy:** 0.5250

### Training Hybrid 2 (SVM + XGBoost):
- **Hybrid 2 (SVM + XGBoost) Accuracy:** 0.4750

### Training Hybrid 3 (RF + Gradient Boosting):
- **Hybrid 3 (RF + Gradient Boosting) Accuracy:** 0.5500

### Training Hybrid 4 (RF + SVM):
- **Hybrid 4 (RF + SVM) Accuracy:** 0.4500

### Training Hybrid 5 (RF + SVM without stacking):
- **Hybrid 5 (RF + SVM without stacking) Accuracy:** 0.4750

### Final Results from Run 1:
- Hybrid 1 (XGBoost + Random Forest): **0.5250**
- Hybrid 2 (SVM + XGBoost): **0.4750**
- Hybrid 3 (RF + Gradient Boosting): **0.5500**
- Hybrid 4 (RF + SVM): **0.4500**
- Hybrid 5 (RF + SVM without stacking): **0.4750**

## Run 2
### Training Hybrid 1 (XGBoost + Random Forest):
- **Hybrid 1 (XGBoost + Random Forest) Accuracy:** 0.6643

### Training Hybrid 2 (SVM + XGBoost):
- **Hybrid 2 (SVM + XGBoost) Accuracy:** 0.6571

### Training Hybrid 3 (RF + Gradient Boosting):
- **Hybrid 3 (RF + Gradient Boosting) Accuracy:** 0.6500

### Training Hybrid 4 (RF + SVM):
- **Hybrid 4 (RF + SVM) Accuracy:** 0.6286

### Training Hybrid 5 (RF + SVM without stacking):
- **Hybrid 5 (RF + SVM without stacking) Accuracy:** 0.6786

### Final Results from Run 2:
- Hybrid 1 (XGBoost + Random Forest): **0.6643**
- Hybrid 2 (SVM + XGBoost): **0.6571**
- Hybrid 3 (RF + Gradient Boosting): **0.6500**
- Hybrid 4 (RF + SVM): **0.6286**
- Hybrid 5 (RF + SVM without stacking): **0.6786**

## Run 3
### Training Hybrid 1 (XGBoost + Random Forest):
- **Hybrid 1 (XGBoost + Random Forest) Accuracy:** 0.6786

### Training Hybrid 2 (SVM + XGBoost):
- **Hybrid 2 (SVM + XGBoost) Accuracy:** 0.6571

### Training Hybrid 3 (RF + Gradient Boosting):
- **Hybrid 3 (RF + Gradient Boosting) Accuracy:** 0.6571

### Training Hybrid 4 (RF + SVM):
- **Hybrid 4 (RF + SVM) Accuracy:** 0.6143

### Training Hybrid 5 (RF + SVM without stacking):
- **Hybrid 5 (RF + SVM without stacking) Accuracy:** 0.6357

### Final Results from Run 3:
- Hybrid 1 (XGBoost + Random Forest): **0.6786**
- Hybrid 2 (SVM + XGBoost): **0.6571**
- Hybrid 3 (RF + Gradient Boosting): **0.6571**
- Hybrid 4 (RF + SVM): **0.6143**
- Hybrid 5 (RF + SVM without stacking): **0.6357**

## Run 4
### Training Hybrid 1 (XGBoost + Random Forest):
- **Hybrid 1 (XGBoost + Random Forest) Accuracy:** 0.6643

### Training Hybrid 2 (SVM + XGBoost):
- **Hybrid 2 (SVM + XGBoost) Accuracy:** 0.6571

### Training Hybrid 3 (RF + Gradient Boosting):
- **Hybrid 3 (RF + Gradient Boosting) Accuracy:** 0.6571

### Training Hybrid 4 (RF + SVM):
- **Hybrid 4 (RF + SVM) Accuracy:** 0.6143

### Training Hybrid 5 (RF + SVM without stacking):
- **Hybrid 5 (RF + SVM without stacking) Accuracy:** 0.6143

### Final Results from Run 4:
- Hybrid 1 (XGBoost + Random Forest): **0.6643**
- Hybrid 2 (SVM + XGBoost): **0.6571**
- Hybrid 3 (RF + Gradient Boosting): **0.6571**
- Hybrid 4 (RF + SVM): **0.6143**
- Hybrid 5 (RF + SVM without stacking): **0.6143**

## Conclusion
The project successfully implements multiple hybrid machine learning models and evaluates their performance based on accuracy. Each model demonstrates varying accuracy levels across different runs, indicating the importance of model selection and parameter tuning for classification tasks.
