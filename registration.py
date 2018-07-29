registry = []
def register(func):
    print('running register(%s)' % func)
    registry.append(func)
    return func