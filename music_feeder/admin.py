from django.contrib import admin
from .models import MusicFile, TestSession, TestPlay


class MusicFileAdmin(admin.ModelAdmin):
    class Meta:
        model = MusicFile
        fields = '__all__'


class TestSessionAdmin(admin.ModelAdmin):
    class Meta:
        model = TestSession
        fields = '__all__'


class TestPlayAdmin(admin.ModelAdmin):
    class Meta:
        model = TestPlay
        fields = '__all__'

