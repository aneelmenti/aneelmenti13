from django.shortcuts import render
from django.views import View
from.models import Products
from django.http import HttpResponse
# Create your views here.
class ProductsInput(View):
    def get(self,request):
        return render(request,'productsinput.html')
class ProductsInsert(View):
    def get(self,request):
        p_id=int(request.GET["t1"])
        p_name=request.GET["t2"]
        p_cost=float(request.GET["t3"])
        p_mfdt=request.GET["t4"]
        p_expdt=request.GET["t5"]
        p1=Products(pid=p_id,pname=p_name,pcost=p_cost,pmfdt=p_mfdt,pexpdt=p_expdt)
        p1.save()
        return HttpResponse("product inserted successfully")
class ProductsDisplay(View):
    def get(self,request):
        recs=Products.objects.all()
        mydict={"records":recs}
        return render(request,'display.html',context=mydict)
class ProductsDeleteInput(View):
    def get(self,request):
        return render(request,'deleteinput.html')
class ProductsDelete(View):
    def get(self,request):
        p_id=int(request.GET["t1"])
        p1=Products.objects.filter(pid=p_id)
        if p1:
            p1.delete()
            return HttpResponse("product deleted successfully")
        else:
            return HttpResponse("products doesnot exists")
class ProductsUpdateInput(View):
    def get(self,request):
        return render(request,'updateinput.html')
class ProductsUpdate(View):
    def get(self,request):
        p_id = int(request.GET["t1"])
        p_name = request.GET["t2"]
        p_cost = float(request.GET["t3"])
        p_mfdt = request.GET["t4"]
        p_expdt = request.GET["t5"]
        p=Products.objects.get(pid=p_id)
        p.pname=p_name
        p.pcost=p_cost
        p.pmfdt=p_mfdt
        p.pexpdt=p_expdt
        p.save()
        return HttpResponse("product updated successfully")




