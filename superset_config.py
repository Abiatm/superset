import os

# ✅ Use a strong random key — generate with: openssl rand -base64 42
SECRET_KEY = os.getenv("SUPERSET_SECRET_KEY", "change_this_please_123!")

# ✅ Read your Postgres URL from environment variable
SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")

# 🧰 Optional recommended settings
SQLALCHEMY_TRACK_MODIFICATIONS = False
ENABLE_PROXY_FIX = True
WTF_CSRF_ENABLED = True
