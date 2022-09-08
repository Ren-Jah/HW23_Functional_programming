# с помощью функционального программирования (функций filter, map),
# итераторов/генераторов сконструировать запрос
def query_constructor(cmd, value, data):
    """ Конструктор запроса с использованием ФП """
    if cmd == 'filter':
        result = filter(lambda x: value in x, data)
        return result

    if cmd == 'map':
        value = int(value)
        result = map(lambda x: x.split(" ")[value], data)
        return result

    if cmd == 'unique':
        result = list(set(data))
        return result

    if cmd == 'sort':
        reverse = bool(value)
        result = sorted(data, reverse=reverse)
        return result

    if cmd == 'limit':
        value = int(value)
        result = list(data)[:value]
        return result
