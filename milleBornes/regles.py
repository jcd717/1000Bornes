from flask import Blueprint,render_template, g
from milleBornes import getReglesMD

bp = Blueprint('regles', __name__)


@bp.route('/regles')
def regles():
    g.md=getReglesMD()
    return render_template('regles.j2')
