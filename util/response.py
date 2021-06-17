from flask import jsonify

def wrapResp(controllCallback):
    try:
        data = controllCallback()
    except Exception as e:
        return jsonify({ "status": "NG", "message": str(e) })
    else:
        return jsonify({ "status": "OK", "data": data })