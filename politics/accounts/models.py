from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
# from django_countries.fields import CountryField


class UserManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, country, password=None, active=True, admin=False, staff=False):
        if not email:
            raise ValueError('User must have a valid email address!!!')

        if not username:
            raise ValueError('User must have a valid username!!!')
        
        if not password:
            raise ValueError('User must have a password!!!')

        if not first_name:
            raise ValueError('User must have a First Name!!!')

        if not last_name: 
            raise ValueError('User must have a Last Name!!!')

        if not country:
            raise ValueError('User must have a Country!!!')


        user_obj = self.model(
            email=self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
            country = country
            )

        user_obj.set_password(password)
        user_obj.admin = admin
        user_obj.staff = staff
        user_obj.active = active
        user_obj.save(using=self._db)
        return user_obj

    def create_staff(self, email, username, first_name, last_name, country, password=None):
        user = self.create_user(
            email,
            username = username,
            password = password,
            first_name = first_name,
            last_name = last_name,
            country = country,
            staff = True
        )
        return user

    def create_superuser(self, email, username, first_name, last_name, country, password=None):
        user = self.create_user(
            email,
            username = username,
            password = password,
            first_name = first_name,
            last_name = last_name,
            country = country,
            admin = True,
            staff = True
        )
        return user



class User (AbstractBaseUser):
    username = models.CharField(unique=True, max_length=100)
    email = models.EmailField(unique=True, max_length=255)
    first_name = models.CharField(max_length=250, blank=False)
    last_name = models.CharField(max_length=250, blank=False)
    country = models.CharField(max_length=150, blank=False)
    # country = CountryField()
    active = models.BooleanField(default=True) # all users that can login
    staff = models.BooleanField(default=False) #Users that can collaborate on others portfolio
    admin = models.BooleanField(default=False) #Super user with all priviledges
    created_at = models.DateTimeField(auto_now_add=True)


    USERNAME_FIELD =  'username'

    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name

    # def get_fullname(self):
    #     return

    def get_username(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_active(self):
        return self.active

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin


def usr_file_path(instance, filname):
    return 'users/avatars/{0}/{1}'.format(instance.user.id, filename)

class Profile(models.Model):
    genders = [
        ('MALE','Male'),
        ('FEMALE','Female'),
        ('OTHERS','Others'),
        ('PERFER NOT TO SAY','Prefer not to say')]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(null=True)
    gender = models.CharField(max_length=100, choices=genders, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    avatar = models.ImageField(upload_to=usr_file_path, default='user/avatar.jpg')
    

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name
    

# Signal to create a profile for a user at registration
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


