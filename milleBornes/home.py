from flask import Blueprint, render_template, g

from .listeCartes import getTitle

bp = Blueprint('home', __name__)


@bp.route('/')
def home():
    g.listeCartes=getTitle()
    return render_template('home.j2')

