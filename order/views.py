from django.shortcuts import redirect, render
from . models import Menu,MenuCategory
from resto.models import BookTable
def menu_view(request):
    stc=MenuCategory.objects.get(id=1)
    sac=MenuCategory.objects.get(id=3)
    spc=MenuCategory.objects.get(id=2)
    st=Menu.objects.filter(category=stc)
    sa=Menu.objects.filter(category=sac)
    sp=Menu.objects.filter(category=spc)
    context={'sp':sp,'sa':sa,'st':st}
    return render(request,'menu.html',context)

def booking_view(request):
    uid=request.session.get('uid')
    bt=BookTable.objects.filter(customer_id=uid)
    context={'bt':bt}
    return render(request,'booking.html',context)



def delete_view(request):
    uid=request.GET.get('id')
    f=BookTable.objects.get(id=uid)
    f.delete()
    return redirect('orders:bookings')