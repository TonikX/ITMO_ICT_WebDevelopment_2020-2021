from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from .models import Car, Owner, License, Registration


def home(request):
    res = '<h1>Добро пожаловать!\nВы можете выбрать категорию:</h1>'
    res += f'<div><a href=\'owner\'>Владельцы автомобилей</a></div>'
    res += f'<div><a href=\'car\'>Автомобили</a></div>'
    return HttpResponse(res)


def owner(request):
    owners = Owner.objects.all()
    res = '<h1>Список владельцев автомобилей</h1>'
    for owner in owners:
        res += f'<div><a href={owner.id}>{owner.first_name} {owner.last_name}</a></div>'
    return HttpResponse(res)


def car(request):
    cars = Car.objects.all()
    res = '<h1>Список автомобилей</h1>'
    for car in cars:
        res += f'<div>{car.brand} {car.model}</div>'
    return HttpResponse(res)


def detail(request, owner_id):
    try:
        owner = Owner.objects.get(pk=owner_id)
        licenses = License.objects.all().filter(owner=owner)
        registrations = Registration.objects.all().filter(owner=owner)
        cars = []
        for reg in registrations:
            cars.append(
                {'car': reg.car, 'start_date': reg.start_date, 'end_date': reg.end_date})
    except Owner.DoesNotExist:
        raise Http404(
            'Такого владельца в базе данных нет.\nПопробуйте вернуться к списку владельцев и выбрать кого-то, кто существует\n')

    return render(request, 'owner/detail.html', {
        'owner': owner, 'licenses': licenses, 'cars': cars})
