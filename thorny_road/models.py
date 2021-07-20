from django.db import models

class Collateral(models.Model):
    name=models.CharField(max_length=128)
    address=models.CharField(max_length=1024)
    old_address=models.CharField(max_length=1024)
    private_area=models.FloatField(default=0.0)
    public_area=models.FloatField(default=0.0)
    households=models.IntegerField(default=0)
    targetholds=models.IntegerField(default=0)  
    completion_date=models.DateField()
    floor_area_ratio=models.FloatField(default=0.0)
    building_cover_ratio=models.FloatField(default=0.0)
    construction_company=models.CharField(max_length=128)
    floor=models.IntegerField(default=0)
    top_floor=models.IntegerField(default=0)

    def __str__(self):
        return self.name


# Create your models here.
class Asset(models.Model):
    owner=models.ForeignKey('auth.User', on_delete=models.CASCADE)
    collateral=models.ForeignKey('Collateral', on_delete=models.CASCADE)
    purchase_price=models.IntegerField()
    share_rate=models.FloatField()
    
    def __str__(self):
        return "{} {} {}%".format(self.owner, self.collateral, self.share_rate)

    def get_asset_balance(self):
        return self.purchase_price * self.share_rate / 100.0