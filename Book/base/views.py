from django.shortcuts import render,HttpResponse
from .models import  People
from flight.models import flights
from account.models import User
from base64 import b64encode
from datetime import datetime
from django.utils.timezone import timedelta

def base(request):
    if request.method == "GET":


            return render(request, "base.html")
    else:    
        data = dict(request.POST)
        for k,v in data.items():
            if isinstance(v, list):
                if len(v)>1:
                    data[k] = ','.join(v)
                elif len(v)==1:
                    data[k] = v[0]
                else:
                    data[k] = ''
            else:
                data[k] = ''
        startplace = data["departure"]
        endplace = data["destination"]
        check_in_time = data["CheckIn"]
        in_time = datetime.strptime(check_in_time, '%Y-%m-%d') + timedelta(days=1)
        flight_query = flights.objects.filter(startplace__contains=startplace, endplace__contains=endplace, starttime__range=(check_in_time, in_time))
        flight_list = []
        for i in flight_query:
            d = {}
            # d["id"] = i.id
            d["flight_number"] = i.flightid
            d["departure"] = i.startplace
            d["destination"] = i.endplace
            d["check_in_date"] = check_in_time  
            d["check_in_time"] = i.starttime.strftime("%H:%M:%S")
            d["check_out_time"] = i.endtime.strftime("%H:%M:%S")
            d["price"] = i.price
            flight_list.append(d)
        s = "搜索时间为"+check_in_time+"出发地为["+startplace+"], 目的地为["+endplace+"]的航班："
        choices = [s]
        
        flight_list_div = []
        tmp = []
        ct = 0
        
        
        while 1:
            try:
                tmp.append(flight_list[ct])
                if (ct + 1) % 5 == 0:
                    flight_list_div.append(tmp)
                    tmp = []
                ct += 1
            except:
                flight_list_div.append(tmp)
                break
                



        return render(request, "base.html",{"flight_list_div":flight_list_div,"choices":choices})

def info(request):
    if request.method == "GET":
        data = dict(request.GET)
        for k,v in data.items():
            if isinstance(v, list):
                if len(v)>1:
                    data[k] = ','.join(v)
                elif len(v)==1:
                    data[k] = v[0]
                else:
                    data[k] = ''
            else:
                data[k] = ''
        flight_number = data["f1"]
        departure = data["f2"]
        destination = data["f3"]
        check_in_date = data["f4"]
        check_in_time = data["f5"]
        check_out_time = data["f6"]
        price = data["f7"]
        return render(request, "info.html", {"flight_number":flight_number, "departure":departure, "destination":destination, "check_in_date":check_in_date, "check_in_time":check_in_time, "check_out_time":check_out_time, "price":price})

def confirm(request):
    if request.method == "GET":
        return render(request, "confirm.html")
    else:
        data = dict(request.POST)
        for k,v in data.items():
            if isinstance(v, list):
                if len(v)>1:
                    data[k] = ','.join(v)
                elif len(v)==1:
                    data[k] = v[0]
                else:
                    data[k] = ''
            else:
                data[k] = ''
        name = data["name"]
        id_number = data["id_number"]
        result = People.objects.filter(name__exact=name, id_number__exact=id_number)
        if result.exists():
            return render(request, "success.html")
    return render(request, "confirm.html", {"info":"身份验证失败,请重试！"})



        
    
