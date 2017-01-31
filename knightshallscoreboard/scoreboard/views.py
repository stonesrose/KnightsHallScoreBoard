from django.shortcuts import render

# Create your views here.

from .models import matchRounds, matchInfo, teamInfo

def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    currentRound = matchRounds.objects.latest('id')
    print currentRound.matchInfo.homeTeam
    #teamNames = currentRound.matchInfo.
    context = {'currentRound': currentRound}
    return render(request, 'scoreboard/scoreboard.html', context)