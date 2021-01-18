# Интерфейсы

## Отображение всех авторов

#### /api/authors/ (GET)

```js
loadAuthors()
{
    $.ajax({
        url: 'http://127.0.0.1:8000/api/authors/',
        type: 'GET',
        success: (response) => {
            this.authors = response
        },
        error: (response) => {
            alert(response)
        }
    })
}
```