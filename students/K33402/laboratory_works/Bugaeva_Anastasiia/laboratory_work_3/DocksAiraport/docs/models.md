## User

Таблица пользователей

    class User(AbstractUser):
        phone = models.CharField("Телефон", max_length=15, blank=True, null=True)
    
        REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']

## Авиакомпания

Таблица авиакомпаний

    class Airline(models.Model):
        name = models.CharField(max_length=30)

## Город и Аэропорт   

Таблица городов и их аэропортов

    class CityAirport(models.Model):
        cityName = models.CharField(max_length=30)
        airportName = models.CharField(max_length=30)
 
## Рейс
    class Flight(models.Model):
        company = models.ForeignKey(Airline, on_delete=models.CASCADE)
        num_flight = models.IntegerField()
        numberOfPackages = models.IntegerField()
        departure = models.ForeignKey(CityAirport, verbose_name='Город, аэропорт', related_name="departure", on_delete=models.CASCADE)
        arrival = models.ForeignKey(CityAirport, verbose_name='Город, аэропорт', related_name="Arrival", on_delete=models.CASCADE)
        departure_date = models.DateTimeField(null=True)
        arrival_date = models.DateTimeField(null=True)

## Место в самолете
Место в самолете (связь "один ко многим" с сущностью Flight)

    class Place(models.Model):
        num_flight = models.ForeignKey(Flight, on_delete=models.CASCADE, verbose_name='Рейс', blank=True, related_name='numberFlight')
        passenger = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пассажир', blank=True, null=True)

## Комментарии
Комментарии к рейсам

    class Comments(models.Model):
        flight = models.ForeignKey(Flight, on_delete=models.CASCADE, verbose_name='Рейс', blank=True, null=True, related_name='Flight')
        author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец комментария', blank=True, null=True)
        create_date = models.DateTimeField(auto_now=True)
        rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
        text = models.TextField(verbose_name='Текст комментария')
        status = models.BooleanField(verbose_name='Видимость комментария', default=True)
