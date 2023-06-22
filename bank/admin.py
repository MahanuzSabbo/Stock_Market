from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from .models import customer
from .models import StockAdmin
from django import forms
from django.contrib import messages
from django.http import HttpResponseRedirect
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'password')

admin.site.register(customer, CustomerAdmin)
class Stock(admin.ModelAdmin):
    list_display=['trade_code', 'high', 'low', 'open', 'close', 'volume','date']

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv)]
        return new_urls + urls

    def upload_csv(self,request):
        if request.method == "POST":
            csv_file = request.FILES["csv_upload"]

            if not csv_file.name.endwith('.csv'):
                messages.warning(request, 'uploaded')
                return HttpResponseRedirect(request.path_info)

            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.split("\n")

            for x in csv_data:
                fields = x.split(",")
                created = Employee.objects.Update_or_create(
                    trade_code= fields[0],
                    high=fields[1],
                    low=fields[2],
                    open=fields[3],
                    close=fields[4],
                    volume=fields[5],
                    date=fields[6]

               )
            url = reverse('admin:index')
            return HttpResponseRedirect(url)

        form = CsvImportForm()
        data ={"form": form}
        return render(request, "customer/csv_upload.html", data)
