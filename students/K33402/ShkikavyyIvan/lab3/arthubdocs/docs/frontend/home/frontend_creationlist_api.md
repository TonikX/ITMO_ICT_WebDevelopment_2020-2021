# Интерфейсы

## Отображение всех произведений искусств

#### /api/creations/ (GET)

```js
 loadCreations()
{
    $.ajax({
        url: 'http://127.0.0.1:8000/api/creations/',
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

##Удаление произведений искусств

#### /api/creations/id/delete/ (DELETE)

```js
deleteCreation(creationId)
{
    $.ajax({
        url: 'http://127.0.0.1:8000/api/creations/' + creationId + '/delete/',
        type: 'DELETE',
        success: (response) => {
            alert('Запись удалена')
            this.loadCreations()
        },
        error: (response) => {
            alert(response)
        }
    })
}
```
## Создание произведения

#### api/creations/create/ (POST)

- name
- description
- creator
- type

```js
 newCreation()
{
    $.ajax({
        url: 'http://127.0.0.1:8000/api/creations/create/',
        type: 'POST',
        data: {
            name: this.name,
            description: this.description,
            creator: this.creator,
            type: this.type
        },
        success: (response) => {
            alert('Создано произведение')
            console.log(response)
            this.$router.push({name: 'Home'})
        },
        error: (response) => {
            alert(response)
        }
    })
}
```
