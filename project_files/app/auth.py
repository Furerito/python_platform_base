from functools import wraps
from flask import redirect, url_for, session
from app.db import get_user_by_id, get_user

print('auth.py')

def login_required(f):
    """
    Dekorator, um sicherzustellen, dass der Benutzer eingeloggt ist.
    Falls der Benutzer nicht eingeloggt ist oder die 2FA nicht verifiziert wurde,
    wird er zur Login-Seite oder zur 2FA-Seite weitergeleitet.
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('home'))
        user = get_user(session['username'])
        if not user['two_factor_verified']:
            return redirect(url_for('two_factor'))
        return f(*args, **kwargs)
    return decorated_function

def superuser_required(f):
    """
    Dekorator, um sicherzustellen, dass der Benutzer ein Superuser ist.
    Falls der Benutzer kein Superuser ist, wird er zur Dashboard-Seite weitergeleitet.
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        user = get_user(session['username'])
        if not user or not user['is_superuser']:
            return redirect(url_for('dashboard'))
        return f(*args, **kwargs)
    return decorated_function

def get_current_user():
    """
    Hilfsfunktion, um den aktuell eingeloggenen Benutzer zu erhalten.
    Gibt den Benutzer zurück oder None, falls kein Benutzer eingeloggt ist.
    """
    if 'username' in session:
        return get_user(session['username'])
    return None

def is_superuser():
    """
    Hilfsfunktion, um zu überprüfen, ob der aktuelle Benutzer ein Superuser ist.
    Gibt True zurück, wenn der Benutzer ein Superuser ist, andernfalls False.
    """
    user = get_current_user()
    if user and user['is_superuser']:
        return True
    return False