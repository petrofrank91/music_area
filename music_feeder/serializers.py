from __future__ import unicode_literals

from rest_framework import serializers

from .models import MusicFile, TestPlay, TestSession, TestDemographic
from .fields import CurrentUserIPDefault


class MusicFileSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
        )
        model = MusicFile


class TestSessionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            #'url',
            'uuid',
            'ip_address',
            'referral_link',
            'referral_code',
        )
        extra_kwargs = {
            'ip_address': {
                'read_only': True,
                'default': CurrentUserIPDefault(),
            },
        }
        read_only_fields = ('uuid')
        model = TestSession


class TestPlaySerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            # 'url',
            'musaic',
            'session',
            'is_skipped',
            'is_listened_before',
            'listened_ratio',
            'skipping_reason',
        )
        extra_kwargs = {
            'listened_ratio': {'min_value': 0, 'max_value': 100},
            'is_skipped': {'required': True},
            'is_listened_before': {'required': True},
        }
        model = TestPlay

    def validate(self, data):
        request = self.context.get('request')
        session_uuid = request.query_params.get('session')
        #if session_uuid != str(data['session'].uuid):
        #    raise serializers.ValidationError("Wrong session uuid")
        return data


class TestDemographicSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestDemographic
