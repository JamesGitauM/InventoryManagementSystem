from django.shortcuts import render,redirect, HttpResponse,get_object_or_404
from inventory.models import *
from .forms import *

# Create your views here.

def index(request):
    return render(request, 'index.html')


def display_laptop(request):
    #returning all entries in the laptop models
    items=Laptop.objects.all()
    context={
    'items':items,
    'header':'Laptops',
    }
    return render(request,'index.html',context)

def display_desktop(request):
    #returning all entries in the laptop models
    items=Desktop.objects.all()
    context={
    'items':items,
    'header':'Desktops',
    }
    return render(request,'index.html',context)

def display_mobile(request):
    #returning all entries in the laptop models
    items=Mobile.objects.all()
    context={
    'items':items,
    'header':'Mobiles',
    }
    return render(request,'index.html',context)


# adding items views
# def add_laptop(request):
#     if request.method=="POST":
#         form=LaptopForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#
#
#
#     else:
#         form=LaptopForm()
#         # LaptopForm
#         return render(request,'add_new.html',{'form':form})
#
#
# def add_desktop(request):
#     if request.method=="POST":
#         form=DesktopForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#
#
#
#     else:
#         form=DesktopForm()
#         # LaptopForm
#         return render(request,'add_new.html',{'form':form})
# def add_mobile(request):
#     if request.method=="POST":
#         form=MobileForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#
#
#
#     else:
#         form=MobileForm  ()
#         # LaptopForm
#         return render(request,'add_new.html',{'form':form})
def add_device(request,frm):
    if request.method=="POST":
            form=frm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('index')
    else:
            form=frm  ()
             # frm
            return render(request,'add_new.html',{'form':form})
def add_laptop(request):
    return add_device(request,LaptopForm)
def add_desktop(request):
    return add_device(request,LaptopForm)
def add_mobile(request):
    return add_device(request,MobileForm)


# editing item functions:   generalization of edit devices
def edit_device(request,pk,model,frm):
    item=get_object_or_404(model,pk=pk)
    if request.method=="POST":
        form=frm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')


    else:
        form=frm(instance=item)
        return render(request,'edit_item.html',{'form':form})


def edit_desktop(request,pk):
    return edit_device(request,pk,Desktop,DesktopForm)
def edit_laptop(request,pk):
    return edit_device(request,pk,Laptop,LaptopForm)
def edit_mobile(request,pk):
    return edit_device(request,pk,Mobile,MobileForm)

# def delete_device(request,pk,model):
def delete_laptop(request,pk):
    Laptop.objects.filter(id=pk).delete()
    items=Laptop.objects.all()
    context ={'items':items}
    return render(request,'index.html', context)
def delete_desktop(request,pk):
    Desktop.objects.filter(id=pk).delete()
    items=Laptop.objects.all()
    context ={'items':items}
    return render( request,'index.html', context)
def delete_mobile(request,pk):
    Laptop.objects.filter(id=pk).delete()
    items=Mobile.objects.all()
    context ={'items':items}
    return render(request,'index.html', context)
