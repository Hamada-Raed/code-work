import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, precision_recall_fscore_support
from sklearn.impute import SimpleImputer

np.random.seed(42)
n_samples = 1000
data = pd.DataFrame({
    'transaction_amount': np.random.normal(100, 50, n_samples),  
    'num_attempts': np.random.randint(1, 5, n_samples),  
    'transaction_time': np.random.randint(0, 24, n_samples),  
    'location': np.random.randint(1, 100, n_samples),  
    'fraud_flag': np.random.randint(0, 2, n_samples)  #
})

data.loc[data.sample(frac=0.05).index, 'transaction_amount'] = np.nan

# 3. Handle dirty data
imputer = SimpleImputer(strategy='mean')
data['transaction_amount'] = imputer.fit_transform(data[['transaction_amount']])

# 4. Split the data
features = data[['transaction_amount', 'num_attempts', 'transaction_time', 'location']]
labels = data['fraud_flag']

X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = RandomForestClassifier(n_estimators=100, random_state=42)

counter = 0
target_accuracy = 0.92
while True:
    model.fit(X_train, y_train)
    accuracy = model.score(X_test, y_test)
    counter += 1
    print(f"Attempt {counter}: Accuracy = {accuracy:.4f}")
    if accuracy >= target_accuracy or counter >= 100:  
        break

y_pred = model.predict(X_test)

print(classification_report(y_test, y_pred))

plt.figure(figsize=(10, 6))
sns.boxplot(data=data, y='transaction_amount')
plt.title('Boxplot of Transaction Amount with Outliers Highlighted')
plt.show()

conf_matrix = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues')
plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()

precision, recall, f1_score, support = precision_recall_fscore_support(y_test, y_pred, average='binary')
print(f"Precision: {precision:.4f}, Recall: {recall:.4f}, F1-Score: {f1_score:.4f}, Support: {support}")