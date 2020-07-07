
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from . import models
from django_countries import countries


# Create your views here.


class Homeview(ListView):

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"


class RoomDetail(DetailView):

    model = models.Room


def search(request):
    city = request.GET.get("city", "Anywhere")
    city = str.capitalize(city)
    room_type = int(request.GET.get("room_type", 0))
   
    country = request.GET.get("country", "CA")
    price = int(request.GET.get("price", 0))
    guest = int(request.GET.get("guest", 0))
    beds = int(request.GET.get("beds", 0))
    bedrooms = int(request.GET.get("bedrooms", 0))
    bathrooms = int(request.GET.get("bathrooms", 0))

    s_amenities = request.GET.getlist("amenity")
    s_facilities = request.GET.getlist("facility")
    s_house_rules = request.GET.getlist("house_rule")

    s_instant_book = bool(request.GET.get("instant_book"))
    s_super_host = bool(request.GET.get("super_host"))

    form = {
        "city": city, 
        "s_country": country, 
        "s_room_type": room_type, 
        "price": price,
        "guest": guest,
        "beds": beds,
        "bedrooms": bedrooms,
        "bathrooms": bathrooms,
        "s_amenities": s_amenities,
        "s_facilities": s_facilities,
        "s_house_rules": s_house_rules,
        "instant_book": s_instant_book,
        "super_host": s_super_host
        }

    room_types = models.RoomType.objects.all()
    amenities = models.Amenity.objects.all()
    facilities = models.Facility.objects.all()
    house_rules = models.HouseRule.objects.all()

    choice = {
        "countries": countries,
        "room_types": room_types,
        "amenities": amenities,
        "facilities": facilities,
        "house_rules": house_rules}

    filter_args = {}

    if city != "Anywhere":
        filter_args["city__startswith"] = city
    
    filter_args["country"] = country

    if room_type != 0:
        filter_args["room_type__pk"] = room_type

    if price != 0:
        filter_args["price__lte"] = price

    if guest != 0:
        filter_args["guests__gte"] = guest

    if bedrooms != 0:
        filter_args["bedrooms__gte"] = bedrooms

    if beds != 0:
        filter_args["beds__gte"] = beds

    if bathrooms != 0:
        filter_args["baths__gte"] = bathrooms

    if s_instant_book is True:
        filter_args["instant_book"] = True

    if s_super_host is True:
        filter_args["host__superhost"] = True
    
    if len(s_amenities) > 0:
        for s_amenity in s_amenities:
            print(s_amenity)
            filter_args["amenities__pk"] = int(s_amenity)

    if len(s_facilities) > 0:
        for s_facility in s_facilities:
            print(s_facility)
            filter_args["facilities__pk"] = int(s_facility)

    rooms = models.Room.objects.filter(**filter_args)

    print(rooms)

    return render(request, "rooms/search.html", {**form, **choice, "rooms": rooms})
