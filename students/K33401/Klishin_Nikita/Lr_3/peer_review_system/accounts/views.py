from accounts.serializers import StudentSerializer
from accounts.models import StudentProfile
from django.shortcuts import render

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
# from .permissions import IsOwnerProfileOrReadOnly
#from .serializers import UserProfileSerializer


# class UserProfileListCreateView(ListCreateAPIView):
#     queryset=UserProfile.objects.all()
#     serializer_class=UserProfileSerializer
#     # permission_classes=[IsAuthenticated]

#     def perform_create(self, serializer):
#         user=self.request.user
#         serializer.save(user=user)


# class userProfileDetailView(RetrieveUpdateDestroyAPIView):
#     queryset=UserProfile.objects.all()
#     serializer_class=UserProfileSerializer
#     permission_classes=[IsAuthenticated]

class StudentListView(generics.ListAPIView):
	queryset = StudentProfile.objects.all()
	serializer_class = StudentSerializer


class StudentDetailView(generics.RetrieveUpdateAPIView):
	queryset = StudentProfile.objects.all()
	serializer_class = StudentSerializer