from datetime import datetime

from django.views.generic import ListView  # импортируем класс, который
# говорит нам о том, что в этом представлении
# мы будем выводить список объектов из БД
from django.views.generic import DetailView
from .models import Product


class ProductsList(ListView):
    model = Product  # указываем модель, объекты которой мы будем выводить
    template_name = 'products.html'
    context_object_name = 'products'
    queryset = Product.objects.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['value1'] = None
        return context


class ProductDetail(DetailView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product'


