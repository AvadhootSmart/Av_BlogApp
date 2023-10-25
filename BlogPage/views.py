from django.shortcuts import render, redirect
from BlogPage.models import BlogContent


# Create your views here.
def home(request):
    # Blogs = blogs.objects.all()
    Blogs = BlogContent.objects.all()
    return render(request, "index.html",{"Blogs":Blogs})

   

def ContentBlog(request, myid):
    BlogPost = BlogContent.objects.filter(id=myid)
    return render(request, "ContentBlog.html",{"BlogPost":BlogPost} )

def User(request):
    if request.method == "POST":
        Title = request.POST.get('Title')
        Content = request.POST.get('Content')

        # Check if Title and Content are not empty
        if Title and Content:
            BlogContent.objects.create(Title=Title, Content=Content)
            return redirect('/')  # Redirect to a success page
        else:
            # Handle validation errors or inform the user that fields are required.
            return redirect('/admin/')
    return render(request, "User.html")
