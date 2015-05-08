from django.conf.urls import patterns, include, url

from music_feeder.views import IndexView, TrackerView

from rest_framework import routers

from music_feeder.viewsets import MusicFileViewSet, TestSessionViewSet, TestPlayViewSet


router = routers.DefaultRouter()
router.register(r'musicfile', MusicFileViewSet)
router.register(r'testsession', TestSessionViewSet)
router.register(r'testplay', TestPlayViewSet)


urlpatterns = patterns(
    '',
    url(r'^api/', include(router.urls)),
    url(r'^tracker/$', TrackerView.as_view(), name='tracker'),
    url(r'^.*$', IndexView.as_view(), name='index'),
)
