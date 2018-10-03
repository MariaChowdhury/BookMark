"""
This script takes online books url of rss feed as input. Then creates an .xml file and 
processes the .xml file to return json file that contains Title, Year, and Author of book information
"""
# importing the required modules

import json
import requests
import xml.etree.ElementTree as ET

def loadRSS():

    # url of rss feed
    url = 'https://onlinebooks.library.upenn.edu/newrss.xml'

    # creating HTTP response object from given url
    resp = requests.get(url)

    # saving the xml file
    with open('onlinebooks.xml', 'wb') as f:
        f.write(resp.content)


def parseXML(xmlfile):

    # create element tree object
    tree = ET.parse(xmlfile)

    # get root element
    root = tree.getroot()

    # create empty list for book items
    bookitems = []

    # iterate book item
    for item in root.findall('./channel/item'):

        for child in item:
            if child.tag == 'description':

                # append description to list of items
                bookitems.append(child.text)
    return bookitems





def main():
    #url=argv[1]
    # load rss from web to update existing xml file
    loadRSS()

    # parse xml file
    bookitems = parseXML('onlinebooks.xml')
    book={}
    for item in bookitems:
        line=item.split("(")
        title=line[0]
        rest=line[1]
        year_author=rest.split(")")
        year_publisher=year_author[0]
        year_published=year_publisher.split(" ")
        year=year_published[len(year_published)-1]
        if len(year)>4:
            year=year.replace('c','')
        author=year_author[1]
        author=author.replace(",  by ",'')
        if year.isdigit():

            book["Title"] = title
            book["Year"] = year
            book["Author"]=author

        print(json.dumps(book))
        
if __name__ == "__main__":

    main()
