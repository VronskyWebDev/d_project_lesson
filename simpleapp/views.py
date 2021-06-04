
from django.views.generic import ListView  # импортируем класс, который
# говорит нам о том, что в этом представлении
# мы будем выводить список объектов из БД
from .models import Product


class ProductsList(ListView):
    model = Product  # указываем модель, объекты которой мы будем выводить
    template_name = 'products.html'
    context_object_name = 'products'



