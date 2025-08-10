try:
    # If backend/app/__init__.py exposes 'app'
    from app import app
except Exception:
    # Fallback: import Flask app object from backend/app/routes.py if defined there
    from app.routes import app  # adjust if your app object lives elsewhere
