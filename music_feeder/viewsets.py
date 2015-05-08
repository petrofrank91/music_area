from __future__ import unicode_literals

from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import TestPlay, TestSession, MusicFile, TestDemographic
from .serializers import TestPlaySerializer, TestSessionSerializer, MusicFileSerializer


class MusicFileViewSet(viewsets.ModelViewSet):
    queryset = MusicFile.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = MusicFileSerializer


class TestSessionViewSet(viewsets.ModelViewSet):
    queryset = TestSession.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = TestSessionSerializer


class TestPlayViewSet(viewsets.ModelViewSet):
    queryset = TestPlay.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = TestPlaySerializer


class TestDemographicViewSet(viewsets.ModelViewSet):
    queryset = TestDemographic.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = TestPlaySerializer
