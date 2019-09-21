from django.shortcuts import render

# Create your views here.
def user_create_view(request):
    form = UserModelForm(request.POST or None, request.FILES or None)
    context = {'form': form}
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        return redirect('/portfolio/users/list/')
    return render(request, 'portfolio/user_create.html', context)
