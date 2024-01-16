from django.contrib.auth.models import AbstractUser
class CustomUser(AbstractUser):
  pass
  def __str__(self):
      return self.username# ...INSTALLED_APPS = [    'projects.apps.ProjectsConfig',    'users.apps.UsersConfig',    'rest_framework',    'django.contrib.admin',
