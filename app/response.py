from flask import jsonify


def ok(values, message, total=None):
    res = {
        'values': values,
        'message': message
    }
    if total not in ["", None, 0]:
        res['total_values'] = total

    response = jsonify(res)
    response.status_code = 200
    return response


def badRequest(values, message):
    res = {
        'values': values,
        'message': message
    }

    response = jsonify(res)
    response.status_code = 400
    return response


def unAuthorized(values, message):
    res = {
        'values': values,
        'message': message
    }

    response = jsonify(res)
    response.status_code = 401
    return response
