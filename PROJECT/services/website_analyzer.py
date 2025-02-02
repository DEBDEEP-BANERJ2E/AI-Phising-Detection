from models.website_model import WebsiteModel
import torch

class WebsiteAnalyzer:
    def __init__(self):
        self.model = WebsiteModel()

    def analyze(self, image_tensor):
        return self.model.predict(image_tensor)
