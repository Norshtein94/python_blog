from django.shortcuts import render
from django.shortcuts import redirect
import logging

logger = logging.getLogger('blog_app.views')


# Create your views here.


def home(request):
    if request.session.get('is_login') == '1':
        return render(request, 'home.html', {'username': request.session.get('current_username')})
    else:
        return render(request, 'login.html')


# login
def login(request):
    logger.debug('request.method is %s', request.method)

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        logger.debug("username is %s and password is %s", username, password)
        # validate username and password
        if username == 'test' and password == 'test123':
            # create session
            request.session['is_login'] = '1'
            request.session['current_username'] = username
            return redirect('home')
        else:
            login_error = 'Username or password is wrong!'
            return render(request, 'login.html', {'login_error': login_error, 'username': username})
    else:
        return render(request, 'login.html')
