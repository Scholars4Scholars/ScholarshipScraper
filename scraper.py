from bs4 import BeautifulSoup
import  requests
import json
import uuid

def parseHTML(html):
    pageAsDictionary = {}
    soup = BeautifulSoup(html, 'html.parser')
    titleHTML = soup.find_all("div", class_='title')
    if len(titleHTML) > 0:
        titleHTML = titleHTML[0]
    else:
        return None
    if titleHTML is None:
        return None
    title = titleHTML.find('h3')
    if title is None:
        return None
    else:
        pageAsDictionary['title'] = title.get_text()
    existsParameter = False

    #sketch af, but works.
    keys = soup.find_all('dt')
    values = soup.find_all('dd')
    index = 0
    for item in keys:
        key = item.get_text()
        value =  values[index]
        if key and value:
            existsParameter = True
            pageAsDictionary[key] = value.get_text()
        index += 1

    if existsParameter:
        return pageAsDictionary
    else:
        return None


def testHTML():
    with open('sample_no_login.html', 'r') as myfile:
        data = myfile.read()
        return parseHTML(data)

def main():
    array = []
    id = 16900
    for i in xrange(0,1):
        id += 1
        url = 'http://www.fastweb.com/college-scholarships/scholarships/' + str(id)
        request = requests.get(url)
        dictionary = parseHTML(request.text)

    print(dictionary)

def main():
    array = []
    id = 165628
    for i in xrange(0,4000):
        id += 1
        url = 'http://www.fastweb.com/college-scholarships/external_scholarships_search/' + str(id)
        request = requests.get(url)
        dictionary = parseHTML(request.text)
        if dictionary is not None:
            dictionary['id'] = id
            array.append(dictionary)
            if len(array) > 25:
                filename = str(uuid.uuid4()) + '.json'
                with open(filename, 'w') as outfile:
                    json.dump(array, outfile)
                array = []
    filename = str(uuid.uuid4()) + '.json'
    with open(filename, 'w') as outfile:
        json.dump(array, outfile)


main()