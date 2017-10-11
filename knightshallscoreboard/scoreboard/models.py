from django.db import models

class teamInfo(models.Model):
    teamName = models.CharField(max_length=100, primary_key=True)
    teamImage = models.CharField(max_length=100, default="ACL_defaul.png" )
    teamColors = models.CharField(max_length=100, default="#ffffff,#ffffff") #comma seperated 2 RGB primary colors:  balck,white = #000000,#ffffff
    teamLocation = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.teamName
    class Meta:
        ordering = ['teamName']


class matchType(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    fightsperRound = models.IntegerField()
    maxRounds = models.IntegerField(blank=True, null=True)
    maxScore = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return self.name

class matchInfo(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    matchDate = models.DateField()
    matchTime = models.TimeField()
    matchLocation = models.CharField(max_length=100)
    matchtype = models.ForeignKey(matchType)
    homeTeam = models.ForeignKey(teamInfo, related_name='homeTeam',)
    awayTeam = models.ForeignKey(teamInfo, related_name='awayTeam',)
    numberRounds = models.IntegerField(blank=True, null=True)
    matchComplete = models. BooleanField(blank=True)
    matchnumber = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

class matchRounds(models.Model):
    matchInfo = models.ForeignKey(matchInfo)
    round = models.IntegerField()
    homeTeamScore = models.IntegerField()
    awayTeamScore = models.IntegerField()







