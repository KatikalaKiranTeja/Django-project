from pathlib import Path

from django.contrib import messages
from django.shortcuts import redirect, render

from apps.core.auth import admin_login_required
from apps.teams.dtos.team_dto import CreateTeamDTO, UpdateTeamDTO
from apps.teams.services.impl import TeamServiceImpl


service = TeamServiceImpl()


def public_list(request):
    teams = service.get_all_teams()
    return render(request, 'teams/public_list.html', {'teams': teams})


@admin_login_required
def admin_dashboard(request):
    teams = service.get_all_teams()
    status = request.GET.get('status')
    return render(request, 'teams/admin_dashboard.html', {'teams': teams, 'status': status})


@admin_login_required
def add_team_page(request):
    return render(request, 'teams/add.html', {'status': request.GET.get('status')})


@admin_login_required
def add_team_action(request):
    if request.method != 'POST':
        return redirect('teams:add_team_page')

    file = request.FILES.get('teamLogo')
    logo_path = ''
    if file:
        from django.core.files.storage import default_storage

        saved_name = default_storage.save(f'images/{Path(file.name).name}', file)
        logo_path = f'/media/{saved_name}'

    dto = CreateTeamDTO(
        team_code=request.POST.get('teamCode', '').strip(),
        team_name=request.POST.get('teamName', '').strip(),
        country=request.POST.get('country', 'India').strip(),
        coach_name=request.POST.get('coachName', '').strip(),
        captain_name=request.POST.get('captainName', '').strip(),
        logo_path=logo_path,
    )
    ok, status = service.create_team(dto)
    if ok:
        return redirect('teams:admin_dashboard')
    return redirect(f"{request.path_info.replace('add', 'add-page')}?status={status}")


@admin_login_required
def update_team_page(request, code: str):
    team = service.get_team(code)
    if not team:
        messages.error(request, 'Team not found')
        return redirect('teams:admin_dashboard')
    return render(request, 'teams/update.html', {'team': team, 'status': request.GET.get('status')})


@admin_login_required
def update_team_action(request):
    if request.method != 'POST':
        return redirect('teams:admin_dashboard')

    code = request.POST.get('teamCode', '').strip()
    existing = service.get_team(code)
    if not existing:
        return redirect('teams:admin_dashboard')

    logo_path = existing.logo_path
    file = request.FILES.get('teamLogo')
    if file:
        from django.core.files.storage import default_storage

        saved_name = default_storage.save(f'images/{Path(file.name).name}', file)
        logo_path = f'/media/{saved_name}'

    dto = UpdateTeamDTO(
        team_code=code,
        team_name=request.POST.get('teamName', '').strip(),
        country=request.POST.get('country', 'India').strip(),
        coach_name=request.POST.get('coachName', '').strip(),
        captain_name=request.POST.get('captainName', '').strip(),
        logo_path=logo_path,
    )
    ok, _ = service.update_team(dto)
    return redirect('teams:admin_dashboard' if ok else f"{request.path_info.replace('update', 'edit/' + code)}?status=error")


@admin_login_required
def delete_team_action(request, code: str):
    if request.method != 'POST':
        return redirect('teams:admin_dashboard')
    service.delete_team(code)
    return redirect('teams:admin_dashboard')
