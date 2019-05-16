from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response,get_object_or_404
from flight.models import flights

def salesman(request):
   return render_to_response('salesman.html')

def insert_flight(request):
   error_info = []
   FLIGHTID = request.GET['flightid']
   STARTTIME=request.GET['start_time']
   ENDTIME=request.GET['end_time']
   STARTCITY=request.GET['start_city']
   ENDCITY=request.GET['end_city']
   PRICE = float(request.GET['price'])
   Volume = int(request.GET['volume'])
   if FLIGHTID is '' or STARTTIME is '' or ENDTIME is '' or STARTCITY is '' or ENDCITY is '' or Volume is '':
      error_info.append("Input cannot be empty!")
      return render_to_response('salesman.html', {'error_info':error_info})
   this_flight=flights.objects.filter(flightid=FLIGHTID,starttime=STARTTIME)
   flights.objects.create(flightid=FLIGHTID,starttime=STARTTIME,endtime=ENDTIME,startplace=STARTCITY,endplace=ENDCITY,price=PRICE, volume=Volume)
   return render_to_response('salesman.html', {'this_flight':this_flight,'error_info':error_info})

def query_flight(request):
   query = request.GET['flight']
   flight = flights.objects.filter(flightid__icontains=query)
   return render_to_response('search_flight.html', {'query':query,'flight':flight})

def operate_flight(request):
    if request.GET['subject'] == 'delete flight':
      search_word = request.GET['search_word']
      name=request.GET['flight']
      stime=request.GET['start_time']
      etime=request.GET['end_time']
      splace=request.GET['start_place']
      eplace=request.GET['end_place']
      p=request.GET['ticket_price']
      Volume=request.GET['volume']
      flight=flights.objects.filter(flightid__icontains=search_word)

      flights.objects.filter(flightid=name,starttime=stime,endtime=etime,startplace=splace,endplace=eplace,price=p, volume=Volume).delete()

      return render_to_response('search_flight.html',{'query':search_word,'flight':flight,'delete':True, 'change':False})

    elif request.GET['subject'] == 'change flight':
      search_word = request.GET['search_word']
      o_FLIGHTID = request.GET['o_flightid']
      FLIGHTID = request.GET['flight']
      STARTTIME=request.GET['start_time']
      ENDTIME=request.GET['end_time']
      STARTCITY=request.GET['start_place']
      ENDCITY=request.GET['end_place']
      PRICE = float(request.GET['ticket_price'])
      Volume=int(request.GET['volume'])
      
      flight=flights.objects.filter(flightid=o_FLIGHTID).update(flightid=FLIGHTID,starttime=STARTTIME,endtime=ENDTIME,startplace=STARTCITY,endplace=ENDCITY,price=PRICE, volume=Volume)
      

      ffffff=flights.objects.filter(flightid__icontains=search_word)

      return render_to_response('search_flight.html',{'query':search_word,'flight':ffffff,'delete':False, 'change':True})

    



