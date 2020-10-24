from django.db import models

class Car(models.Model):
	COLORS = (
		('bk', 'black'),
		('w', 'white'),
		('s', 'silver'),
		('g', 'grey'),
		('r', 'red'),
		('y', 'yellow'),
		('gn', 'green'),
		('bl', 'blue'),
		('bn', 'brown'),
		('t', 'teal'),
		('p', 'pink'),
		('v', 'violet'),
		('o', 'orange'),
	)
	# imho it would be better with table brand...
	# еще тип бы добавить, чтобы проверять, позволяют ли права такое водить
	brand = models.CharField(max_length=30)
	model = models.CharField(max_length=60)
	color = models.CharField(max_length=2, choices=COLORS)
	number = models.CharField(max_length=6, unique=True)

class Owner(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	birthday = models.DateField()
	car = models.ManyToManyField(Car, through='Registration')

class License(models.Model):
	TYPES = (
		('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('M', 'M'),
		('A1', 'A1'), ('B1', 'B1'), ('C1', 'C1'), ('D1', 'D1'),
		('BE', 'BE'), ('CE', 'CE'), ('DE', 'DE'), ('C1E', 'C1E'), ('D1E', 'D1E'),
	)
	number = models.IntegerField(unique=True)
	date = models.DateField()
	type = models.CharField(max_length=3, choices=TYPES)
	owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

class Registration(models.Model):
	owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
	car = models.ForeignKey(Car, on_delete=models.CASCADE)
	start_date = models.DateField()
	end_date = models.DateField(blank=True, null=True) 