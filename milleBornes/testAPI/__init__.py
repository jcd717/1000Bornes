from flask import Blueprint, render_template, g, url_for, jsonify, request, session
import os


bp = Blueprint('testAPI', __name__)


@bp.route('/')
def homeAPI():
    return render_template('testAPI/testAPI.j2')


@bp.route('/hello', methods = ('GET', 'POST'))
def helloAPI():
    d={'result': 'toto'}
    return jsonify(d)


@bp.route('/add', methods=('GET', 'POST'))
def addAPI():
    datas=request.get_json() # récupère le body json de la requête
    return {'result': datas['a']+datas['b']}


@bp.route('/cpt', methods=('GET', 'POST'))
def cptAPI():
    cpt=session.get('cpt',0)
    cpt+=1
    session['cpt']=cpt
    d = {'result': cpt}
    return jsonify(d)
