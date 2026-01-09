import webbrowser

def url_validator(func):
    def wrapper(url):
        if url.startswith('https://') and '.' in url:
            func(url)
        else:
            print('URL is not valid')
    return wrapper

@url_validator
def open_url(url):
    webbrowser.open(url)

open_url('https://youtube.com')