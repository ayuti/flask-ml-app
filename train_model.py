import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib

# Load data
def train():
    df = pd.read_csv("data.csv")

    # Features and label
    X = df[['market_cap', 'total_volume']]
    y = df['current_price']

    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # Train model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Save model
    joblib.dump(model, 'model.pkl')
    print("Model saved as model.pkl")


if __name__ == "__main__":
    train()