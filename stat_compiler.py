import webbrowser
from urllib.request import urlopen
from bs4 import BeautifulSoup

chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
webbrowser.register('google-chrome', None, webbrowser.BackgroundBrowser(chrome_path))


#list of drafted players
drafts = "https://www.basketball-reference.com/draft/NBA_"
draftyears = ["2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017",]

for x in draftyears:
    newlink = drafts + x + ".html"
    #webbrowser.get('google-chrome').open_new_tab(newlink)
    page = urlopen(newlink)
    soup = BeautifulSoup(page, 'html.parser')
    
    data = []
    table = soup.find('table', attrs={'id' : 'stats'})
    tableBody = table.find('tbody')
    rows = tableBody.find_all('tr')

    inc = 1
    for row in rows:
        colsNames = row.find('td', attrs={'data-stat':'player'})
        colsUnis = row.find('td', attrs={'data-stat':'college_name'})
        
        #print(colsUnis)
        if colsNames:
            american = colsUnis.find('csk')
            if colsUnis.string:
                print(colsNames.string)

        #First 30 players taken in the draft: AKA the first round
        if inc == 30:
            break
        inc += 1
    print("\n\n")


    table = soup.find('tbody')
    rowInTable = soup.find_all("tr")
    #if x == "2000":
        #print(rowInTable)
    #data_soup = BeautifulSoup(rowInTable, 'html.parser')
    #for y in range(30):
        #number = str(y)
        
        #row = soup.find_all(attrs={"data-row": "0"})
       # row2 = soup.find_all("data-row")
        #print(row2)
        
    #Scrape the table to get a list of all draft picks
    #print("\n\n\n")


#print(rowInTable)

#accumulating stats

#stats = 'https://www.sports-reference.com/cbb/'
#webbrowser.get('google-chrome').open_new_tab(stats)

