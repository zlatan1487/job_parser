import os


class Path:
    """Класс миксин, хранит api kay для платформы SuperJob"""

    private_key: str = os.getenv('PRIVATE_KAY_SUPER_JOB')


