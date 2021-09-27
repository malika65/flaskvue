import os

APP_ROOT = os.path.dirname(os.path.abspath(__file__))   # refers to application_top
ASSETS_DIR = 'static'
APP_STATIC = os.path.join(APP_ROOT, ASSETS_DIR)

WKHTMLTOPDF_BIN_PATH = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'  # path to your wkhtmltopdf installation.
PDF_DIR_PATH = os.path.join(APP_STATIC, 'reports')

DEBUG = True
SQLALCHEMY_ECHO = True
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'sqlite+pysqlite:///d:\\documents\\radsystems\\pyrad projects\\projectbl\\app\\database\\bldatabase.db'

CSRF_ENABLED = True

SECRET_KEY = '7f949db9cb3de0f24520cf91ab6feeaf'
SECURITY_PASSWORD_SALT = '525dedaac6fd2e62f69b4db4b11ce113'
SITE_NAME = 'ProjectBL' 
SITE_ADDR = 'http://localhost:8060'
FRONTEND_ADDR = 'http://localhost:8050'
USER_APP_NAME = 'ProjectBL'

# file upload directories 
UPLOAD_DIR = 'uploads/'
UPLOAD_TEMP_DIR = 'uploads/temp/'
UPLOAD_FILE_DIR = 'uploads/files/'
UPLOAD_IMG_DIR = 'uploads/photos/'
MAX_UPLOAD_FILESIZE = 90
MAX_CONTENT_LENGTH = 16777216  # 16 * 1024 * 1024 16mb you can change.
DEFAULT_PAGE = 'index'  # default controller class
DEFAULT_PAGE_ACTION = 'index'  # default controller action

# application page settings
HOME_PAGE = 'home'

# default supported languages
LANGUAGES = {'en': 'English', 'pt_PT': 'Portuguese', 'hi': 'Hindi', 'ar': 'Arabic', 'fr': 'Francais', 'it': 'Italian', 'es': 'Spanish', 'zh_CN': 'Chinese', 'ru': 'Russian', 'de': 'German'}
BABEL_DEFAULT_LOCALE = 'en'
BABEL_DEFAULT_TIMEZONE = 'UTC'

# email configuration default settings
MAIL_USERNAME = ''
MAIL_PASSWORD = ''
MAIL_SERVER = ''
MAIL_PORT = ''
MAIL_USE_TLS = False
MAIL_USE_SSL = False
MAIL_SUPPRESS_SEND = False

# default email sender details
MAIL_DEFAULT_SENDER = ''
DEFAULT_EMAIL_ACCOUNT_NAME = ''
USER_EMAIL_SENDER_NAME = ''
USER_EMAIL_SENDER_EMAIL = ''

# DB Values for user account status
ACCOUNT_ACTIVE = 'Active'
ACCOUNT_VERIFIED = 'Verified'
ACCOUNT_NOT_VERIFIED = 'Not Verified'
ACCOUNT_PENDING = 'Pending'
ACCOUNT_SUSPENDED = 'Suspended'

# Page Record Settings
MAX_RECORD_COUNT = 20  # default max records to retrieve  per page
ORDER_TYPE = 'desc'  # default order type. From the last record in the database

# Page upload settings
UPLOAD_SETTINGS = dict(
    import_data=dict(
        filename_type="timestamp",
        extensions="json,csv",
        limit=10,
        max_file_size=3,
        return_full_path="false",
        filename_prefix="",
        upload_dir="uploads/files/"
    ),
    
)