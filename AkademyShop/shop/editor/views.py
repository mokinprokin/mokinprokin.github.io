from django.shortcuts import *
from .models import Item
from django.views.decorators.csrf import *
from .functions import *
from editor.forms import *
from django.http import *
def main(request):
    items=Item.objects.all()
    return render(request,"main.html",{"items":items})
@csrf_exempt
def adminPanel(request):
    items=[]
    form=[]
    isSuperUser=False
    try:
        superUser=request.COOKIES["admin"]

        isSuperUser= True if(superUser=="forsunkaStudy16893") else  (False,0/0)
        if (request.method=="POST"):
            if 'action' in request.POST:
                action=str(request.POST.get("action"))
                if action=='change':
                    name=str(request.POST.get("header"))
                    cost=int(request.POST.get("cost"))
                    add=int(request.POST.get("add"))
                    try:
                        item=Item.objects.get(cost=cost,name=name)
                        if(add==0 and item.count>0):
                            item.count-=1
                            item.save()
                        elif(add==1 and item.count<99):
                            item.count+=1
                            item.save()
                    except Item.DoesNotExist:
                        print("bad request")
                elif action=='edit':
                    name=str(request.POST.get("OldName"))
                    cost=int(request.POST.get("OldCost"))
                    try:
                        item=Item.objects.get(name=name,cost=cost)
                        new_name=str(request.POST.get("NewHeader"))
                        new_description=str(request.POST.get("NewDescription"))
                        new_cost=int(request.POST.get("NewCost"))
                        item.name=new_name
                        item.description=new_description
                        item.cost=new_cost
                        item.save()
                    except Item.DoesNotExist:
                        print("bad request")
            else:
                    itemForm=ItemForm(request.POST,request.FILES)
                    try:
                        if itemForm.is_valid():
                            UploadFileToDB(request.FILES["fileName"])
                            model_instance=itemForm.save(commit=False)
                            model_instance.save()
                            return HttpResponse("<a href='/adminforsunka155678915/'>Back To Admin Page</a>")
                    except Exception as ex:
                        print(ex)
        form=ItemForm()
        items=Item.objects.all()
    except:
        print("xxx")
        if request.method=="POST":
            password=str(request.POST.get("password"))
            response=redirect("/adminforsunka155678915/")
            response.set_cookie("admin",password)
            return response
    
    return render(request,"admin.html",{"items":items,"form":form,'isSuperUser':isSuperUser})