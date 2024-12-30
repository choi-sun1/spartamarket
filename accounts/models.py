from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


def user_profile_image_path(instance, filename):
    return f'profile_images/{instance.id}/{filename}'


class User(AbstractUser):
    profile_image = models.ImageField(upload_to=user_profile_image_path, blank=True, null=True)

    # 팔로우
    follows = models.ManyToManyField('self', symmetrical=False, related_name='followers', blank=True)

    # groups와 user_permissions의 related_name 설정
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_groups',
        blank=True,
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions',
        blank=True,
        verbose_name='user permissions'
    )

    @property
    def follower_count(self):
        return self.followers.count()

    @property
    def following_count(self):
        return self.follows.count()

    def __str__(self):
        return self.username
