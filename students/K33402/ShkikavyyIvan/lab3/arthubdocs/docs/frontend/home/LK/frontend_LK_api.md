# Интерфейсы

## Отображение данных пользователя

#### /auth/users/me/ (GET)

```js
loadInfo()
{
    $.ajax({
        url: 'http://127.0.0.1:8000/auth/users/me/',
        type: 'GET',
        success: (response) => {
            this.user = response
        },
        error: (response) => {
            alert(response)
        }
    })
}
```

## Отображение комментариев пользователя

#### api/reviews/ (GET)

```js
loadReviews()
{
    $.ajax({
        url: 'http://127.0.0.1:8000/api/reviews/',
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

## Удаление комментариев пользователя

#### api/reviews/id/delete/ (DELETE)

```js
deleteReview(reviewId)
{
    $.ajax({
        url: 'http://127.0.0.1:8000/api/reviews/' + reviewId + '/delete/',
        type: 'DELETE',
        success: (response) => {
            alert('Запись удалена')
            this.loadReviews()
        },
        error: (response) => {
            alert(response)
        }
    })
}
```