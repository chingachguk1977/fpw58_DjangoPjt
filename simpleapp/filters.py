from django_filters import FilterSet, ModelChoiceFilter, ModelMultipleChoiceFilter
from .models import Product, Material, ProductMaterial, ProductCategory


# Создаем свой набор фильтров для модели Product.
# FilterSet, который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики.
class ProductFilter(FilterSet):
    material = ModelMultipleChoiceFilter(
        field_name='productmaterial__material',
        queryset=Material.objects.all(),
        label='Material',
        #empty_label='Любой',  # нужно, только если ModelChoiceFilter, а не ModelMultipleChoiceFilter
        conjoined=True,  # нужно, только если ModelMultipleChoiceFilter, а не ModelChoiceFilter
                           # также нужно, если множественный фильтр работал по AND, а не по OR
    )

    class Meta:
        # В Meta классе мы должны указать Django модель,
        # в которой будем фильтровать записи.
        model = Product
        # В fields мы описываем по каким полям модели
        # будет производиться фильтрация.
        fields = {
            # поиск по названию
            'name': ['icontains'],
            # количество товаров должно быть больше или равно
            'quantity': ['gt'],
            'price': [
                'lt',  # цена должна быть меньше или равна указанной
                'gt',  # цена должна быть больше или равна указанной
            ],
        }
