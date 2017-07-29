from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from orders.forms import OrderForm
from .forms import CarsFilterForm
from .models import Car


def cars_list(request):
    cars = Car.objects.all()
    form = CarsFilterForm(request.GET)
    if form.is_valid():
        if form.cleaned_data["min_price"]:
            cars = cars.filter(price__gte=form.cleaned_data["min_price"])
        if form.cleaned_data["max_price"]:
            cars = cars.filter(price__lte=form.cleaned_data["max_price"])
        if form.cleaned_data["ordering"]:
            cars = cars.order_by(form.cleaned_data["ordering"])

    return render(request, "cars/cars_list.html", {"cars": cars, "form": form})


def cars_detail(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    form = OrderForm(request.POST or None, initial={
        "car": car
    })
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("{}?sended=True".format(reverse("car", kwargs={"car_id": car.id})))

    return render(request, "cars/cars_detail.html", {
        "car": car,
        "form": form,
        "sended": request.GET.get("sended", False)
    })
