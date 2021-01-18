# Интерфейсы

## Отображение информации об авторе

#### /api/authors/id/ (GET)

```js
loadAuthor()
{
    $.ajax({
        url: 'http://127.0.0.1:8000/api/authors/' + this.$route.params.id + '/',
        type: 'GET',
        success: (response) => {
            this.author = response
        },
        error: (response) => {
            alert(response)
        }
    })
}
```

## Отображение всех произведений автора

#### //api/authors/creation/id/'

```js
loadCreation()
{
    $.ajax({
        url: 'http://127.0.0.1:8000/api/authors/creation/' + this.$route.params.id + '/',
        type: 'GET',
        success: (response) => {
            this.creations = response
        },
        error: (response) => {
            alert(response)
        }
    })
}
```