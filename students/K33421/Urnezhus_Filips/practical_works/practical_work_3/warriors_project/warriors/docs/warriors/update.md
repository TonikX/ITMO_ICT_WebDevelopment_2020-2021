# Обновить данные воинов

Обновляет информацию о воинах.

**URL** : `warriors/update/<int:pk>`

**Method** : `PUT`

**Data constraints** : `{}`

**Content-Type** : application/json

**Python code** :
```python
def put(self, request, pk=None):
    warrior = get_object_or_404(Warrior, pk=pk)
    serializer = WarriorSerializer(warrior, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST
```