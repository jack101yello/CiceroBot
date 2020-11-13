import requests

def get_response(term): # Translates from English to Latin
    url = 'http://archives.nd.edu/cgi-bin/wordz.pl?english=' + term.strip()
    downloadFileFrom(url)
    f=open('webpage.html')
    lines = f.readlines()
    return arrPacker(lines)

def get_response_lat(term): # Translates from Latin to English
    url = 'http://archives.nd.edu/cgi-bin/wordz.pl?keyword=' + term.strip()
    downloadFileFrom(url)
    f=open('webpage.html')
    lines = f.readlines()
    return arrPackerLat(lines)

def downloadFileFrom(URL): # Downloads the HTML file for the webpage for the desired comic
    r = requests.get(URL, allow_redirects=True)
    open('webpage.html', 'wb').write(r.content)

def arrPacker(arr):
    realArr = arr[4:len(arr)-2]
    str = ''
    for line in realArr:
        str += line
    return str

def arrPackerLat(arr):
    realArr = arr[3:len(arr)-2]
    str = ''
    for line in realArr:
        if(line != ''):
            str += line
    return str