import traceback
from django.shortcuts import render
from django.shortcuts import render, redirect  
# from blog.forms import Blog

from blog.forms import BlogForm, EditBlogForm
from blog.models import  Blog


# Create your views here.  
def post_new_blog(request):
    '''
    work:- create the blog
    '''

    # if method is post then
    if request.method == "POST":
        form = BlogForm(request.POST)
        # validate the form
        if form.is_valid():
            # if form is valid then save in database
            try:
                # save the blog
                form.save()
                # redirect to all blog show template
                return redirect('/show')  
            except Exception as e:
                # if exception is there  just print the error in console
                traceback.print_exc()
                # and pass
                pass
    else:

        form = BlogForm()
    #  return to the index.html where create the post
    return render(request,'index.html',{'form':form})


def show(request):
    '''
    work:-  if the method is get show all the blog detail
    '''
    try:

        if request.method == "GET":
            # get all the blog query set from log table
            Blogs = Blog.objects.all()
            # and send it to show.html
            return render(request,"show.html",{'Blogs':Blogs})
    except Exception as e:
        traceback.print_exc()



def edit(request, id):
    """
      :purpose: get  the blog title and discription
      :input: blog id
      :models: Blog
      :Output: retrieve the particular id base query
      """
    try:
        # retrieve the queryset respective id
        edit_blog = Blog.objects.get(id=id)
        return render(request,'edit.html', {'Blog':edit_blog})
    # if blog id is not exist in table
    except Blog.DoesNotExist:

        traceback.print_exc()
        # return to the all posted blog
        return redirect("/show")

def update(request, id):
    """
      :purpose: get  the blog id in url
      :input: blog id
      :models: Blog
      :Output: edit the blog and update and redirect to  main blog page
    """

    update_blog = Blog.objects.get(id=id)
    form = EditBlogForm(request.POST, instance = update_blog)
    print(request.POST)
    try:
        if form.is_valid():
            form.save()
            return redirect("/show")
    except Exception as e:
        print(e,'jiiiiiiiiiiiiiiiiiiiiiiiiiii')
    return render(request, 'edit.html', {'Blog': Blog})


def destroy(request, id):
    """
         :purpose: get  the blog id in url
         :input: blog id
         :models: Blog
         :Output: delete the blog and redirect to  main blog page
       """
    distroy_blog = Blog.objects.get(id=id)
    distroy_blog.delete()
    return redirect("/show")