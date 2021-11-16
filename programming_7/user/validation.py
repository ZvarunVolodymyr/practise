import re
from user import security


def get_validation_functions(name):
    a = {'id': is_empty, 'id_of_certificate': is_empty, 'first_name': is_username, 'last_name': is_username, 'email': is_empty,
         'password': is_password}
    if not name in a.keys():
        raise ValueError('такого поля не існує')
    return a[name]


def validation(name, data):
    return get_validation_functions(name)(data, name)


def attributes(func):
    def decorator(data, name):
        try:
            attributes = [data[name]]
            return func(*attributes)
        except ValueError as error:
            raise error
        except KeyError:
            raise ValueError('такого поля не існує')

    return decorator


@attributes
def is_empty(value):
    return value


@attributes
def is_username(n):
    if not n.isalpha():
        raise ValueError(str(n) + ' не є username')
    return n


@attributes
def is_password(n):
    if len(re.findall('[A-Z]', n)) == 0:
        raise ValueError(str(n) + ' має містити великі букви')
    if len(re.findall('[a-z]', n)) == 0:
        raise ValueError(str(n) + ' має містити малі букви')
    if len(re.findall('[0-9]', n)) == 0:
        raise ValueError(str(n) + ' має містити числа')
    if len(re.findall('\w', n)) != len(n):
        raise ValueError(str(n) + ' не має містити непідходящих символів')
    return security.hash(n)
