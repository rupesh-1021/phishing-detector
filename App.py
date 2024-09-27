from flask import Flask, render_template, request
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn import metrics

app = Flask(__name__)


df = pd.read_csv("phishing_site_urls.csv")
df['label'] = df['Label'].map({'bad': 0, 'good': 1})
X = df['URL']
y = df['label']

cv = CountVectorizer(max_features=5000, stop_words='english', lowercase=True, binary=True)
X = cv.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.43, random_state=39)

clf = MultinomialNB()
clf.fit(X_train, y_train)
clf.score(X_test, y_test)

y_pred = clf.predict(X_test)
accuracy = metrics.accuracy_score(y_test, y_pred)

print(f"Model Accuracy: {accuracy}")

precision = metrics.precision_score(y_test, y_pred)
print(f"Precision: {precision}")

@app.route('/')
def home():
    return render_template('phishing_detector.html')
    

@app.route('/predict', methods=['POST'])
def predict():
    try:
        if request.method == 'POST':
            prediction_type = request.form['prediction_type']

            if prediction_type == 'url':
                num_urls = int(request.form['num_urls'])
                urls = [request.form[f'url{i}'] for i in range(1, num_urls + 1)]
                data = cv.transform(urls).toarray()
                predictions = clf.predict(data).tolist()

            elif prediction_type == 'ip':
                num_ips = int(request.form['num_ips'])
                ips = [request.form[f'ip{i}'] for i in range(1, num_ips + 1)]
                data = cv.transform(ips).toarray()
                predictions = clf.predict(data).tolist()

            elif prediction_type == 'domains':
                num_domains = int(request.form['num_domains'])
                domains = [request.form[f'domains{i}'] for i in range(1, num_domains + 1)]
                data = cv.transform(domains).toarray()
                predictions = clf.predict(data).tolist()

            else:
                return render_template('phishing_detector.html', error='Invalid prediction type')

    except Exception as e:
        return render_template('phishing_detector.html', error=str(e))

    predictions_with_counter = [(i + 1, pred) for i, pred in enumerate(predictions)]

    if prediction_type == 'url':
        return render_template('phishing_detector.html', urlPredictions=predictions_with_counter)
    elif prediction_type == 'ip':
        return render_template('phishing_detector.html', ipPredictions=predictions_with_counter)
    elif prediction_type == 'domains':
        return render_template('phishing_detector.html', domainsPredictions=predictions_with_counter)

if __name__ == '__main__':
    app.run()
