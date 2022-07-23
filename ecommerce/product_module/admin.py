from django.contrib import admin
from .models import Brand, Category, Product, CartItem

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ["image_tag", "name", "price", "brand", "category", "quantity"]
    search_fields = ["name", "price", "brand__name", "category__name",]
    list_filter = ["brand","category",]

    class Meta:
        model = Product

class BrandAdmin(admin.ModelAdmin):
    list_display = ["name", "is_active"]
    search_fields = ["name"]
    class Meta:
        model = Brand


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "is_active", "icon_code"]
    search_fields = ["name"]
    class Meta:
        model = Category

admin.site.register(Product, ProductAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(CartItem)