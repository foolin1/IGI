from django.db import models
from django.core.validators import RegexValidator, EmailValidator, MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self, phone_number, email, password=None):
        if not phone_number:
            raise ValueError('Users must have a phone number')
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            phone_number=phone_number,
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, email, password):
        user = self.create_user(
            phone_number,
            email,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(
        max_length=13,
        unique=True,
        validators=[RegexValidator(regex=r'^\+37529\d{7}$', message="Phone number must be entered in the format: '+37529******'. Up to 9 digits allowed.")]
    )
    email = models.EmailField(
        max_length=50,
        unique=True,
        validators=[EmailValidator()]
    )
    is_client = models.BooleanField(default=True)
    balance = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  # Добавьте это поле, если хотите разрешить доступ в админ-панель

    objects = UserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.email


class Bill(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True, blank=False)
    last_time_payed = models.DateTimeField(blank=True, null=True, auto_now_add=False)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)

class Auto(models.Model):
    number = models.CharField(unique=True, blank=False, max_length=4, null=False)
    auto_model = models.CharField(max_length=50, blank=False)
    users = models.ManyToManyField(User)
    is_parked = models.BooleanField(blank=False, default=False)
    bill = models.OneToOneField(Bill, on_delete=models.CASCADE, blank=False, null=False)

class ParkingSpot(models.Model):
    number = models.PositiveIntegerField(unique=True,validators=[
            MinValueValidator(1),
            MaxValueValidator(999)
        ], blank=False, max_length=3, null=False, primary_key=True)
    price = models.DecimalField(max_digits=7, validators=[
            MinValueValidator(0.0)
        ], decimal_places=3)
    auto = models.OneToOneField(Auto, on_delete=models.SET_NULL, null=True, blank=True)
    is_available = models.BooleanField(default=True)

class AboutCompany(models.Model):
    info = models.CharField(blank=False, max_length=1000)

class NewsArticle(models.Model):
    name = models.CharField(blank=False, max_length=100)
    description = models.CharField(blank=False, max_length=1000)
    short_description = models.CharField(blank=True, max_length=100)

class Vacancy(models.Model):
    name = models.CharField(blank=False, max_length=50)
    description = models.CharField(blank=False, max_length=500)

class FAQ(models.Model):
    question = models.CharField(blank=False, max_length=300)
    answer = models.CharField(blank=False, max_length=1000)
    creation_time = models.DateTimeField(auto_now_add=True, blank=False)

class Contact(models.Model):
    name = models.CharField(blank=False, max_length=50)
    email = models.EmailField(
        max_length=50,
        unique=True,
        blank=False,
        validators=[EmailValidator()]
    )
    phone_number = models.CharField(
        max_length=13,
        unique=True,
        blank=False,
        validators=[
            RegexValidator(
                regex=r'^\+37529\d{7}$',
                message="Phone number must be entered in the format: '+37529******'. Up to 9 digits allowed."
            )
        ]
    )
    photo = models.CharField(blank=True, max_length=100)
    position = models.CharField(max_length=50, blank=False)

class Promocode(models.Model):
    name = models.CharField(blank=False, max_length=50, unique=True)
    expires_at = models.DateTimeField(blank=False)
    surcharge = models.DecimalField(blank=False, max_digits=10, decimal_places=2)

class Review(models.Model):
    rating = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ],
        blank=False
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    description = models.CharField(blank=False, max_length=500)

