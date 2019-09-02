from flask import render_template, request
# import bp for decorator
from app.errors import bp


# judge to reply in HTML or JSON preference
def wants_json_response():
    return request.accept_mimetypes['application/json'] >= \
        request.accept_mimetypes['text/html']


@bp.app_errorhandler(404)
def not_found_error(error):
    # return html format
    return render_template('errors/404.html'), 404


@bp.app_errorhandler(500)
def internal_error(error):
    # return html format
    return render_template('errors/500.html'), 500
