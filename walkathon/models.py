from django.db import models

# TODO  More contact info (address, phone #)?

# Create your models here.
class Participant(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    statement = models.TextField()
    # picture

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

    active = models.BooleanField(default=True)
    created_on = models.DateTimeField()

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
