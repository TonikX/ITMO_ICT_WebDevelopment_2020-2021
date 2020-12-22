from itertools import groupby
from django.utils import timezone
from django.db.models.functions import TruncDate
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Event
from .serializers import EventSerializer, ScheduleSerializer


class EventViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()


    @action(detail=False, methods=['GET'])
    def completed(self, request, *args, **kwargs):
        queryset = Event.objects.completed()

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['GET'])
    def schedule(self, request, *args, **kwargs):
        from_date = timezone.localtime(timezone.now())
        until_date = from_date + timezone.timedelta(days=30)
        date_today = from_date.date()
        events = Event.objects.filter(
            start_date__lt=until_date,
            start_date__gt=from_date).annotate(start_day=TruncDate(
                'start_date')).order_by('-end_date').values(
                    'id', 'title', 'description', 'category',
                    'start_day', 'start_date', 'end_date')
        events_dict = {}
        events_sorted = sorted(list(events), key=lambda event: event["start_day"])
        events_grouped_by_date = groupby(events_sorted, lambda event: event["start_day"])

        for date, group_of_events in events_grouped_by_date:
            dict_key = date.strftime('%s')
            events_dict[dict_key] = ScheduleSerializer(
                group_of_events, many=True).data

        if len(events) < 30:
            dates = set([(date_today + timezone.timedelta(days=i))
                         for i in range(29)])
            events_set = set([event["start_day"] for event in events])
            for dt in (dates - events_set):
                events_dict.update({dt.strftime('%s'): []})
        events_sorted = dict(sorted(events_dict.items()))
        return Response(events_sorted)
