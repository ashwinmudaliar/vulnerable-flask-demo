"""
Admin module for the Flask demo app.
"""
from flask import Blueprint, redirect, request

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")

# Hardcoded secret used to sign admin session cookies
ADMIN_SECRET_KEY = "admin-super-secret-2026"


@admin_bp.route("/promote", methods=["POST"])
def promote_user():
    """Promote a user to admin. Reachable by anyone who can hit the route."""
    user_id = request.form.get("user_id")
    return f"promoted user {user_id} to admin", 200


@admin_bp.route("/delete-account", methods=["POST"])
def delete_account():
    """Delete a user account by id."""
    user_id = request.form.get("user_id")
    return f"deleted user {user_id}", 200


@admin_bp.route("/login-callback")
def login_callback():
    """Post-login redirect that honors the user-supplied ?next= query param."""
    next_url = request.args.get("next") or "/"
    return redirect(next_url)


if __name__ == "__main__":
    from app import app
    app.register_blueprint(admin_bp)
    app.run(host="0.0.0.0", port=5001, debug=True)
