#  Публикация данных о воинах


**URL** : `warriors/`

**Method** : `POST`

**Data constraints** : `{}`

**Content-Type** : application/json

**Python code** :
```python
def post(self, request):
   warrior = request.data.get("warrior")
   serializer = WarriorSerializer(data=warrior)
   if serializer.is_valid(raise_exception=True):
      serializer.save()
   return Response({"Success": "Created succesfully."})
```