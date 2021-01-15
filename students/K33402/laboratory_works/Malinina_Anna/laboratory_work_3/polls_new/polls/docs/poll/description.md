# Описание опроса

Опрос содержит в себе вопросы с несколькими вариантами ответа, тему, создателя, описание, примерное время прохождения

Структура опроса:
```json
{
  "id": 0,
  "creator": {
    "id": 0,
    "username": "string",
    "name": "string",
    "email": "user@example.com",
    "date_of_birth": "2020-12-06"
  },
  "question_set": [
    {
      "id": 0,
      "answer_set": [
        {
          "id": 0,
          "description": "string",
          "question": 0
        }
      ],
      "description": "string",
      "poll": 0
    }
  ],
  "title": "string",
  "create_date": "2020-12-06T15:48:08.285Z",
  "description": "string",
  "voting_time": 0,
  "theme": "string"
}
```

Методы для работы с опросами:

* GET /poll/ poll_list

* POST /poll/ poll_create

* GET
/poll/{id}/
poll_read

* PUT
/poll/{id}/
poll_update

* DELETE
/poll/{id}/
poll_delete

