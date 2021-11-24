import functools
from rest_framework import serializers


def validator_(obj, data, func=None):
    errors = {}
    if not func is None:
        is_valid_ = functools.partial(func, data=data)
        for i in data.keys():
            try:
                data[i] = is_valid_(i)
            except Exception as error:
                data[i] = None
                errors[i] = error

    obj.is_valid()
    for i in obj.errors.items():
        errors[i[0]] = i[1][0]

    if len(errors) != 0:
        raise serializers.ValidationError(errors)
    return data

