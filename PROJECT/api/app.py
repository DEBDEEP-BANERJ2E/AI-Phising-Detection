from flask import Flask, request, jsonify
from services.email_analyzer import EmailAnalyzer
from services.url_analyzer import URLAnalyzer
from services.website_analyzer import WebsiteAnalyzer


def create_api():
    app = Flask(__name__)

    email_analyzer = EmailAnalyzer()
    url_analyzer = URLAnalyzer()
    website_analyzer = WebsiteAnalyzer()

    @app.route("/analyze/email", methods=["POST"])
    def analyze_email():
        content = request.json.get("content", "")
        result = email_analyzer.analyze(content)
        return jsonify(result)

    @app.route("/analyze/url", methods=["POST"])
    def analyze_url():
        url = request.json.get("url", "")
        result = url_analyzer.analyze([len(url), url.count("."), url.count("/"), len(set(url)), len(url.split("/"))])
        return jsonify(result)

    @app.route("/analyze/website", methods=["POST"])
    def analyze_website():
        file = request.files.get("file")
        # Dummy tensor for placeholder
        import torch
        dummy_tensor = torch.randn(1, 1, 28, 28)
        result = website_analyzer.analyze(dummy_tensor)
        return jsonify(result)

    return app
