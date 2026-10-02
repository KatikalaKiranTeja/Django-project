import os


class AdminAuthService:
    def validate_credentials(self, username: str, password: str) -> bool:
        expected_user = os.getenv('ADMIN_USERNAME', 'admin')
        expected_pass = os.getenv('ADMIN_PASSWORD', 'admin123')
        return username == expected_user and password == expected_pass
