from django.shortcuts import redirect, render

from apps.core.auth import admin_login_required
from apps.matches.dtos.match_dto import UpsertMatchDTO
from apps.matches.services.impl import MatchServiceImpl
from apps.teams.services.impl import TeamServiceImpl


match_service = MatchServiceImpl()
team_service = TeamServiceImpl()


def public_list(request):
    matches = match_service.list_matches()
    return render(request, 'matches/public_list.html', {'matches': matches})


@admin_login_required
def admin_list(request):
    matches = match_service.list_matches()
    return render(request, 'matches/admin_list.html', {'matches': matches, 'status': request.GET.get('status')})


@admin_login_required
def add_page(request):
    teams = team_service.get_all_teams()
    return render(request, 'matches/add.html', {'teams': teams, 'status': request.GET.get('status')})


@admin_login_required
def add_action(request):
    if request.method != 'POST':
        return redirect('matches:add_page')

    dto = UpsertMatchDTO(
        match_id=int(request.POST.get('matchId', 0)),
        team1_code=request.POST.get('team1', ''),
        team2_code=request.POST.get('team2', ''),
        venue=request.POST.get('venue', ''),
        match_date=request.POST.get('matchDate', ''),
        match_time=request.POST.get('matchTime', ''),
        status=request.POST.get('status', 'upcoming'),
        winner_code=request.POST.get('winnerCode', ''),
        team1_score=request.POST.get('team1Score', ''),
        team2_score=request.POST.get('team2Score', ''),
        player_of_match=request.POST.get('playerOfMatch', ''),
    )
    ok, _ = match_service.create_match(dto)
    return redirect('matches:admin_list' if ok else 'matches:add_page')


@admin_login_required
def edit_page(request, match_id: int):
    match = match_service.get_match(match_id)
    if not match:
        return redirect('matches:admin_list')
    teams = team_service.get_all_teams()
    return render(request, 'matches/update.html', {'match': match, 'teams': teams, 'status': request.GET.get('status')})


@admin_login_required
def update_action(request):
    if request.method != 'POST':
        return redirect('matches:admin_list')
    dto = UpsertMatchDTO(
        match_id=int(request.POST.get('matchId', 0)),
        team1_code=request.POST.get('team1', ''),
        team2_code=request.POST.get('team2', ''),
        venue=request.POST.get('venue', ''),
        match_date=request.POST.get('matchDate', ''),
        match_time=request.POST.get('matchTime', ''),
        status=request.POST.get('status', 'upcoming'),
        winner_code=request.POST.get('winnerCode', ''),
        team1_score=request.POST.get('team1Score', ''),
        team2_score=request.POST.get('team2Score', ''),
        player_of_match=request.POST.get('playerOfMatch', ''),
    )
    ok, _ = match_service.update_match(dto)
    return redirect('matches:admin_list' if ok else f"{request.path_info}?status=error")


@admin_login_required
def delete_action(request, match_id: int):
    if request.method != 'POST':
        return redirect('matches:admin_list')
    match_service.delete_match(match_id)
    return redirect('matches:admin_list')
