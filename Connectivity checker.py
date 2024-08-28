# import urllib
# use urllib.request to get the data from the url
# func that takes url
# returns a response

import urllib.request as urllib


def main(url):
    print("Checking connectivity........")

    response=urllib.urlopen(url)
    print("Connected to url successfully")
    print("The response code was: ", response.getcode())


print("This is a site connectivity checker program")
input_url= input("Input the url you want to check: ")

main(input_url)