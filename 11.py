string = "https://ghibliapi.vercel.app/asdfafa"
 
from urllib.parse import urlparse

def extract_domain_name(url):
    parsed_url = urlparse(url)
    
    domain = parsed_url.netloc
    
    # If no scheme like https:// is provided, netloc might be empty
    if not domain:
        domain = parsed_url.path.split('/')[0]
    print(domain)

extract_domain_name(string)