from flask import Blueprint, session, request, jsonify


from . import getOptions, Option, optionsToJSON, optionsJSONtoEnum

bp = Blueprint('api', __name__)


@bp.route('/options',methods=('POST',))
def options():
    """ Récupère les options stockées dans localStorage (côté client) et les stocke dans la session (côté serveur).
        L'envoi est effectué par du JS côté client
    """
    session['options']=optionsJSONtoEnum(request.get_json())
    return {}
