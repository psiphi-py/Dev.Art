from django.shortcuts import render
from .models import Post, Artist, MainCarousel, Featured, About

def art(request):
    # defining variables and collecting Models to send to template 'art.html'

    # lp = l(ist)p(ost)
    #la = l(ist)a(rtist)
    #lmc = l(ist)m(ain)c(arousel)

    # assigns all models to variables to send to templates
    lp = Post.objects.all()
    la = Artist.objects.all()
    lmc = MainCarousel.objects.all()

    # define 3 arrays to store carousel variable data inside
    c_img = []
    c_title = []
    c_text = []

    # since we do not know the id's of MainCarousel data, we loop through all and store them in arrays
    for car_var in lmc:
        c_img.append(car_var.car_image)
        c_title.append(car_var.car_title)
        c_text.append(car_var.car_text)


    # saving all variables to be sent to template
    context = {'lp':lp, 'la':la, 'c_img':c_img, 'c_title':c_title, 'c_text':c_text}
    return render(request, 'main/art.html', context)


def featured(request):
    # defining variables and collecting Models to send to template 'featured.html'

    # l(ist)f(eature)
    lf = Featured.objects.all()
    return render(request, 'main/featured.html', {'lf': lf})

def inspect(request, id):
    lf = Featured.objects.all()

    # received art id from urls.py and send this artwork to 'inspect.html'
    lf2 = lf.get(id=id)
    return render(request, 'main/inspect.html', {'lf2':lf2})

def about(request):
    # l(ist)about
    labout = About.objects.all()
    return render(request, 'main/about.html', {'labout':labout})

def contact(request):
    # l(ist)a(rtist)
    la = Artist.objects.all()
    return render(request, 'main/contact.html', {'la':la})

def post_inspect(request, id):
    li = Post.objects.all()
    # received art id from urls.py and send this artwork to 'post_inspect.html'
    li2 = li.get(id=id)

    return render(request, 'main/post_inspect.html', {'li2': li2} )

# It's the rhythm of the night - There, now the song is stuck in your head too.