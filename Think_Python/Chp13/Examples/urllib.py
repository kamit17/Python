import urllib.request

def  retreive_page(url):
    """Retreive the contents of a webpage.
    The content is converted to a string before returning it.
    """
    
    my_socket = urllib.request.urlopen(url)
    dta = str(my_socket.readall())
    my_socket.close()
    return dta

the_text=retreive_page("https://xml2rfc.tools.ietf.org/public/rfc/xml/rfc2001.xml")
print(the_text)