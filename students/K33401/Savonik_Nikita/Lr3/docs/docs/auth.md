<h1>Авторизация и Регистрация</h1>

<h3>Авторизация <b>POST</b><h3> 
<code>protocol:Host:port/api/auth/token/login/</code> <br>

<b>Header</b>
<ul>
    <li>
    Content-Type:multipart/form-data
    </li>
    <li>Accept: application/json</li>
</ul>

<b>Body</b>
<ul>
    <li>username: username</li>
    <li>password: password</li>
</ul>

<h3>Регистрация <b>POST</b><h3>
<code>protocol:Host:port/api/auth/users/</code> <br>

<b>Header</b>
<ul>
    <li>
    Content-Type:multipart/form-data
    </li>
    <li>Accept: application/json</li>
    <li>Authorization: Token <em>token</em></li>
</ul>

<b>Body</b>
<ul>
    <li>username: username</li>
    <li>password: password</li>
</ul>

<h3>Изменение, получение, удаление данных <b>GET / PATCH / PUT / DELETE</b><h3> 
<code>protocol:Host:port/api/auth/users/me/</code> <br>

<b>Header</b>
<ul>
    <li>
    Content-Type:multipart/form-data
    </li>
    <li>Accept: application/json</li>
     <li>Authorization: Token <em>token</em></li>
</ul>

<b>Body</b>
optional
