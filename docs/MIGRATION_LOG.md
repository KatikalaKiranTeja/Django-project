# Migration Log

## 2026-02-18
- Created master migration plan
- Scaffolded Django project and domain apps
- Added layered folders for controller/dto/repository/service
- Configured base URLs, settings, static/media
- Added DB engine switch (SQLite default, MySQL via env)
- Added placeholder app routes/controllers
- Implemented Teams module (entity/dto/repository/service/controller + templates)
- Implemented Players module (entity/dto/repository/service/controller + templates)
- Implemented Matches module (entity/dto/repository/service/controller + templates)
- Added admin session guard decorator
- Added login/logout controller and template
- Added JSP-like compatibility redirects for core routes
- Added static asset copy from Java project webapp
- Added dependencies for MySQL compatibility (PyMySQL + cryptography)
- Verified Django system check and route reversing
