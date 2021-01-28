# Регистрация и авторизация

Сервис подразумевает регистрацию пользователя в системе для создания заказов.

Регистрация выполняется по POST запросу:

**URL:** <code>host:port/auth/users/</code>

**Body:** 
<li>usernsme: usernsme</li>
<li>password: password</li>
<li>date of birth (optional)</li>
<li>email (optional)</li>

<br>
Авторизация выполняется по POST запросу:

**URL:** <code>host:port/auth/token/login/</code>

**Body:** 
<li>token: token</li>

<br>
Для авторизированного пользователя доступно редактирование данных и удаление провиля с помощью PUTCH и DELETE запросов:

**URL:** <code>host:port/auth/users/me/</code>

