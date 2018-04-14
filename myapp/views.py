from django.shortcuts import render
from django.shortcuts import loader
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import generic
from .models import Post
from django.http import HttpResponse
from .models import book
from .models import books
# Create your views here.
from .forms import ProductForm
import datetime


def index(Request):
    return  HttpResponse("hey")

def contact(Request):
    return render(Request,'myapp/basic.html',{'content':['hari','priya']})





@csrf_exempt
def cred(request):
    # if post request came
    if request.method == 'POST':
        v1 = request.POST.get('username')
        v2 = request.POST.get('password')


        data = Post(username=v1,password=v2)
        data.save()
        # adding the values in a context variable
        context = {
            'super1': v1,
            'super2': v2,
        }
        # getting our showdata template
        template = loader.get_template('myapp/show.html')



        # returing the template
        return HttpResponse(template.render(context, request))


    else:
        # if post request is not true
        # returing the form template
        template = loader.get_template('myapp/form.html')
        return HttpResponse(template.render())


@csrf_exempt
def sum(request):
    if request.method == 'POST':
        v1 = request.POST.get('n1')
        v2 = request.POST.get('n2')

        s=int(v1)+int(v2)

        context = {
            'super1': s
        }
        template = loader.get_template('myapp/sum2.html')

        # returing the template
        return HttpResponse(template.render(context, request))
    else:
        template = loader.get_template('myapp/sum1.html')
        return HttpResponse(template.render())



# generic view to show the details of a particular object
class DetailsView(generic.DetailView):
    model = Post
    template_name = 'myapp/post.html'


class IndexView(generic.ListView):
    # a name to refer to the object_list(to be used in the index.html)
    context_object_name = 'product_list'
    template_name = 'myapp/index.html'

    def get_queryset(self):
        return books.objects.all()



def makeentry(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)

        if form.is_valid():
            author = request.POST.get('author', '')
            title = request.POST.get('title', '')
            text = request.POST.get('text', '')
            created_date = request.POST.get('created_date', '')
            published_date= request.POST.get('published_date', '')


        product = books(author=author,title=title,text=text,created_date=created_date,published_date=published_date)
        product.save()

        form = ProductForm()

        return render(request, 'myapp/makeentry.html', {'form': form})
    else:
        form = ProductForm()
        return render(request, 'myapp/makeentry.html', {'form': form})




# generic view to show the details of a particular object
class DetailsView(generic.DetailView):
    model = books
    template_name = 'myapp/detail.html'



def daysweek(request):
   today = datetime.datetime.now().date()
   time=datetime.datetime.now().time()
   daysOfWeek = ['January', 'February', 'March', 'April', 'May', 'June', 'July','August','September','October','November','December']
   #return render(request, "myapp/daysoftheweek.html", {"today": today, "days_of_week":daysOfWeek,"time":time})
   context = {
    'today': today,
    'time': time,
    'days_of_week':daysOfWeek
    }
   template = loader.get_template('myapp/daysoftheweek.html')
   return HttpResponse(template.render(context, request))


class startview(generic.ListView):
    # a name to refer to the object_list(to be used in the index.html)
    context_object_name = 'product_list'
    template_name = 'myapp/index1.html'

    def get_queryset(self):
        return books.objects.all()
