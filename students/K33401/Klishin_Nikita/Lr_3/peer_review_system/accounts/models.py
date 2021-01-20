# from main.models import StudentProfile, TeacherProfile
from django.db import models
from django.db.models import signals
from django.contrib.auth import get_user_model
from django.contrib.auth.models import (
	BaseUserManager, 
	AbstractBaseUser
)
import datetime


class MyUserManager(BaseUserManager):
	def create_user(self, email, password=None, is_teacher=False):
		"""
		Создание и сохранение пользователя
		 """
		if not email:
			raise ValueError('Users must have an email address')

		user = self.model(
			email=self.normalize_email(email),
		)

		user.set_password(password)
		user.save(using=self._db)

		# если новый пользователь - преподаватель
		if is_teacher:
			TeacherProfile.objects.create(user=user)
		else:
			StudentProfile.objects.create(user=user)

		return user
		
	def create_superuser(self, email, password=None, is_teacher=False):
		"""
		Creates and saves a superuser with the given email, date of
        birth and password.
        """
		user = self.create_user(
			email,
			password=password,
		)
		user.admin = True
		user.save(using=self._db)
		return user


class CustomUser(AbstractBaseUser):
	email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
	active = models.BooleanField(default=True)
	admin = models.BooleanField(default=False)
	# is_staff = models.BooleanField(default=False)
	
	name = models.CharField(max_length=120, default="Имя", verbose_name="Person name")
	surname = models.CharField(max_length=120, default="Фамилия", verbose_name="Person surname")
	birth_date = models.DateField(default=datetime.date.today)
	is_teacher=models.BooleanField(default=False)


	objects = MyUserManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['is_teacher']


	def __str__(self):
		return self.email + ' ' + self.name + ' ' + self.surname

	def has_perm(self, perm, obj=None):
		"Does the user have a specific permission?"
		# Simplest possible answer: Yes, always
		return True

	def has_module_perms(self, app_label):
		"Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
		return True

	@property
	def is_staff(self):
		"Is the user a member of staff?"
		return self.admin
	
	@property
	def is_admin(self):
		"Is the user a admin member?"
		return self.admin
	
	@property
	def is_active(self):
		"Is the user active?"
		return self.active


class TeacherProfile(models.Model):
	user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name='teacher_profile')


class StudentProfile(models.Model):
	user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='student_profile')
	student_class = models.ForeignKey('main.StudentsClass', on_delete=models.CASCADE, related_name='student_class', blank=True, null=True)

	def __str__(self) -> str:
		return "Student profie: " + self.user.email



