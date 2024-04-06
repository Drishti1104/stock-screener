from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=20, default="")
    email = models.EmailField(max_length=50, unique=True, default="")
    password = models.TextField(default="")
    is_member = models.BooleanField(default=False)

    def __str__(self):
        return self.email



class Query(models.Model):
    query = models.TextField(default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.email} - {self.query}"


class Stocks(models.Model):
    Company = models.CharField(max_length=100, default="")
    Ticker = models.CharField(max_length=20, default="")
    MarketCap = models.FloatField(default=0)
    PBRatio = models.FloatField(default=0)
    PERatio = models.FloatField(default=0)
    DividendYield = models.FloatField(default=0)
    EPS = models.FloatField(default=0)
    ROE = models.FloatField(default=0)
    IndustryPE = models.FloatField(default=0)
    FaceValue = models.FloatField(default=0)
    ReturnOnAssets = models.FloatField(default=0)
    OperatingProfitMargin = models.FloatField(default=0)
    NetProfitMargin = models.FloatField(default=0)
    EVToSales = models.FloatField(default=0)
    EVToEBITDA = models.FloatField(default=0)
    EarningsYield = models.FloatField(default=0)
    SectorPB = models.FloatField(default=0)
    SectorDividendYield = models.FloatField(default=0)
    SectorROE = models.FloatField(default=0)
    SectorROCE = models.FloatField(default=0)
    PriceToOCF = models.FloatField(default=0)
    PriceToFCF = models.FloatField(default=0)
    ROIC = models.FloatField(default=0)
    PEPremiumVsSector = models.FloatField(default=0)
    PBPremiumVsSector = models.FloatField(default=0)
    DividendYieldVsSector = models.FloatField(default=0)
    SectorPE = models.FloatField(default=0)
    PriceToSales = models.FloatField(default=0)
    PEGRatio = models.FloatField(default=0)

