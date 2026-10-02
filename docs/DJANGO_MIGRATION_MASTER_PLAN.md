# IPL Java -> Django Migration Master Plan

## 1. Objective
Build a complete Django version of the existing Java Servlet/JSP IPL project while preserving:
- same visual frontend style (HTML/CSS/JS)
- same user/admin workflows and CRUD behavior
- same MySQL database
- fully layered backend structure similar to Java:
  - controller
  - dto
  - entities/models
  - repository + repository implementation
  - service + service implementation

This document is the execution checklist and backup control sheet.

---

## 2. Source Project Baseline
Source location:
- `IplManagement/IPlManagement`

Current backend modules:
- Admin login
- Teams CRUD
- Players CRUD
- Matches CRUD + filters

Current frontend pages:
- `main.jsp`, `adlogin.jsp`
- Admin pages: `admindash.jsp`, `adminPlayers.jsp`, `adminMatches.jsp`
- Public pages: `teams.jsp`, `players.jsp`, `Matches.jsp`
- Forms: add/update pages for team/player/match

Known issues to fix during migration:
- `playerOfMatch` input not saved to DB
- completed match update can null important fields
- weak auth protection and hardcoded secrets
- deletes via GET
- status value casing inconsistency

---

## 3. Target Django Architecture
Target root:
- `IplManagementPython/`

Target package layout:
- `config/` (settings, urls, asgi, wsgi)
- `apps/`
  - `core/` (exceptions, shared helpers)
  - `admin_auth/`
  - `teams/`
  - `players/`
  - `matches/`
- each domain app:
  - `controllers/`
  - `dtos/`
  - `repositories/interfaces.py`
  - `repositories/impl.py`
  - `services/interfaces.py`
  - `services/impl.py`
  - `models.py`
  - `urls.py`
  - `templates/<module>/...`
- global templates/static/media folders

---

## 4. Migration Strategy (Phase-by-Phase)

### Phase 0: Safety + Baseline Freeze
Checklist:
- [ ] capture Java route and action map
- [ ] capture DB schema and current records backup
- [ ] freeze static assets list
- [ ] create risk list and acceptance criteria

Backup steps:
- [ ] DB dump before first Django write
- [ ] copy JSP/CSS/JS and image assets snapshot
- [ ] create migration log file (`docs/MIGRATION_LOG.md`)

Exit criteria:
- [ ] baseline documented and reproducible

### Phase 1: Django Foundation
Checklist:
- [ ] create virtual environment and dependency list
- [ ] initialize Django project (`config`)
- [ ] create apps (`core`, `admin_auth`, `teams`, `players`, `matches`)
- [ ] configure MySQL via environment variables
- [ ] configure static/media
- [ ] setup app-level URL includes

Exit criteria:
- [ ] `python manage.py runserver` works
- [ ] health endpoint responds

### Phase 2: Data Layer + Model Alignment
Checklist:
- [ ] align models to existing MySQL tables (`teams`, `players`, `matches`)
- [ ] enforce unique/foreign key constraints equivalent to Java logic
- [ ] prepare optional custom user/admin auth model strategy

Exit criteria:
- [ ] ORM read/write validated against same DB

### Phase 3: Teams Module End-to-End
Checklist:
- [ ] DTOs implemented
- [ ] repository interface + impl implemented
- [ ] service interface + impl implemented
- [ ] controllers/views implemented
- [ ] add/update/delete/list routes implemented
- [ ] templates converted from `addTeam.jsp`, `updateTeam.jsp`, `admindash.jsp`, `teams.jsp`
- [ ] file upload for team logo implemented
- [ ] duplicate code handling preserved

Exit criteria:
- [ ] admin/public team flows pass verification checklist

### Phase 4: Players Module End-to-End
Checklist:
- [ ] layered backend complete
- [ ] templates converted from `addPlayer.jsp`, `updatePlayer.jsp`, `adminPlayers.jsp`, `players.jsp`
- [ ] jersey uniqueness per team enforced
- [ ] image upload implemented

Exit criteria:
- [ ] admin/public player flows pass verification checklist

### Phase 5: Matches Module End-to-End
Checklist:
- [ ] layered backend complete
- [ ] templates converted from `addMatch.jsp`, `updateMatch.jsp`, `adminMatches.jsp`, `Matches.jsp`
- [ ] status filtering preserved
- [ ] winner/scores/player-of-match fully persisted
- [ ] completed-update data loss bug fixed

Exit criteria:
- [ ] admin/public match flows pass verification checklist

### Phase 6: Auth + Security Hardening
Checklist:
- [ ] replace hardcoded credentials with Django auth/env settings
- [ ] protect all admin routes with login checks
- [ ] logout clears session
- [ ] deletes changed to POST with CSRF
- [ ] input validation + service-level guardrails

Exit criteria:
- [ ] unauthorized access blocked for admin endpoints

### Phase 7: Frontend Parity + Route Compatibility
Checklist:
- [ ] visual parity check page-by-page
- [ ] JS interactions preserved (search/filter/toggle)
- [ ] legacy route mapping or redirects documented
- [ ] static/media paths verified

Exit criteria:
- [ ] UI and UX match original behavior

### Phase 8: Testing + Final Verification
Checklist:
- [ ] manual test matrix execution
- [ ] unit tests for services/repositories
- [ ] integration tests for critical flows
- [ ] regression pass report generated

Exit criteria:
- [ ] production-ready checklist all green

---

## 5. Page-to-Page Mapping (JSP -> Django Template)
- `main.jsp` -> `templates/public/main.html`
- `adlogin.jsp` -> `templates/admin_auth/login.html`
- `admindash.jsp` -> `templates/teams/admin_dashboard.html`
- `teams.jsp` -> `templates/teams/public_list.html`
- `addTeam.jsp` -> `templates/teams/add.html`
- `updateTeam.jsp` -> `templates/teams/update.html`
- `adminPlayers.jsp` -> `templates/players/admin_list.html`
- `players.jsp` -> `templates/players/public_list.html`
- `addPlayer.jsp` -> `templates/players/add.html`
- `updatePlayer.jsp` -> `templates/players/update.html`
- `adminMatches.jsp` -> `templates/matches/admin_list.html`
- `Matches.jsp` -> `templates/matches/public_list.html`
- `addMatch.jsp` -> `templates/matches/add.html`
- `updateMatch.jsp` -> `templates/matches/update.html`

---

## 6. Functional Verification Matrix (Must Pass)

### Auth
- [ ] admin can login
- [ ] invalid credentials show error
- [ ] protected pages require login
- [ ] logout works

### Teams
- [ ] add team with logo
- [ ] duplicate team code blocked
- [ ] update team with/without new logo
- [ ] delete team
- [ ] team search filter works
- [ ] public team page renders all teams

### Players
- [ ] add player with image
- [ ] duplicate jersey within same team blocked
- [ ] update player with/without new image
- [ ] delete player
- [ ] search filter works
- [ ] public player page renders all players

### Matches
- [ ] add upcoming/completed match
- [ ] update match fields correctly
- [ ] completed match update does not erase core data
- [ ] player of match persists and displays
- [ ] delete match
- [ ] admin/public filters (All/Upcoming/Completed) work

### Static & media
- [ ] all styles/icons/images load
- [ ] uploaded images render in admin/public pages

---

## 7. Rollback Plan
If any phase breaks critical flows:
- [ ] stop new phase work
- [ ] restore from last git checkpoint
- [ ] restore DB from latest dump (if schema/data modified)
- [ ] reopen unresolved checklist items

---

## 8. Definition of Done
Project is considered complete only if:
- [ ] all pages migrated from JSP to Django templates
- [ ] all backend logic migrated to layered Django modules
- [ ] all critical bugs fixed and verified
- [ ] admin/public flows pass full matrix
- [ ] codebase documented and runnable end-to-end

---

## 9. Execution Log (to update during implementation)
- [ ] Phase 0 started
- [ ] Phase 1 started
- [ ] Phase 2 started
- [ ] Phase 3 started
- [ ] Phase 4 started
- [ ] Phase 5 started
- [ ] Phase 6 started
- [ ] Phase 7 started
- [ ] Phase 8 started
