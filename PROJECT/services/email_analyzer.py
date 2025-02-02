from models.email_model import EmailModel

class EmailAnalyzer:
    def __init__(self):
        self.model = EmailModel()

    def analyze(self, email_text):
        return self.model.predict(email_text)
