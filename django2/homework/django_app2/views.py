from django.shortcuts import render, HttpResponse

from django_app2.models import Film


def home(request):
    return HttpResponse("<h1>Welcome to my first website</h1>")


def find_movie(request):
    find = Film.objects.filter(rate=5)
    response = ""
    for i in find:
        response += str(i) + "<br>"

    return HttpResponse(response)


def create_film(request):
    film_name = "Schindler's List"
    film_rate = 5
    created_in = 1993
    bol = True
    film_status = 2

    film_name2 = "Fight Club"
    film_rate2 = 5
    created_in2 = 1999
    bol2 = True
    film_status2 = 2

    film_name3 = "Ameli"
    film_rate3 = 5
    created_in3 = 2001
    bol3 = True
    film_status3 = 2

    film_name4 = "Mister Nobody"
    film_rate4 = 5
    created_in4 = 2009
    bol4 = True
    film_status4 = 1

    film = Film.objects.create(name=film_name, rate=film_rate, created_at=created_in, is_published=bol, status=film_status)
    film2 = Film.objects.create(name=film_name2, rate=film_rate2, created_at=created_in2, is_published=bol2, status=film_status2)
    film3 = Film.objects.create(name=film_name3, rate=film_rate3, created_at=created_in3, is_published=bol3, status=film_status3)
    film4 = Film.objects.create(name=film_name4, rate=film_rate4, created_at=created_in4, is_published=bol4, status=film_status4)

    return HttpResponse("Success{} {} {} {}".format(film, film2, film3, film4))


def delete_film(request):
    find_2 = Film.objects.get(name="Ameli")
    find_2.delete()

    return HttpResponse("Deleted {}".format(find_2))



