import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, StackingClassifier
from xgboost import XGBClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load your dataset from CSV file (adjust the file path)
df = pd.read_csv('All_testing Files.csv')

# Separate features and target label
X = df.drop(columns=['category'])  # Assuming 'category' is the label column
y = df['category']

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize base models without the deprecated parameter
xgb = XGBClassifier(n_estimators=10, eval_metric='logloss')
rf = RandomForestClassifier(n_estimators=10)
svm = SVC(probability=True, max_iter=1000)
gb = GradientBoostingClassifier(n_estimators=10)

# Hybrid 1: XGBoost + Random Forest (Stacking)
stacked_model_1 = StackingClassifier(estimators=[('xgb', xgb), ('rf', rf)], final_estimator=LogisticRegression())

# Hybrid 2: SVM + XGBoost (Stacking)
stacked_model_2 = StackingClassifier(estimators=[('svm', svm), ('xgb', xgb)], final_estimator=LogisticRegression())

# Hybrid 3: Random Forest + Gradient Boosting (Stacking)
stacked_model_3 = StackingClassifier(estimators=[('rf', rf), ('gb', gb)], final_estimator=LogisticRegression())

# Hybrid 4: Random Forest + SVM (Stacking)
stacked_model_4 = StackingClassifier(estimators=[('rf', rf), ('svm', svm)], final_estimator=LogisticRegression())

# Hybrid 5: Random Forest + SVM (without stacking)
stacked_model_5 = StackingClassifier(estimators=[('rf', rf), ('svm', svm)], final_estimator=LogisticRegression())

# List of hybrid models
models = [
    ('Hybrid 1 (XGBoost + Random Forest)', stacked_model_1),
    ('Hybrid 2 (SVM + XGBoost)', stacked_model_2),
    ('Hybrid 3 (RF + Gradient Boosting)', stacked_model_3),
    ('Hybrid 4 (RF + SVM)', stacked_model_4),
    ('Hybrid 5 (RF + SVM without stacking)', stacked_model_5)
]

# Train and evaluate each model
accuracy_results = {}

for name, model in models:
    print(f"Training {name}...")
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    accuracy_results[name] = accuracy
    print(f"{name} Accuracy: {accuracy:.4f}")

# Print final accuracy results
print("\nFinal Accuracy Results:")
for model_name, acc in accuracy_results.items():
    print(f"{model_name}: {acc:.4f}")
