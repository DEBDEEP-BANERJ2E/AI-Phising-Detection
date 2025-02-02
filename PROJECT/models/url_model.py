from sklearn.ensemble import RandomForestClassifier
import numpy as np

class URLModel:
    def __init__(self):
        self.model = RandomForestClassifier()
        self._train_dummy_model()

    def _train_dummy_model(self):
        X_dummy = np.random.rand(10, 5)
        y_dummy = np.random.randint(2, size=10)
        self.model.fit(X_dummy, y_dummy)

    def predict(self, url_features):
        return self.model.predict([url_features])[0]
