from django.db import models

# Create your models here.

class detail(models.Model):
    name=models.CharField(max_length=20)

#storing person details
class Person(models.Model):
    sex=(
    ('M','MALE'),
    ('F','FEMALE')
    )
    user_name=models.CharField(max_length=20, unique=True)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    sex=models.CharField(max_length=1,choices=sex)
    address=models.TextField()
    email_id=models.EmailField(max_length=100)
    phone_no=models.CharField(max_length=30)
    secondary_phone_no=models.CharField(max_length=30)
    #photos=models.ImageField(upload_to=None,height_field=None,width_field=None,max_length=300)
    password=models.CharField(max_length=20)
    def __str__(self):
        return self.user_name

class PersonCard(Person):
    card_no=models.CharField(max_length=20)


    #storing cloth details
class Cloth(models.Model):
    st=(
    ('N','NYLON'),
    ('S','SILK'),
    ('R','RYAN'),
    ('K','KHADI'),
    ('O','OTHERS')
    )
    cat=(
    ('S','SHIRT'),
    ('P','PAINT'),
    ('SA','SAREE'),
    ('SU','SUIT'),
    ('J','JEANS'),
    ('I','INNERWEAR'),
    ('B','BEDSHEET'),
    ('O','OTHERS'),
    )
    cloth_type=models.CharField(max_length=50)
    catagory=models.CharField(max_length=1,choices=cat)
    color=models.CharField(max_length=20)
    brand=models.CharField(max_length=50)
    #sizeofcloth=models.CharField(max_length=1,choices=size)
    material=models.CharField(max_length=1,choices=st)
    status=models.CharField(max_length=50)
    cost=models.DecimalField(max_digits=19,decimal_places=4)
    person=models.ForeignKey('Person')
    def __str__(self):
        return self.cloth_type

#request status
class OrderRequest(models.Model):
    state=(
    ('R','RECEIVE'),
    ('P','PROCESSING'),
    ('D','DELIVERED')
    )
    person=models.ForeignKey('Person')
    status=models.CharField(max_length=1,choices=state)
    Checkin=models.DateTimeField(auto_now=False,auto_now_add=False)
    #cost=models.DecimalField(max_digits=19,decimalplaces=4)

#response for cloths
class OrderResponse(models.Model):
    orderrequest=models.ForeignKey('OrderRequest')
    cloth=models.ForeignKey('Cloth')
    Checkout=models.DateTimeField(auto_now=False,auto_now_add=False)

class History(models.Model):
    cloth=models.ManyToManyField(Cloth)
    person=models.ForeignKey('Person')
    hist=models.Manager()
    class meta:
        order_with_respect_to='cloth'
