from django.db import models

# Create your models here.
class Customer(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    email = models.EmailField()
    mobile = models.CharField(max_length=12, default=90)
    address = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.username}, {self.password}"
    
class Restaurants(models.Model):
    Res_name = models.CharField(max_length=100)
    Food_cat = models.CharField(max_length=200)
    rating = models.FloatField()
    img = models.URLField(default="https://elledecor.in/wp-content/uploads/2023/12/H1_Swwing.jpg")
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.Res_name
    
class Menu(models.Model):
    res = models.ForeignKey(
        Restaurants,
        on_delete=models.CASCADE
    )
    item_name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    img = models.URLField(default="https://d3sftlgbtusmnv.cloudfront.net/blog/wp-content/uploads/2025/01/Best-Food-In-Ooty-Cover-Photo-840x425.jpg")
    is_available = models.BooleanField(default=True)
    category = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.item_name} - {self.res.Res_name}"

class Cart(models.Model):
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE
    )
    items = models.ManyToManyField("Menu")

    def total_price(self):
        return sum(item.price for item in self.items.all())
    
    def __str__(self):
        return f"{self.customer.username} {self.total_price()}"
