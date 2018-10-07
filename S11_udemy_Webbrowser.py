import webbrowser

#webbrowser.open("https://www.python.org")

help(webbrowser)

safari = webbrowser.get(using='safari')
safari.open_new_tab("http://www.cnn.com")