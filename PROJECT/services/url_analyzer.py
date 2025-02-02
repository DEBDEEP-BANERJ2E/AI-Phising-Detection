from models.url_model import URLModel

class URLAnalyzer:
    def __init__(self):
        self.model = URLModel()

    def analyze(self, url_features):
        return self.model.predict(url_features)
