# Интерфейсы

## Cоздание отзыва

#### /api/reviews/create/ (POST)

- text
- rating
- creation

```js
sendReview()
{
    $.ajax({
        url: 'http://127.0.0.1:8000/api/reviews/create/',
        type: 'POST',
        data: {
            text: this.text,
            rating: this.rating,
            creation: this.creationId
        },
        success: (response) => {
            alert('Спасибо за отзыв')
            console.log(response)
            this.$router.push({name: 'Home'})
        },
        error: (response) => {
            alert(response)
        }
    })
}
```