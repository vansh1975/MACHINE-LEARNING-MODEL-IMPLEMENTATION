pip install pandas scikit-learn
# Step 1: Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix, 
classification_report

# Step 2: Create dataset
data = {
    'text': [
        'Win money now',
        'Hello friend how are you',
        'Free offer just for you',
        'Let us meet tomorrow',
        'Claim your prize now',
        'Are you available today',
        'Congratulations you won lottery',
        'Important meeting at 5pm',
        'Get free recharge now',
        'Call me when you are free'
    ],
    'label': [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]  # 1 = Spam, 0 = Not Spam
}
df = pd.DataFrame(data)

# Step 3: Convert text to numerical data
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['text'])
y = df['label']

# Step 4: Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, 
test_size=0.2, random_state=42)

# Step 5: Train model
model = MultinomialNB()
model.fit(X_train, y_train)

# Step 6: Test model
y_pred = model.predict(X_test)

# Step 7: Evaluation
print("✅ Accuracy:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, 
y_pred))

# Step 8: Test with custom input
while True:
    user_input = input("\nEnter a message (or type 'exit'): ")
    
    if user_input.lower() == 'exit':
        print("Exiting...")
        break
    
    input_data = vectorizer.transform([user_input])
    prediction = model.predict(input_data)[0]
    
    if prediction == 1:
        print("✅ Prediction: SPAM")
    else:
        print("✅ Prediction: NOT SPAM")
