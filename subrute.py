# ############################## subdomain bruteforce script py Virus T #############################################

# needed libraries
import requests

# getting the target url
target=input("Enter the target domain:")

# getting the path of the wordlist from the user
list_path = input("Enter the path of the word list:")
print("\n\n")
# opening the wordlist file
open_file = open(list_path)
list = open_file.read()
subdomains = list.splitlines()

# starting the bruteforce search
for subdomain in subdomains:
  try:  # trying to find the url

    url = "https://%s.%s" % (subdomain, target)  # making the url from the data given by the users
    Response = requests.get(url)  # sending the request and getting the response from the server
    print("[+]%s = Found(%s)"%(url,Response.status_code))  # this subdomain is available
  except requests.exceptions.ConnectionError as e:
    print("[-]%s = Not Found"%(url))  # this subdomain is not available
