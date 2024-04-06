from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class StocksField(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['Company','Ticker','MarketCap','PBRatio','PERatio','DividendYield','EPS','ROE','IndustryPE','FaceValue','ReturnOnAssets','OperatingProfitMargin','NetProfitMargin','EVToSales','EVToEBITDA','EarningsYield','SectorPB','SectorDividendYield','SectorROE','SectorROCE','PriceToOCF','PriceToFCF','ROIC','PEPremiumVsSector','PBPremiumVsSector','DividendYieldVsSector','SectorPE','PriceToSales','PEGRatio']

# ,'BookValue'
admin.site.register(Stocks, StocksField)
admin.site.register(Query)
admin.site.register(User)