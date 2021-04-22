from django.shortcuts import render, redirect
from rest_framework import generics
# from django.core.exceptions import ValidationError
from rest_framework.exceptions import APIException
from datetime import datetime
from django.db.models import Count

from .models import *
from .serializers import *

# Create your views here.


def home(request):
    peaks = Peak.objects.all()
    climbers = Person.objects.all()
    return render(request, 'climbing_club_app/index.html', context={'arr': range(10), 'peaks': peaks, 'climbers': climbers})


def redirect_home(request):
    return redirect('/home')


def lala(request):
    print()
    print('request', request.GET['from'])
    print('*****************************')
    return redirect_home(request)


class ClimberCreateAPIView(generics.CreateAPIView):
    serializer_class = ClimberSerializer


class PeakCreateAPIView(generics.CreateAPIView):
    serializer_class = PeakSerializer


class ClimberRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = ClimberSerializer
    queryset = Person.objects.all()


class PeakRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = PeakSerializer
    queryset = Peak.objects.all()


class ClimbingCreateAPIView(generics.CreateAPIView):
    serializer_class = ClimbingSerializer


class ParticipationCreateAPIView(generics.CreateAPIView):
    serializer_class = ParticipationSerializer


class EmergencySituationCreateAPIView(generics.CreateAPIView):
    serializer_class = EmergencySituationSerializer

    def perform_create(self, serializer):
        climbing = int(self.request.data['climbing'][0])
        participant = int(self.request.data['person'][0])
        if not Participation.objects.filter(climbing_id=climbing, participant_id=participant).count():
            raise APIException(
                'Альпинист не участвовал в указанном восхождении, нештатные ситуации невозможны')
        serializer.save()


class ClimberClimbingListAPIView(generics.ListAPIView):
    serializer_class = ClimberSerializer

    def get_queryset(self):
        # lte for less than or equal
        from_date = [int(i)
                     for i in self.request.query_params.get('from').split('-')]
        from_date = datetime(*from_date)
        to_date = [int(i)
                   for i in self.request.query_params.get('to').split('-')]
        to_date = datetime(*to_date, 23, 59, 59)
        queryset = Person.objects.filter(
            climbings__start_time__lte=to_date, climbings__finish_time__gte=from_date)
        print(queryset)
        return queryset


class FromToClimbingListAPIView(generics.ListAPIView):
    serializer_class = ClimbingSerializer

    def get_queryset(self):
        # lte for less than or equal

        from_date = [int(i)
                     for i in self.request.query_params.get('from').split('-')]
        from_date = datetime(*from_date)
        to_date = [int(i)
                   for i in self.request.query_params.get('to').split('-')]
        to_date = datetime(*to_date, 23, 59, 59)
        queryset = Climbing.objects.filter(
            start_time__lte=to_date, finish_time__gte=from_date)
        print(queryset)
        return queryset


class ClimbersOnPeakListAPIView(generics.ListAPIView):
    serializer_class = ClimberSerializer

    def get_queryset(self):
        pk = int(self.kwargs['pk'])
        queryset = Person.objects.filter(climbings__peak_id=pk).distinct()
        return queryset


class PeakWithoutClimbingListAPIView(generics.ListAPIView):
    serializer_class = PeakSerializer
    # is there a lookup for count objects?

    def get_queryset(self):
        queryset = Peak.objects.annotate(num_climbings=Count(
            'climbings')).filter(num_climbings=0)
        print(queryset)
        return queryset


class CountClimbersOnPeakListAPIView(generics.ListAPIView):
    serializer_class = CountClimbersSerializer

    def get_queryset(self):
        pk = int(self.kwargs['pk'])
        queryset = Person.objects.filter(climbings__peak_id=pk).annotate(
            climbings_on_peak=Count('climbings'))
        return queryset
