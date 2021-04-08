

## User

Таблица пользователей

      class User(AbstractUser):
        phone = models.CharField("Телефон", max_length=15, blank=True, null=True)
    
        REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']
    
        def __str__(self):
            return "{}".format(self.username)

