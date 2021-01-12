

## User

Таблица пользователей

    class User(AbstractUser):
        username = models.CharField(max_length=20, blank=True, null=True, unique=True)
        passport = models.CharField(max_length=100, blank=True, null=True)
        salary = models.IntegerField(default=0)
        REQUIRED_FIELDS = ['first_name', 'last_name', 'passport']
    
        def __str__(self):
            return self.username




## Авиакомпания

Таблица Авиакомпания, у нее есть борт проводники, рейсы и аэропорты

    class Airline(models.Model):  # Авиакомпания
        owner = models.ForeignKey(User, on_delete=models.CASCADE)
        id = models.AutoField(primary_key=True)
        name = models.CharField(max_length=30)
    
        def __str__(self):
            return self.name


## Город    

Таблицы городов

    class City(models.Model):
        name = models.CharField(max_length=40, primary_key=True)
    
        def __str__(self):
            return self.name
    
## Аэропорт
  
Таблица аэропортов, связи 1 ко многим с таблцией "Авиакомпания"

    class Airport(models.Model): 
        class Meta:
            unique_together = (('company', 'city', 'airaport'),)
    
        company = models.ForeignKey(Airline, on_delete=models.CASCADE, verbose_name="Компания")
        city = models.ForeignKey(City, on_delete=models.CASCADE)
        airaport = models.CharField(max_length=30, verbose_name="Аэропорт")
    
        def __str__(self):
            return "Компания: {}, Город: {}, Аэропорт: {}".format(self.company, self.city, self.airaport)
    
## Прилет
    class Arrival(models.Model):
        id = models.AutoField(primary_key=True)
        arrival = models.ForeignKey(Airport, on_delete=models.CASCADE, verbose_name="Прилет")  # куда летим
    
        def __str__(self):
            return "{}".format(self.arrival)
    
## Отлет
    class Departure(models.Model):  
        id = models.AutoField(primary_key=True)
        departure = models.ForeignKey(Airport, on_delete=models.CASCADE, verbose_name="отлет")  # откуда летим
    
        def __str__(self):
            return "{}".format(self.departure)
    
## Путь
    class Route(models.Model):  # Путь
        id = models.AutoField(primary_key=True)
        departure = models.ForeignKey(Departure, on_delete=models.CASCADE, related_name="отлет")  # откуда летим
        arrival = models.ForeignKey(Arrival, on_delete=models.CASCADE, related_name="Прилет")  # куда летим
        dateDeparture = models.DateTimeField()
        dateArrival = models.DateTimeField()
        distance = models.PositiveIntegerField()  # Расстояние в метрах
    

    
## Рейс
    class Flight(models.Model):  
        id = models.TextField(primary_key=True)
        airline = models.ForeignKey(Airline, on_delete=models.CASCADE)
        Transit = models.BooleanField()
        courses = models.ManyToManyField(Route)
        def __str__(self):
            return "{} {}".format(self.airline, self.id)
    
## Самолет
    class Plane(models.Model):  # Самолет
        id = models.AutoField(primary_key=True)
        flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
        countPlace = models.PositiveSmallIntegerField()
        def __str__(self):
            return "id: {}; Компания: {}; Мест: {}".format(self.id, self.flight, self.countPlace)
    
## Борт
    class Board(models.Model):  # Борт
        id = models.AutoField(primary_key=True)
        flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    
## Борт проводник
    class FlightAttendant(models.Model):  # Борт проводник
        user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="attendant")
        education = (
            ('I', 'ITMO'),
            ('S', 'SPBGU'),
            ('D', 'DVFU'),
        )
        Education = models.CharField(max_length=1, choices=education, verbose_name='Об')
        Experience = models.PositiveSmallIntegerField()
        board = models.ManyToManyField(Board)
    
        def __str__(self):
            return "{} {}".format(self.user, self.Education)    

## Пилот
    class Pilot(models.Model):  # Пилот
        education_type = [
            ('1', 'Pilot'),
            ('2', 'SecondPilot'),
            ('3', 'Navigator'),
        ]
        education = models.CharField(
            max_length=1,
            choices=education_type,
            verbose_name="должность"
        )
        # passport = models.CharField(max_length=10, primary_key=True)
        # FIO = models.CharField(max_length=100)
        user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="pilot")
        Experience = models.PositiveSmallIntegerField()
        board = models.ManyToManyField(Board)
    
        def __str__(self):
            return "{} {}".format(self.user, self.education)
