import webbrowser

chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
webbrowser.register('google-chrome', None, webbrowser.BackgroundBrowser(chrome_path))


#list of drafted players

#accumulating stats
stats = 'https://www.sports-reference.com/cbb/'
webbrowser.get('google-chrome').open_new_tab(stats)
#webbrowser.open(urL, 2, True)
