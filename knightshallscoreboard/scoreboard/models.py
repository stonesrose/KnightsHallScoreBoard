from django.db import models

class teamInfo(models.Model):
    teamName = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.teamName


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

    def __str__(self):
        return self.name

class matchRounds(models.Model):
    matchInfo = models.ForeignKey(matchInfo)
    round = models.IntegerField()
    homeTeamScore = models.IntegerField()
    awayTeamScore = models.IntegerField()







