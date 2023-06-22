from django.shortcuts import render
#from django.shortcuts import render
# import json
# from .models import FilesUpload



# def Home(request):
#     form=EmployeeForm()
#     if request.method=='POST':
#         form=EmployeeForm(request.POST)
#         form.save()
#         form=EmployeeForm()
    
#     data=Employee.objects.all()
#     context={
#         'form':form,
#         'data':data,
#     }
#     return render(request,'app/index.html',context)
    # delete View
# def Delete_record(request,id):
#     a=Employee.objects.get(pk=id)
#     a.delete()
#     return redirect('/')

    #Update view
# def Update_Record(request,id):
#     if request.method=='POST':
#         data=Employee.objects.get(pk=id)
#         form=EmployeeForm(request.POST,instance=data)
#         if form.is_valid():
#             form.save()
#     else:

#         data=Employee.objects.get(pk=id)
#         form=EmployeeForm(instance=data)
#     context={
#         'form':form,
#     }
#     return render (request,'app/update.html',context)


# def get(request):
#     f = open('stock_market_data.json')
#     data = json.load(f)
#     for i in data:

#         create_entry = Stock.objects.create(
#             trade_code=i["trade_code"],
#             high=i["high"],
#             low=i["low"],
#             open=i["open"],
#             close=i["close"],
#             volume=i["volume"],
#             date=i["date"]
#         )
#         create_entry.save()

# def home(request):
#     if request.method == "POST":
#         file2 = request.FILES["file"]
#         document = document.object.create(file=file2)
#         document.save()
#         return HttpResponse("File Uploaded")
#     return render(request, "index.html")