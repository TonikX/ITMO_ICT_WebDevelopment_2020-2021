# List of all services (nested)

Выводит информацию обо всех обслуживаниях, подробную информацию о сотрудниках и клетках

**URL** : `/service/list/nested/`

**Method** : `GET`

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
[
    {
        "id": 1,
        "username": {
            "first_name": "Ivan",
            "last_name": "Ivanov",
            "username": "firstuser",
            "passport": "7256 4629003",
            "salary": 10000,
            "cell": [
                2
            ]
        },
        "cell": {
            "id": 2,
            "cell": 15,
            "row": 11,
            "tsekh": 10
        },
        "status": true
    },
    {
        "id": 2,
        "username": {
            "first_name": "Tom",
            "last_name": "Jones",
            "username": "tomjones",
            "passport": "7623 9822034",
            "salary": 30000,
            "cell": [
                2
            ]
        },
        "cell": {
            "id": 2,
            "cell": 15,
            "row": 11,
            "tsekh": 10
        },
        "status": true
    }
]
```

```python
class ServiceNestedSerializer(serializers.ModelSerializer):
    username = UserSerializer()
    cell = CellSerializer()

    class Meta:
        model = Service
        fields = "__all__"
```