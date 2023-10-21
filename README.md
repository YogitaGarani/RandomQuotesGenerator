# RandomQuotesGenerator
RandomQuoteGenerator is a fast and yet extensible method for a random quote generator. This projeect encloses the following functionalities.
## Building a fixed topic based quotes repository
Notable python modules called the soup and quote exist in the open source which can be installed using pip, the python package installer. The soup module plainly parses a html page and provides specified elements to the caller. The quotes module calls the soup module to extract quotes from a well known quotes website. However, the quotes module can only find quotes matching a given word. This project modifies this module to add new interfaces to take in the topic as an argument which is translated to another api on the website to get the relevant quotes in multiple pages.
Using the above setup, a first function called scrapequote is created which iteratively calls the modified quote module function, iq, to pull a specified number of quotes for a set of topics known at the website. Each topic is created as a different file and the corresponding quotes are placed within. The format of each quote line is type casted as a dictionary type for easy parsing and processing.
## Reading from the repository
Two functions help get a random quote from the repository - gettopics and get quote. 
Gettopics returns the list of topics for which quotes exist in the repository. In addition, the gettopics function adds a string Random to the list of topics which can also be chosen by the user. 
The get quote function returns a random quote based on a topic. If the topic is Random, then a topic is also selected at random. This is achieved by simply opening the file corresponding to the topic, mapping the items as a dictionary and indexing it based on a random seed. 
## The user interface
The GUI is constructed with the tkinter module. To start with, gettopics is called to identify the topics available and based on the returned list, a set of buttons are created. When any of the buttons is clicked, the corresponding topic is identified and the getquote function is called with the topic argument. 
The GUI creates following components :
Menu bar, buttons, quote pane with background.

