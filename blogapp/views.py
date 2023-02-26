from django.shortcuts import render , get_object_or_404
from django.urls import reverse_lazy , reverse
from django.views.generic import ListView, DetailView , CreateView , UpdateView , DeleteView 
from .models import  post  , Catagory , Coment  
from django.shortcuts import redirect	
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
#auth library 
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.decorators import login_required
from .forms import UserForm , postForm , AddCommentform


# Create your views here.

def admin_redirect(request):
    return redirect('/admin/')


class Homeview(ListView):
    model = post
    template_name = 'blogapp/base.html' 
    ordering = ['-post_date']


class ArticleDetailsview(DetailView):
    model= post
    template_name = 'blogapp/article.html'


    def get_context_data(self, *args, **kwargs):
        context = super(ArticleDetailsview , self).get_context_data()
        stuff = get_object_or_404(post , id=self.kwargs['pk'])

        # liked = False
        # if stuff.likes.filter(id = self.request.user.id).exists():
        #     liked = True

        # total_dislikes = stuff.total_dislikes()
        # context["total_dislikes"] = total_dislikes

        total_likes = stuff.total_likes()
        context["total_likes"] = total_likes
        # context["liked"] = liked
        return context
        

class Addarticle(CreateView):
    model = post
    form_class =postForm
    template_name = ('blogapp/add_post.html')
    # fields = ("__all__")

# def create_post(request):
#     if request.method == 'POST':
#         form = postForm(request.POST, request.FILES)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.save()
#             return redirect('article', pk=post.pk)
#     else:
#         form = postForm()
#     return render(request, 'blogapp/add_post.html', {'form': form})


class Editarticle(UpdateView):
    model = post
    form_class =postForm
    template_name = ('blogapp/edit.html')
    # fields = ('title' , 'title_tags' , 'body')

class deletepostarticle(DeleteView):
    model = post
    form_class =postForm
    template_name = 'blogapp/delete-post.html'
    success_url  = reverse_lazy('home')

class AddComment(CreateView):
    model = Coment
    form_class = AddCommentform
    # fields = '__all__'
    template_name = ('blogapp/add_comments.html')  

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    
    success_url  = reverse_lazy('home')


class Addcatagory(CreateView):
    model = Catagory
    fields = '__all__'
    template_name = ('blogapp/add-catagory.html')  

def CatagoryView(request , cats):
    Catagory_posts = post.objects.filter(catagory=cats)
    ordering = ['-post_date']
    return render(request , 'blogapp/catagories.html', {'cats' : cats  , 'Catagory_posts' : Catagory_posts}) 

# Create your views here.

def catagoriesview(request):
    return render(request,'blogapp/catagoriesview.html')


# def PostManagemnet(request):
#     return render(request,'blogapp/post_mng.html')





def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        sign_form = UserForm()
        if (request.method == 'POST'):
            sign_form = UserForm(request.POST)
            if(sign_form.is_valid()):
                sign_form.save()
                msg = 'user account created for username: '+ sign_form.cleaned_data.get('username')
                messages.info(request ,msg)
                return redirect('login')

        context = {'sign_form': sign_form}
        return render(request , 'blogapp/sign.html' , context)


def logins(request):
    if request.user.is_authenticated:
        return redirect('home')
   
    else:
        if request.method == 'POST':
            name = request.POST.get('username')
            passwd = request.POST.get('password')
            user=authenticate( username= name, password = passwd)

            if user is not None:
                login(request,user)
                if user.is_active:
                     return redirect('home')
                
                else:
                
                    messages.info(request, 'YOUR ACCOUNT IS LOCKED, PLEASE CONTACT AN ADMIN')
                
            else:
                messages.info(request, 'INVALID USERNAME OR PASSWORD !')

            

        return render(request, 'blogapp/login.html')



def logouts(request):
    logout(request)
    return redirect('home')


def LikeView(request , pk):
    posts = get_object_or_404(post, id=request.POST.get('post_id'))
    posts.likes.add(request.user)
    # liked = False
    # if posts.likes.filter(id = request.user.id).exists():
    #     posts.likes.remove(request.user)
    #     liked = False
    # else:
    #     posts.likes.add(request.user)
    #     liked =True
    
    return HttpResponseRedirect(reverse('article' , args=[str(pk)]))

# def DislikeView(request , pk):
#     posts1 = get_object_or_404(post, id=request.POST.get('post_id'))
#     posts1.dislikes.add(request.user)
#     return HttpResponseRedirect(reverse('article', args=[str(pk)]))
