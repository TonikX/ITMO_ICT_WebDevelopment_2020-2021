# List of all chickens (nested)

Выводит информацию обо всех курицах, подробную информацию об их породах и клетках

**URL** : `/chickens/list/nested/`

**Method** : `GET`

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
[
    {
        "id": 1,
        "breed": {
            "id": 1,
            "breed": "Columbian",
            "productivity": "avg",
            "avg_weight": 3,
            "diet": "Vegetables & fruits"
        },
        "cell": {
            "id": 2,
            "cell": 15,
            "row": 11,
            "tsekh": 10
        },
        "weight": 4,
        "age": 2,
        "egg_amount": 18
    }
]
```

```python
class ChickenNestedSerializer(serializers.ModelSerializer):
    breed = BreedSerializer()
    cell = CellSerializer()

    class Meta:
        model = Chicken
        fields = "__all__"
```