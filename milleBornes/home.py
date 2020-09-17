from flask import Blueprint, render_template, g, session, request, redirect, url_for, jsonify

from .listeCartes import getTitle
from . import getOptions, Option, optionsToJSON, optionsJSONtoEnum

bp = Blueprint('home', __name__)


@bp.route('/')
def home():
    g.listeCartes=getTitle()
    g.continuer=None
    if session.get('partie') and not session['partie'].terminated:
        g.continuer=session['partie'].nombreJoueurs

    return render_template('home.j2')


def isChecked(session,droiteOuGauche : Option):
    return 'checked' if getOptions(session)[Option.MAIN]==droiteOuGauche else ''


@bp.route('/options',methods=('GET','POST'))
def options():
    if request.method=='POST':
        if 'ok' in request.form.keys():
            session['options']={
                Option.MOI: request.form['moi'], Option.PARTENAIRE: request.form['partenaire'],
                Option.ADVERSAIRE_DROITE: request.form['adversaireDroite'], 
                Option.ADVERSAIRE_GAUCHE: request.form['adversaireGauche'],
                Option.MAIN: Option.MAIN_A_DROITE if request.form['droiteOuGauche']=='droite' else Option.MAIN_A_GAUCHE
            }
        return redirect(url_for('home.home'))

    g.options=getOptions(session)
    return render_template('options.j2',isChecked=isChecked,Option=Option)

