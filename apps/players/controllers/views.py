from pathlib import Path

from django.core.files.storage import default_storage
from django.shortcuts import redirect, render

from apps.core.auth import admin_login_required
from apps.players.dtos.player_dto import CreatePlayerDTO, UpdatePlayerDTO
from apps.players.services.impl import PlayerServiceImpl
from apps.teams.services.impl import TeamServiceImpl


player_service = PlayerServiceImpl()
team_service = TeamServiceImpl()


def public_list(request):
    players = player_service.get_all_players()
    return render(request, 'players/public_list.html', {'players': players})


@admin_login_required
def admin_list(request):
    players = player_service.get_all_players()
    return render(request, 'players/admin_list.html', {'players': players, 'status': request.GET.get('status')})


@admin_login_required
def add_page(request):
    teams = team_service.get_all_teams()
    return render(request, 'players/add.html', {'teams': teams, 'status': request.GET.get('status')})


@admin_login_required
def add_action(request):
    if request.method != 'POST':
        return redirect('players:add_page')
    image_path = ''
    file = request.FILES.get('playerImage')
    if file:
        saved = default_storage.save(f'images/{Path(file.name).name}', file)
        image_path = f'/media/{saved}'
    dto = CreatePlayerDTO(
        jersey_number=int(request.POST.get('jerseyNumber', 0)),
        player_name=request.POST.get('playerName', ''),
        age=int(request.POST.get('age', 0)),
        role=request.POST.get('role', ''),
        nationality=request.POST.get('nationality', ''),
        team_code=request.POST.get('teamCode', ''),
        image_path=image_path,
    )
    ok, status = player_service.create_player(dto)
    return redirect('players:admin_list' if ok else f"{request.path_info.replace('add', 'add-page')}?status={status}")


@admin_login_required
def edit_page(request, jersey_number: int, team_code: str):
    player = player_service.get_player(jersey_number, team_code)
    teams = team_service.get_all_teams()
    if not player:
        return redirect('players:admin_list')
    return render(request, 'players/update.html', {'player': player, 'teams': teams, 'status': request.GET.get('status')})


@admin_login_required
def update_action(request):
    if request.method != 'POST':
        return redirect('players:admin_list')
    jersey = int(request.POST.get('jerseyNumber', 0))
    team_code = request.POST.get('teamCode', '')
    existing = player_service.get_player(jersey, team_code)
    if not existing:
        return redirect('players:admin_list')

    image_path = existing.image_path
    file = request.FILES.get('playerImage')
    if file:
        saved = default_storage.save(f'images/{Path(file.name).name}', file)
        image_path = f'/media/{saved}'

    dto = UpdatePlayerDTO(
        jersey_number=jersey,
        player_name=request.POST.get('playerName', ''),
        age=int(request.POST.get('age', 0)),
        role=request.POST.get('role', ''),
        nationality=request.POST.get('nationality', ''),
        team_code=team_code,
        image_path=image_path,
    )
    ok, _ = player_service.update_player(dto)
    return redirect('players:admin_list' if ok else 'players:admin_list?status=error')


@admin_login_required
def delete_action(request, jersey_number: int, team_code: str):
    if request.method != 'POST':
        return redirect('players:admin_list')
    player_service.delete_player(jersey_number, team_code)
    return redirect('players:admin_list')
