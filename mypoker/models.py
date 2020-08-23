from django.db import models


# Create your models here.

class Player1(models.Model):
    name = models.CharField(max_length=16)
    address = models.CharField(max_length=16)

    def __str__(self):
        return self.name


class simpleMeeting(models.Model):
    date = models.DateField(blank=True, default='2020-01-01')
    house = models.ForeignKey(Player1, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.house) + " : " + str(self.date)


class SimpleGame(models.Model):
    noam = models.IntegerField(default=0)
    johnny = models.IntegerField(default=0)
    moshe = models.IntegerField(default=0)
    ahon = models.IntegerField(default=0)
    dror = models.IntegerField(default=0)
    meeting = models.ForeignKey(simpleMeeting, blank=True, null=True, default=None, related_name='games',
                                on_delete=models.SET_NULL)

    # def __str__(self):
        # return str(self.meeting) + ": " + str(self.id)


class Hand(models.Model):
    DIET_CHOICES = [('FLASH', 'Flush'), ('FULL HOUSE', 'Full house'), ('FOUR OF A KIND', 'Four of a kind'),
                    ('STRAIGHT FLUSH', 'Straight flush')]
    type = models.CharField(max_length=50, choices=DIET_CHOICES, blank=True)
    description = models.CharField(max_length=50, blank=True, null=True, default=None)
    player = models.ForeignKey(Player1, related_name='hands', blank=True, null=True, default=None,
                               on_delete=models.SET_NULL)
    meeting = models.ForeignKey(simpleMeeting, related_name='hands', blank=True, null=True, default=None,
                                on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.type) + ": " + str(self.description)

#
# class SimpleMeeting2(models.Model):
#     date = models.DateField(blank=True, default='2020-01-01')
#     house = models.ForeignKey(Player1, null=True, on_delete=models.SET_NULL)
#
#
# class Player2(models.Model):
#     name = models.CharField(max_length=16)
#     address = models.CharField(max_length=16)
#
#     def __str__(self):
#         return self.name
#
#
# class SimpleGame2(models.Model):
#     meeting = models.ForeignKey(simpleMeeting, blank=True, null=True, default=None, related_name='games',
#                                 on_delete=models.SET_NULL)
#     price = models.IntegerField(default=20)
#     participants = models.ManyToManyField(Player2, blank=True, null=True, default=None, related_name='games')
