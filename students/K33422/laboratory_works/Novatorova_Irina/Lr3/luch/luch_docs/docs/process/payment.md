# Список платежных поручений
Выводит список платежных поручений с указанием заявки, клиента и услуги c возможностью фильтрации по клиенту

**URL** : `/luch/payment_order/list`

**Method** : `GET`

**Data constraints** : `{}`

###С фильтрацией по сотруднику (id клиента=1)
**URL** : `/luch/payment_order/list?client=1`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

views.py:

```json
class PaymentOrderNestedAPIView(generics.ListAPIView):
    serializer_class = PaymentOrderNestedSerializer

    def get_queryset(self):
        queryset = Payment_order.objects.all()

        params = self.request.query_params

        client = params.get('client', None)

        if client:
            queryset = queryset.filter(client=client)

        return queryset