from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import pickle
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression

# Create your views here.
def home_view(request):
    return render(request, 'main/home.html')

def shop_view(request):
    return render(request, 'main/shop.html')

def yield_analysis_view(request):
    return render(request, 'main/yield_analysis.html')

def cart_view(request):
    return render(request, 'main/cart.html')

def sign_in_view(request):
    return render(request, 'main/sign_in.html')

def sign_out_view(request):
    # You would typically handle sign-out logic here
    return HttpResponse("You have been signed out.")

def load_model(filename):
    """Load a machine learning model from a file."""
    with open(filename, 'rb') as file:
        return pickle.load(file)

def load_data(file_path):
    """Load data from a CSV file."""
    return pd.read_csv(file_path)

def predict_with_model(request):
    """Predict using multiple models and return their accuracies."""
    # Load all models
    decision_tree = load_model('DecisionTree.pkl')
    nb_classifier = load_model('NBClassifier.pkl')
    random_forest = load_model('RandomForest.pkl')
    svm_classifier = load_model('SVMClassifier.pkl')
    xgboost = load_model('XGBoost.pkl')

    # Load or prepare your test data
    test_data = load_data('test_data.csv')
    Xtest = test_data.drop('target', axis=1)  # Features
    Ytest = test_data['target']  # Labels

    # Predictions
    dt_predictions = decision_tree.predict(Xtest)
    nb_predictions = nb_classifier.predict(Xtest)
    rf_predictions = random_forest.predict(Xtest)
    svm_predictions = svm_classifier.predict(Xtest)
    xgb_predictions = xgboost.predict(Xtest)

    # Accuracy calculations
    dt_accuracy = accuracy_score(Ytest, dt_predictions)
    nb_accuracy = accuracy_score(Ytest, nb_predictions)
    rf_accuracy = accuracy_score(Ytest, rf_predictions)
    svm_accuracy = accuracy_score(Ytest, svm_predictions)
    xgb_accuracy = accuracy_score(Ytest, xgb_predictions)

    return JsonResponse({
        'Decision Tree Accuracy': dt_accuracy,
        'Naive Bayes Accuracy': nb_accuracy,
        'Random Forest Accuracy': rf_accuracy,
        'SVM Accuracy': svm_accuracy,
        'XGBoost Accuracy': xgb_accuracy
    })

def predict(request):
    """Train a Logistic Regression model and make predictions based on user input."""
    if request.method == 'POST':
        try:
            input_data = request.POST
            input_df = pd.DataFrame([input_data])

            # Load or prepare your training data
            train_data = load_data('train_data.csv')
            Xtrain = train_data.drop('target', axis=1)  # Features
            Ytrain = train_data['target']  # Labels

            # Train Logistic Regression model
            log_reg = LogisticRegression(random_state=2)
            log_reg.fit(Xtrain, Ytrain)

            # Predict using the trained model
            predictions = log_reg.predict(input_df)

            # Pass predictions to the template
            context = {
                'predictions': predictions.tolist(),  # Convert numpy array to list for JSON serialization
            }

            return render(request, 'predict.html', context=context)
        except Exception as e:
            return HttpResponse(f"Error: {e}")
    else:
        return HttpResponse("Please send a POST request with input data.")
