from django.utils import timezone
from uuid import uuid4
import os


def path_and_rename(instance, filename):
    """Переименовать файл в ImageField модели User
    Изменить название и путь файла, если существует аналогичный
    с таким же названием.
    Args:
        instance (AbstractUser Model): Instance of User model
        filename (string): Название файла (картинки)

    Returns:
        os.path.join('avatar', filename)
    """
    # TODO: Delete previuous images
    upload_to = "lost"
    time = timezone.now().strftime("%d-%m-%y %H:%M:%S")
    ext = filename.split(".")[-1]
    if instance.pk:
        filename = f"lost_{instance.pk}_{time}.{ext}"
    else:
        filename = f"{uuid4().hex}.{ext}"
    return os.path.join(upload_to, filename)