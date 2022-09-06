<h1>Три эдпоинты</h1>

##Обновление заказа
<ul>
    <li>api/orders/pk/update/ <br>
    <em><b>METHOD</b>: PUT/PATCH </em> <br>
    <em><b>PERMISSIONS</b>: IsOwner</em> <br>
    <em><b>Header</b>: <br>
    Content-Type:multipart/form-data <br>
    Accept: application/json <br>
    Authorization: Token token</em><br>
    <em><b>Body</b>: <br>
    optional </em><br>
    <b>Code</b>: 200 OK
    </li>
</ul>

##Обновление кота
<ul>
    <li>api/cats/pk/update/ <br>
    <em><b>METHOD</b>: PUT/PATCH </em> <br>
    <em><b>PERMISSIONS</b>: IsAdminUser</em> <br>
    <em><b>Header</b>: <br>
    Content-Type:multipart/form-data <br>
    Accept: application/json <br>
    Authorization: Token token</em><br>
    <em><b>Body</b>: <br>
    optional </em><br>
    <b>Code</b>: 200 OK
    </li>
</ul>
##Обновление кота в заказе
<ul>
    <li>api/cat_to_orders/pk/update/ <br>
    <em><b>METHOD</b>: PUT/PATCH </em> <br>
    <em><b>PERMISSIONS</b>: IsOwnerCatToOrder</em> <br>
    <em><b>Header</b>: <br>
    Content-Type:multipart/form-data <br>
    Accept: application/json <br>
    Authorization: Token token</em><br>
    <em><b>Body</b>: <br>
    optional </em><br>
    <b>Code</b>: 200 OK
    </li>
</ul>