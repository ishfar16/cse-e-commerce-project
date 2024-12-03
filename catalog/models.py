from django.db import models
class Item(models.Model):
    title = models.CharField(max_length= 200)
    price = models.IntegerField()
    discount_price = models.IntegerField()
    slug = models.SlugField()
    def __dtr__(self):
        return self.user.title

class OrderItem(models.Model):
    user = models.ForeignKey(user, on_delte=models.CASCADE)
    item = models.ForeignKey(Item, on_delete = models.CASCADE)
    Ordered = models.BooleanField(default = False)
    quantity = models.IntegerField(default = 1)

    def __dtr__(self):
        return f"{self.quantity} of {self.item.title}"

class Order(models.Model):
    user = models.ForeignKey(user,on_delete=models.CASCADE)
    items=models.ManyToManyField(OrderItem)
    Ordered = models.BooleanField(default = False)
    start_date = models.DateTimeField(aut_now_add = True)
    ordered_date = models.DateTimeField()


    def __dtr__(self):
        return self.user.username