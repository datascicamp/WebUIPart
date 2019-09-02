from flask import Blueprint

# template_folder indicates the fold in errors where storing template
# bp = Blueprint('errors', __name__, template_folder='templates')
bp = Blueprint('errors', __name__)

# This import is at the bottom to avoid circular dependencies.
from app.errors import handlers
