# INST326-Project
This is for the final project in INST326 with instructor Cruz. Members of the group are Samuel, Isaac, Craig, and Shalome. 
Instructor Cruz has given us the exception to meet the requirements for 3 memembers due to project member issues.

Documentation: 

    Our project scrapes data off of the FootLocker website in order to use that data to 
    help shoppers find particular shoes. We do this by scraping data off of the pages on the site,
    then scraping individual shoe data and saving those attributes that we have scraped.
    Once we have saved the individual shoe attributes, we are then able to use those attributes
    in a function that would simplify the shopping experience for the user online. 

    DISCLAIMERS:
    The program does take a decent amount of time to run through depending on how many pages are iterated through.
    If you are using a slow computer or have a slow internet connection, you may want to increase the amount of 
    time.sleep() in the scrape() function of the automated.py file if the pages are not iterating. 

    The program only runs using the Google Chrome browser and the user must download the correct
    chromedriver.exe. This can be downloaded at https://chromedriver.chromium.org/downloads 
    To check which version you need click the three dots in the top right of a tab
    and hover over "Help" and then click "About Google Chrome".
    
    In order to run our program from the command line, the user needs to input certain criteria such as 
    desired attributes of a shoe,the desired gender of the shoe, and the PATH that your chromedriver.exe 
    is located and then run the site.py file. Please use lower case attributes when entering in the command line. 
    An example of what would be input in the command line for Windows is: 
    "python site.py --attributes black nike --gender W --PATH "C:\Program Files (x86)\chromedriver.exe""
    
    To interpret the output of the program, you would see the attributes of the shoe that best fits the 
    user criteria and satisfies what they are searching for. 
    The best way to find the shoe that is output is to find the last element, which is a modified 
    product ID#. The actual product ID# is everything until the first space or lower case letter. 
    For example, if the modified ID# is "1018581Reach", then the actual ID# is "1018581". 
    If the modified ID# is "7953BLKSay", then the actual ID# is "7953BLK".
    After you have the actual ID#, you can go to https://www.footlocker.com/ and type it into
    the search bar. After entering the search, you should be directed to the matching shoe's page. 

    Thank you for using our program!
