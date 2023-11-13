from flask import request, jsonify
import functools

_user_model = None

def init_auth(User):
    global _user_model
    _user_model = User

def ok_user_and_password(username, password):
    """Test whether the supplied username and password match."""
    user = _user_model.query.filter_by(username=username).first()
    return user.check_password(password) if user else False

def authenticate():
    """ Return a response indicating a failure to authenticate."""
    message = {'message': "Authenticate."}
    resp = jsonify(message)

    resp.status_code = 401
    resp.headers['WWW-Authenticate'] = 'Basic realm="Main"'

    return resp


def requires_authorization(f):
    """A python decorator which requires HTTP basic authentication."""

    @functools.wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not ok_user_and_password(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)

    return decorated
