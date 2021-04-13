"""
This program hacks westerns website
Author:  Batuhan Aktan
Student Number: 20229360
Date:  Dec 2020
"""
import urllib.request

content = ''


def openWeb(url):
    """
    This function opens any url and returns the html as a string.
    Parameters:  url - a string leading to a website.
    Return:  content - the html of the url given in string.
    """
    html = urllib.request.urlopen(url)
    content = html.read()
    content = content.decode('utf-8')
    return content 
def writeFile(content):
    """
    This function creates an html file and writes the updated content on it.
    Parameters:  none
    Return:  none
    """
    file = open("websiteContent.html", 'w')
    file.write(content)
    file.close()

def replaceWest():
    """
    This function replaces every western with Queen's.
    Parameters:  none
    Return:  none
    """
    global content #allows edits of the global content variable
    content = content.replace('Western' , "Queen's") #replaces western with Queen's using .replace()


def replaceDean():
    """
    This function replaces the dean's name and the link.
    Parameters:  none
    Return:  none
    """
    global content
    content = content.replace('https://president.uwo.ca/', 'https://www.queensu.ca/principal/about')
    content = content.replace('Dr. Alan Shepard', 'Dr. Patrick Deane')


def replaceRank():
    """
    This function replaces the rank of western from top 1% to bottom 1%.
    Parameters:  none
    Return:  none
    """
    global content
    content = content.replace('Ranked among the top 1% of higher education institutions worldwide','Ranked among the bottom 1% of higher education institutions worldwide')


def operatingRevenue():
    """
    This function replaces the operating revenue with 1000 dollars.
    Parameters:  none
    Return:  none
    """
    global content
    content = content.replace(' $778.2 million' , ' 1000 Dollars')


def replaceIpb():
    """
    This function replaces the link for Institutional planning and budgeting with Queen's website.
    Parameters:  none
    Return:  none
    """
    global content
    content = content.replace('https://www.ipb.uwo.ca/', 'https://www.queensu.ca/')


def replaceImg():
    """
    This function replaces western's image with clowns.
    Parameters:  none
    Return:  none
    """
    global content
    content = content.replace('src="../../img/about/about-flower.jpg"', 'src="./clowns.jpg"')
    content = content.replace('alt="A round flower in front of UC Tower"', 'alt="Bunch of clowns"')


def replaceEnrollment():
    """
    This function replaces the enrollment with clowns.
    Parameters:  none
    Return:  none
    """
    global content
    content = content.replace('<td class="data">Undergraduates (includes Concurrent and Medical Residents)</td>', '<td class="data">Undergraduate Clowns (includes Concurrent and Medical Clowns)</td>')
    content = content.replace('<td>Graduate</td>', '<td>Graduate Clowns</td>')
    content = content.replace('<td>PhDs</td>','<td>Clown PhDs</td>')
    content = content.replace('<strong>Total:</strong>', '<strong>Total Clowns:</strong>')

def replaceWhoWeAre():
    """
    This function replaces who we are link with a clown hiring website.
    Parameters:  none
    Return:  none
    """
    global content
    content = content.replace('<a class=" selected" href="index.html">Who We Are</a>', '<a class=" selected" href="https://www.gigsalad.com/Circus-Entertainment/Clown">Who We Are</a>')

    
def main():
    """
    This function puts all the functions together to edit westerns website.
    Parameters:  none
    Return:  none
    """
    global content
    content = openWeb("https://www.uwo.ca/about/whoweare/facts.html")
    replaceWest()
    replaceDean()
    replaceRank()
    operatingRevenue()
    replaceIpb()
    replaceImg()
    replaceEnrollment()
    replaceWhoWeAre()
    writeFile(content)
    
main()

