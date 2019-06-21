from . import web
from flask_login import login_required


@web.route("/my/gift")
@login_required
def my_gifts():
    return "1111"
