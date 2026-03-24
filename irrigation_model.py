import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

def train_model():
    # Load your dataset (Ensure your dataset is in the right format)
    data = pd.read_csv('irrigation_data.csv')

    # Features (soilm moisture, temperature, humidity)
    X = data[['soil_moisture', 'temperature', 'humidity']]
    
    # Target variable (1 if irrigation needed, 0 otherwise)
    y = data['irrigation_needed']

    # Split the data for training and testing
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize and train the Random Forest model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Save the model to a file
    joblib.dump(model, 'models/smart_irrigation_model.pkl')

    # Model performance (optional)
    test_score = model.score(X_test, y_test)
    print(f'Model Test Accuracy: {test_score * 100:.2f}%')

# Train and save the model
train_model()
