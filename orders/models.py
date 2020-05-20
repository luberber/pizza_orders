from django.db import models

# Create your models here.
class RegularPizza(models.Model):
    type = models.CharField(max_length=64)
    small_prize = models.FloatField()
    large_prize = models.FloatField()

    def __str__(self):
        #return f"{self.type} {self.small_prize} {self.large_prize}"
        return "{} {} {}".format(self.type, self.small_prize, self.large_prize)

class SicilianPizza(models.Model):
    type = models.CharField(max_length=64)
    small_prize = models.FloatField()
    large_prize = models.FloatField()

    def __str__(self):
        return "{} {} {}".format(self.type, self.small_prize, self.large_prize)

class Topping(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return "{}".format(self.name)

class Sub(models.Model):
    name = models.CharField(max_length=64)
    small_prize = models.FloatField(blank=True)
    large_prize = models.FloatField()
    #toppings = models.ManyToManyField(Topping, blank=True, related_name="subs")

    def __str__(self):
        return "{} {} {}".format(self.name, self.small_prize, self.large_prize)

class Add(models.Model):
    sub = models.ForeignKey(Sub, on_delete=models.CASCADE, related_name="sub")
    topping = models.ForeignKey(Topping, on_delete=models.CASCADE, related_name="toppping")
    prize = models.FloatField()

    def __str__(self):
        return "{} {} {}".format(self.sub, self.topping, self.prize)

class Pasta(models.Model):
    name = models.CharField(max_length=64)
    prize = models.FloatField()

    def __str__(self):
        return "{} {}".format(self.name, self.prize)

class Salad(models.Model):
    name = models.CharField(max_length=64)
    prize = models.FloatField()

    def __str__(self):
        return "{} {}".format(self.name, self.prize)

class DinnerPlatter(models.Model):
    name = models.CharField(max_length=64)
    small_prize = models.FloatField()
    large_prize = models.FloatField()

    def __str__(self):
        return "{} {} {}".format(self.name, self.small_prize, self.large_prize)
