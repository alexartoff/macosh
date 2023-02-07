from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


# Create your models here.
def expert_photo_path(instance, filename):
    return f'img/expert/{instance.username}/{filename}'


class Skill(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name=_('Skill title')
    )
    description = models.TextField(
        default='',
        verbose_name=_('Skill description')
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"


class Expert(AbstractUser):
    first_name = models.CharField(
        max_length=90,
        verbose_name=_('First name')
    )
    last_name = models.CharField(
        max_length=90,
        verbose_name=_('Last name')
    )
    about = models.TextField(
        default='something about...',
        verbose_name=_('Expert about')
    )
    username = models.CharField(
        max_length=200,
        unique=True,
        verbose_name=_('Username')
    )
    photo = models.ImageField(
        default='img/expert/default/expert-default.png',
        upload_to=expert_photo_path,
        verbose_name=_('Expert photo')
    )
    slug = models.SlugField(
        max_length=200,
        unique=True,
        verbose_name='Expert slug'
    )
    password = models.CharField(
        max_length=255,
        verbose_name=_('Password')
    )
    email = models.EmailField(
        blank=True,
        verbose_name=_("email")
    )
    created_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Added')
    )
    last_update = models.DateTimeField(
        auto_now=True,
        verbose_name=_('Last update')
    )
    last_login = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name=_('Last login')
    )
    is_staff = models.BooleanField(
        default=False,
        verbose_name=_('Staff')
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name=_('Active user')
    )
    skill = models.ManyToManyField(Skill)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = "Expert"
        verbose_name_plural = "Experts"

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    full_name.short_description = _('Full name')

    def show_skills(self):
        skills = self.skill.all()
        _ = ''
        for item in skills:
            _ += f'{item}; '
        return _[:-1]

    show_skills.short_description = _('Skills list')

    def save(self, *args, **kwargs):
        self.validate_unique()
        super(Expert, self).save(*args, **kwargs)
