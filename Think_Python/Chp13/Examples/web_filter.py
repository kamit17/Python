import urllib.request

url = "https://xml2rfc.tools.ietf.org/public/rfc/xml/rfc2001.xml"

destination_filename="rfc2001.xml"

urllib.request.urlretrieve(url,destination_filename)