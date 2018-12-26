from django.shortcuts import render
from restaurants.models import Restaurant
from django.http import JsonResponse


def restaurant_list(request):
    my_restaurants = []
    for restaurant in Restaurant.objects.all():
        my_restaurants.append({
            'name': restaurant.name
        })
    return JsonResponse(my_restaurants, safe=False)


def restaurant_detail(request, restaurant_id):
    restaurant_obj = Restaurant.objects.get(id=restaurant_id)
    my_restaurant = {
        'name': restaurant_obj.name,
        'description': restaurant_obj.description,
        'opening_time': restaurant_obj.opening_time,
        'closing_time': restaurant_obj.closing_time
    }
    return JsonResponse(my_restaurant)
