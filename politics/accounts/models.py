from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# from django_countries.fields import CountryField


class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None, active=True, admin=False, staff=False):
        if not email:
            raise ValueError('User must have a valid email address!!!')
        user_obj = self.model(
            email=self.normalize_email(email),
            username = username
            )
        if not username:
            raise ValueError('User must have a valid username!!!')

        if not password:
            raise ValueError('User must have a password')

        user_obj.set_password(password)
        user_obj.admin = admin
        user_obj.staff = staff
        user_obj.active = active
        user_obj.save(using=self._db)
        return user_obj

    def create_staff(self, email, username, password=None):
        user = self.create_user(
            email,
            username = username,
            password = password,
            staff = True
        )
        return user

    def create_superuser(self, email, username, password=None):
        user = self.create_user(
            email,
            username = username,
            password = password,
            admin = True,
            staff = True
        )
        return user



class User (AbstractBaseUser):
    username = models.CharField(unique=True, max_length=100)
    email = models.EmailField(unique=True, max_length=255)
    active = models.BooleanField(default=True) # all users that can login
    staff = models.BooleanField(default=False) #Users that can collaborate on others portfolio
    admin = models.BooleanField(default=False) #Super user with all priviledges
    created_at = models.DateTimeField(auto_now_add=True)


    USERNAME_FIELD =  'username'

    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def __str__(self) -> str:
        return self.email

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


# class Profile(User):
#     genders = [
#         ('male','MALE'),
#         ('female','FEMALE'),
#         ('others', 'OTHERS'),
#         ('prefer not to say','PERFER NOT TO SAY'),]
    
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     first_name = models.CharField(max_length=250)
#     last_name = models.CharField(max_length=250)
#     dob = models.DateField()
#     gender = models.CharField(max_length=100, choices=genders)
    # country = CountryField()


    

