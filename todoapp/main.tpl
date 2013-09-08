<!DOCTYPE html>
<html>
    <head>
        <title>Todo Application</title>
    </head>
    
    <body>
        <h1>Todo List</h1>
       %if defined('username'):
        <p>Welcome, {{username}}</p>
       %end
        <p><a href="/login">Login</a></p>
        <p><a href="/register">Register</a></p>
       %if defined('serverError'):
        <p>API error: {{serverError}}</p>
       %end
       %for todo in get('todo', []):
        <form action="?id={{todo['id']}}" method="POST">
            <input type="checkbox" name="completed" value="True"{{' checked' if todo['completed'] else ''}} />
            <input type="text" name="title" size="50" value="{{todo['title']}}" required />
            <input type="text" name="dueTo" value="{{todo['dueTo'] or ''}}" />
            <input type="text" name="priority" value="{{todo['priority']}}" required />
            <input type="submit" name="action" value="save" />
            <input type="reset" value="reset" />
            <input type="submit" name="action" value="delete" />
        </form>
       %    if defined('changedId') and int(changedId) == todo['id']:
       %        if defined('clientError'):
        <p>Error: {{': '.join(key + ': ' + (value[0] if isinstance(value, list) else value) for key, value in clientError.items())}}</p>
       %        else:
        <p>Saved.</p>
       %        end
       %    end
       %end
        <form action="/" method="POST">
            <input type="checkbox" name="completed" value="True" />
            <input type="text" name="title" size="50" required />
            <input type="text" name="dueTo" />
            <input type="text" name="priority" value="Minor" required />
            <input type="submit" name="action" value="save" />
            <input type="reset" value="reset" />
        </form>
       %if not defined('changedId') and defined('clientError'):
        <p>Error: {{': '.join(key + ': ' + (value[0] if isinstance(value, list) else value) for key, value in clientError.items())}}</p>
       %end
        <p><a href="/orderBy/dueTo">Sort by due to</a></p>
        <p><a href="/orderBy/priority">Sort by priority</a></p>
    </body>
</html>

