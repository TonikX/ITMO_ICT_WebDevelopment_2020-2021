from django.db import models


class OwnedModel(models.Model):
    owner = models.IntegerField(null=False, default=0)

    class Meta:
        abstract = True


class Book(OwnedModel):
    id = models.IntegerField(primary_key=True, auto_created=True)
    author = models.CharField(max_length=100, null=False)
    name = models.CharField(max_length=100)
    year_of_pub = models.DateField(auto_now_add=True)
    section = models.CharField(max_length=100, null=True)
    pressmark = models.CharField(max_length=100, null=True)
    debit_date = models.DateField(auto_now_add=True)


class InstanceOfBook(OwnedModel):
    id = models.IntegerField(primary_key=True)
    id_book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)
    status = models.BooleanField(default=False)


class Reader(OwnedModel):
    id = models.IntegerField(primary_key=True)
    full_name = models.CharField(max_length=100, null=False)
    passport_number = models.IntegerField()
    birthday = models.DateField(null=False)
    address = models.CharField(max_length=100, null=False)
    phone = models.IntegerField()
    TYPE_EX = (
        ('Middle', 'Middle'),
        ('High', 'High'),
        ('None', 'None'))
    degree = models.CharField(max_length=6, choices=TYPE_EX)
    graduate_degree = models.BooleanField(null=False)
    books = models.ManyToManyField(InstanceOfBook, through='IssuingAInstance')


class IssuingAInstance(OwnedModel):
    instance = models.ForeignKey(InstanceOfBook, on_delete=models.CASCADE, null=True)
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE, null=True)
    start_date = models.DateField(auto_now_add=True)
    return_date = models.DateField()


class ReadingRoom(OwnedModel):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, default='Room')
    size = models.IntegerField(default=0)


class InstanceOfBookInReadingRoom(OwnedModel):
    id_instance = models.ForeignKey(InstanceOfBook, on_delete=models.CASCADE, null=True)
    id_room = models.ForeignKey(ReadingRoom, on_delete=models.CASCADE, null=True)
    count = models.IntegerField(default=0)


class Registers(OwnedModel):
    id_reader = models.ForeignKey(Reader, on_delete=models.CASCADE, null=True)
    id_room = models.ForeignKey(ReadingRoom, on_delete=models.CASCADE, null=True)
    register_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now_add=True)
    unregister_date = models.DateField(auto_now_add=True)
