from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import NameForm
from .models import Static_informations 
# Create your views here.


def ok(request):
    my_context = {"mydata":"newdata",
    "mynumer":123}
    data_query = Static_informations.objects.all()

    # print(,"++++++++++++++++++++++++++++++++++++")

    return render(request,"calculater.html",my_context)


# def calculater(request):
def calculater(request):
    context = {}

    # data_query = Static_informations.objects.all()
    # new1 = list(data_query.values())[0]
    # context["data"] = new1["data_of_filed"]
    # context["colour"] = new1["colour"]
    # context["textalling"] = new1["text_alingment"]
    # context["inputtype"] = new1["inputtype"]

    if request.method == "GET":
        # print(list(data_query.values())[0],"==========================================")
        # context["data"] = list(data_query.values())[0]
        data_query = Static_informations.objects.all()
        new1 = list(data_query.values())[0]
        context["data"] = new1["data_of_filed"]
        context["colour"] = new1["colour"]
        context["textalling"] = new1["text_alingment"]
        context["inputtype"] = new1["inputtype"]




        return render(request, "calculater.html",context)
    if request.method == "POST":
        context = {}


        data_query = Static_informations.objects.all()

        new1 = list(data_query.values())[0]
        context["data"] = new1["data_of_filed"]
        context["colour"] = new1["colour"]
        context["textalling"] = new1["text_alingment"]
        context["inputtype"] = new1["inputtype"]

        value=request.POST['fname']
        value1=request.POST['lname']
        try:
            value = int(value)
            value1 = int(value1)
            new = value+value1
            context ={"value":value,
            "value1":value1,
            "new":new,
            "data":new1["data_of_filed"],
            "colour":new1["colour"],
            "textalling":new1["text_alingment"],
            "inputtype" : new1["inputtype"]}


        except:
            context ={"value":value,
            "value1":value1,
            "new":"",
            "data":new1["data_of_filed"],
            "colour":new1["colour"],
            "textalling":new1["text_alingment"],
            "inputtype" : new1["inputtype"]}
        
        
        # print(value)
        print(context)
        return render(request, "calculater.html", context)





