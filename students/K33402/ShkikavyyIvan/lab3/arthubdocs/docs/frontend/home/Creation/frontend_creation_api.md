# Интерфейсы

## Отображение информации об определенном произведении

#### /api/creations/id/' (GET)

```js
loadCreation()
{
    $.ajax({
        url: 'http://127.0.0.1:8000/api/creations/' + this.$route.params.id + '/',
        type: 'GET',
        success: (response) => {
            this.creation = response
        },
        error: (response) => {
            alert(response)
        }
    })
}
```

##Подгрузка комментариев о данном произведении

#### /api/reviews/creation/id/ (GET)

```js
 loadReviews()
{
    $.ajax({
        url: 'http://127.0.0.1:8000/api/reviews/creation/' + this.$route.params.id + '/',
        type: 'GET',
        success: (response) => {
            this.reviews = response
        },
        error: (response) => {
            alert(response)
        }
    })
}
```