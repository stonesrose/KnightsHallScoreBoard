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

def update(request, match_id=0):
    currentRound = matchRounds.objects.latest('id')

    if request.method == 'POST': # If the form has been submitted...
        print request.POST
        for key,value in request.POST.iteritems():
           print("%s: %s"%(key, value))
           if key != "csrfmiddlewaretoken":
              winner=key
    else:
        context = {'currentRound': currentRound}
        return render(request, 'scoreboard/scoreupdate.html', context)

    if winner == "home":
        currentRound=matchRounds.objects.create(matchInfo = currentRound.matchInfo,
            round= currentRound.round + 1,
            homeTeamScore = currentRound.homeTeamScore + 1,
            awayTeamScore = currentRound.awayTeamScore)
    elif winner == "away":
        currentRound=matchRounds.objects.create(matchInfo = currentRound.matchInfo,
            round = currentRound.round + 1,
            homeTeamScore = currentRound.homeTeamScore,
            awayTeamScore = currentRound.awayTeamScore + 1)

    #Ok
    # if request.POST['homeWin']:
    #     print "HOMEWIN"

    # elif request.POST['awayWin']:
    #     print "awayWIN"

    print currentRound
    context = {'currentRound': currentRound}
    return render(request, 'scoreboard/scoreupdate.html', context)

def create(request):
    if request.method == 'GET' : # If the form has been submitted...
        print request.GET
        teams=teamInfo.objects.all()

        context = {'teams': teams}
        return render(request, 'scoreboard/scorecreate.html', context)
    else:
        teams=teamInfo.objects.all()

        context = {'teams': teams}
        return render(request, 'scoreboard/scorecreate.html', context)

def double(request):
    currentRound = matchRounds.objects.latest('id')
    print currentRound.matchInfo.homeTeam
    context = {'currentRound': currentRound}
    return render(request, 'scoreboard/dualScoreboard.html', context)