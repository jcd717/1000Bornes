from flask import Blueprint, render_template, g, url_for
import os
import markdown
from milleBornes import getReglesMD

bp = Blueprint('regles', __name__)


@bp.route('/regles')
def regles():
    g.md=getReglesMD()
    return render_template('regles.j2')
