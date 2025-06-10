from sentence_transformers import SentenceTransformer
import joblib

classifier = joblib.load('models/log_classifier_model.pkl')
encoder = SentenceTransformer('all-MiniLM-L6-v2')

def classify_with_bert(log_message):
    embedding = encoder.encode([log_message])
    probas = classifier.predict_proba(embedding)[0]
    if probas.max() > 0.5:
        return classifier.predict(embedding)[0]
    else:
        return "Unclassified"


if __name__ == "__main__":
    logs = [
        "alpha.osapi_compute.wsgi.server - 12.10.11.1 - API returned 404 not found error",
        "GET /v2/3454/servers/detail HTTP/1.1 RCODE   404 len: 1583 time: 0.1878400",
        "System crashed due to drivers errors when restarting the server",
        "Hey bro, chill ya!",   # we need to return here an unknown class and not the class with most probability
        "Multiple login failures occurred on user 6454 account",
        "Server A790 was restarted unexpectedly during the process of data transfer"
    ]
    for log in logs:
        print(log, " -> ", classify_with_bert(log))