<!DOCTYPE html>
<html>
    <head>
        <title>Todo Application</title>
    </head>
    
    <body>
        <p><a href="/">Main page</a></p>
       %if defined('serverError'):
        <p>API error: {{serverError}}</p>
       %end
        <form action="/register" method="POST">
            <p>Email: <input type="text" name="email" required /></p>
            <p>Username: <input type="text" name="username" required /></p>
            <p>Password: <input type="password" name="password" required /></p>
            <p><input type="submit" name="action" value="register" /></p>
        </form>
       %if defined('successful'):
        <p>Registered.</p>
       %end
       %if defined('clientError'):
        <p>Error: {{': '.join(key + ': ' + (value[0] if isinstance(value, list) else value) for key, value in clientError.items())}}</p>
       %end
    </body>
</html>

