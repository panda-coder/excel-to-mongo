import os

# Database
DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb://localhost:27017")
DATABASE_PORT = os.environ.get("DATABASE_PORT", 27017)

# Upload
UPLOAD_FOLDER = '/tmp/excel-to-mongo'
ALLOWED_EXTENSIONS = {'xlsx'}