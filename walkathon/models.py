from django.db import models
# import datetime

# TODO  More contact info (address, phone #)?

# Create your models here.
class Participant(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    statement = models.TextField()
    # picture

    active = models.BooleanField(default=True)
    # auto time stamp
    # ?
    # created_on = models.DateTimeField(default=datetime.datetime.now())
    created_on = models.DateTimeField()

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

    @models.permalink
    def get_absolute_url(self):
        return ('walkathon.views.participant_detail', [str(self.id)])

    def full_name(self):
        return u'%s %s' % (self.first_name, self.last_name)

class Sponsor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    statement = models.TextField()
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    is_sponsoring = models.ForeignKey(Participant)

    active = models.BooleanField(default=True)
    created_on = models.DateTimeField()

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

    @models.permalink
    def get_absolute_url(self):
        return ('walkathon.views.sponsor_detail', [str(self.id)])

    def full_name(self):
        return u'%s %s' % (self.first_name, self.last_name)
