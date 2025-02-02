from transformers import pipeline

class EmailModel:
    def __init__(self):
        self.model = pipeline("text-classification", model="distilbert-base-uncased")

    def predict(self, email_text):
        return self.model(email_text)[0]
