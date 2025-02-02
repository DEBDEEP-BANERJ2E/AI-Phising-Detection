from api.app import create_api
from dashboard.app import run_dashboard

if __name__ == "__main__":
    api_app = create_api()
    run_dashboard(api_app)
