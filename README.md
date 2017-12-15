# Fantasy-Football-Analysis

First gathered all the links from which the data for each player has to be fetched using Selenium
Defined a function to crawl through each page and fetch the required data and save it as a json file
The obtained data is then analysed and the players/teams performance is predicted using machine learning



Steps for running the script.

1. For fetching the list of players from the website, run player_list.py script. A player_list.json file will be created.
2. Run player_dataset.py script to run the the webscraper for each players url. The single_data.py script is called each time to fetch the required data.
3. A fpl_data.csv file will get created when Step 2 is completed.
4. Run the pl_analysis .ipynb to precess the data and keep the essential features.
5. Analyse and get the ICT index/ value of a player and predict the best possible team from the extracted data using Logistic Regression.
