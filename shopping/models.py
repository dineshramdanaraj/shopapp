import uuid
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import EmailValidator, MaxValueValidator, MaxLengthValidator
from django.db.models import Sum, Count  
from django.utils import timezone

# Create your models here.
class Base(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    create_date = models.DateField(auto_now_add= True)
    update_date = models.DateField(auto_now_add= True)
    class Meta:
        abstract = True

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField()
    email = models.EmailField(validators=[EmailValidator])
    ph_no = models.CharField(max_length= 10, null = True)
    is_verified = models.BooleanField(default= False)


class item_category(Base):
    type_Name = models.CharField(max_length= 100)
    def __str__(self):
        return self.type_Name

class item(Base):
    type = models.ForeignKey(item_category, on_delete= models.CASCADE, related_name= 'category')
    item_name = models.CharField(max_length= 1000, unique=  True)
    price = models.IntegerField(default= 0)
    image = models.ImageField(upload_to='item')
    ratings = models.OneToOneField('rating', on_delete=models.SET_NULL, null=True, blank=True)

class cart(Base):
    user = models.ForeignKey(User, null = True, on_delete= models.SET_NULL, related_name='cart')
    is_paid = models.BooleanField(default = False)
    instamojo_id = models.CharField(max_length=1000, null= True)

    def cart_total(self, k):
        i = int(k)
        return i
        


class cart_item(Base):
    cart = models.ForeignKey(cart, on_delete = models.CASCADE, related_name = 'cart_items')
    item = models.ForeignKey(item, on_delete= models.CASCADE)
    quantity = models.IntegerField(default=0)
    
    @property
    def item_total(self):
        return self.quantity * self.item.price

class rating(Base):
    item_to_rate = models.ForeignKey(item, on_delete=models.CASCADE)
    rate = models.IntegerField(validators= [MaxValueValidator(5)], null = True, default= 0)
    count = models.IntegerField(default= 0)
    user = models.ForeignKey(User, null = True, on_delete= models.SET_NULL)

class order(Base):
    cart = models.ForeignKey(cart, on_delete= models.CASCADE)
    user = models.ForeignKey(User, null = True, on_delete= models.SET_NULL)

class reviews(Base):
    item_to_review = models.ForeignKey(item, on_delete= models.CASCADE)
    user = models.ForeignKey(User, null = True, on_delete= models.SET_NULL)
    comment = models.TextField(null = True)

discount_choices = (("%", "percentage"), ("Rs", "amount"), ("N", "none") )  

class coupon(Base):
     
    Code = models.CharField(max_length= 10, unique=True)
    discount = models.IntegerField()
    type = models.CharField(max_length= 2, choices= discount_choices, default = 'N')
    valid_until = models.DateTimeField()






