
def user_status(request):
    user = request.user
    if user.is_authenticated:
        status = 'авторизирован'
    else:
        status = 'не авторизован'
    return {'status': status}