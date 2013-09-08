import bottle

from api import JSONAPI

app = bottle.Bottle()

@app.get('/register')
@app.post('/register')
def register(**kwargs):
    if bottle.request.forms:
        api = JSONAPI('http://localhost:8000/')
        response = api.post('register', **bottle.request.forms)

        if response.successful():
            kwargs['successful'] = True
        if response.clientError():
            kwargs['clientError'] = response.body()
        elif response.serverError():
            kwargs['serverError'] = str(response)

    return bottle.template('register', **kwargs)

@app.get('/login')
def login():
    '''Ask for HTTP basic authentication.'''
    if not bottle.request.auth:
        bottle.response.status = '401 - Unauthorized'
        bottle.response.headers['WWW-Authenticate'] = 'Basic realm="Todo Application"'
    else:
        bottle.redirect('/')

@app.get('/')
@app.get('/orderBy/<column>')
def main(column='createdAt', **kwargs):
    if not bottle.request.auth:
        login()
    else:
        api = JSONAPI('http://localhost:8000/', *bottle.request.auth)
        response = api.get('todo', ordering=column)

        kwargs['username'] = bottle.request.auth[0]
        if response.successful():
            kwargs['todo'] = response.body()
        elif response.serverError():
            kwargs['serverError'] = str(response)

    return bottle.template('main', **kwargs)

@app.post('/')
@app.post('/orderBy/<column>')
def update(**kwargs):
    api = JSONAPI('http://localhost:8000/', *bottle.request.auth)
    action = bottle.request.forms.pop('action')

    if 'id' in bottle.request.query:
        if action == 'save':
            response = api.put('todo', bottle.request.query['id'], **bottle.request.forms)
        elif action == 'delete':
            response = api.delete('todo', bottle.request.query['id'])
        kwargs['changedId'] = bottle.request.query['id']
    elif action == 'save':
        '''Create new one.'''
        response = api.post('todo', **bottle.request.forms)
        if response.successful():
            kwargs['changedId'] = response.body()['id']

    if response.clientError():
        kwargs['clientError'] = response.body()
    elif response.serverError():
        kwargs['serverError'] = str(response)

    return main(**kwargs)

if __name__ == '__main__':
    bottle.debug(True)
    app.run(host='localhost', port=8080, reloader=True)

