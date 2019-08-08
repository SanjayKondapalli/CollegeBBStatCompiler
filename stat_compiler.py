import webbrowser
from urllib.request import urlopen
from bs4 import BeautifulSoup

#CREATES LINK TO COLLEGE REFERENCE PAGE FOR EACH ELIGIBLE PLAYER
def createCollegeLink(name):
     lowerName = name.lower()
     fullName = lowerName.split()

     link1 = "https://www.sports-reference.com/cbb/players/"
     player = fullName[0] + "-" + fullName[1]
     link2 = "-1.html"

     fullLink = link1 + player + link2
     return fullLink

#OBTAINS USER PREFERENCES OF WHAT DRAFT CLASSES TO TRAIN/TEST (including tests)
def getUserYears():
    print("What year do you want to start training? (1980-2018)")
    
    #Training Data Start Year
    startTrainYear = input("Start Year?: ")
    if not startTrainYear.isdigit():
        print("Please enter valid number")
        return 1
    startTrainYear = int(startTrainYear)

    #Training Data End Year
    print("What year do you want to end training? (1980-2018)")
    endTrainYear = input("End Year?: ")
    if not endTrainYear.isdigit():
        print("Please enter valid number")
        return 1
    endTrainYear = int(endTrainYear)

    #Testing Data Start Year
    print("What year do you want to begin testing? (1981-2019)")
    startTestYear = input("Start Year?: ")
    if not startTestYear.isdigit():
        print("Please enter valid number")
        return 1
    startTestYear = int(startTestYear)

    #Testing Data End Year
    print("What year do you want to finish testing? (1981-2019)")
    endTestYear = input("End Year?: ")
    if not endTestYear.isdigit():
        print("Please enter valid number")
        return 1
    endTestYear = int(endTestYear)

    #Error Checks
    if endTrainYear < startTrainYear:
        return 1
    if startTestYear <= endTrainYear:
        return 1
    if endTestYear < startTestYear:
        return 1
    if startTrainYear < 1980 or startTrainYear > 2018:
        return 1
    if endTrainYear < 1980 or startTrainYear > 2018:
        return 1
    if startTestYear < 1981 or startTestYear > 2019:
        return 1
    if endTestYear < 1981 or startTestYear > 2019:
        return 1

    return 0
    

chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
webbrowser.register('google-chrome', None, webbrowser.BackgroundBrowser(chrome_path))


#MAIN FUNCTION

#Get years from users to train and test
while getUserYears() == 1:
    print("Sorry, please input your preferences again")
#ERROR TESTING USER INPUT




#list of drafted players
drafts = "https://www.basketball-reference.com/draft/NBA_"
draftyears = ["2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017",]

for x in draftyears:
    newlink = drafts + x + ".html"
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
               # print(colsNames.string)
               colLink = createCollegeLink(colsNames.string)
               page2 = urlopen(colLink)
               soup2 = BeautifulSoup(page2, "html.parser")
               
               #print(soup2,"\n")
               
        
        #First 30 players taken in the draft: AKA the first round
        if inc == 30:
            break
        inc += 1

    print(soup2)
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

