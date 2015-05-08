from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from uuidfield import UUIDField
# from multiselectfield import MultiSelectField


class MusicFile(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return "[%s %s]" % (self.id, self.name)


class TestSession(models.Model):
    uuid = UUIDField(auto=True, unique=True)
    ip_address = models.IPAddressField()
    referral_link = models.CharField(max_length=200)
    referral_code = models.CharField(max_length=200)
    # demographic = models.ForeignKey(TestDemographic)

    def __unicode__(self):
        return "[%s %s]" % (self.id, self.uuid)


class TestPlay(models.Model):
    NOT_INTERESTING = 'NOT_INTERESTING'
    TOO_LONG = 'TOO_LONG'
    NOT_MY_TASTE = 'NOT_MY_TASTE'
    NOT_RIGHT_MOOD = 'NOT_RIGHT_MOOD'

    SKIPPING_REASON_CHOICES = (
        (NOT_INTERESTING, _("Not interesting or exciting enough")),
        (TOO_LONG, _("Interesting but too long or repetitive")),
        (NOT_MY_TASTE, _("Just not my taste")),
        (NOT_RIGHT_MOOD, _("Not the right mood, but would listen to it again")),
    )

    musaic = models.ForeignKey(MusicFile)
    session = models.ForeignKey(TestSession)
    is_skipped = models.BooleanField(default=False)
    is_listened_before = models.BooleanField(default=False)
    listened_ratio = models.IntegerField(default=50)
    skipping_reason = models.CharField(max_length=16, choices=SKIPPING_REASON_CHOICES, blank=True, null=True)

    def __unicode__(self):
        return "[%s for session:%s]" % (self.id, self.session.id)


class TestDemographic(models.Model):
    AGE_RANGE_CHOICES = (
        ("< 18", _("< 18")),
        ("18 - 25", _("18 - 25")),
        ("25 - 40", _("25 - 40")),
        ("40+", _("40+"))
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    age_range = models.CharField(max_length=20, choices=AGE_RANGE_CHOICES, blank=False)

    music_job = models.CharField(max_length=100, choices=AGE_RANGE_CHOICES, blank=False)
    music_personal = models.CharField(max_length=100, choices=AGE_RANGE_CHOICES, blank=False)
    music_experience_pro = models.CharField(max_length=100, choices=AGE_RANGE_CHOICES, blank=False)
    music_experience_stu = models.CharField(max_length=100, choices=AGE_RANGE_CHOICES, blank=False)
    music_genres = models.CharField(max_length=100)
    music_event = models.CharField(max_length=100)
    music_last_event = models.CharField(max_length=100)

    like = models.CharField(max_length=100)
    improve = models.CharField(max_length=500)
    other = models.CharField(max_length=500)
