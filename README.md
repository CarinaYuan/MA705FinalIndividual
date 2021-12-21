# MA705 Final Individual Project

This repository contains files used in the MA705 dashboard project.

The final dashboard is deployed on Heroku [here](https://ma705-demo-airbnb.herokuapp.com/).

### Dashboard Description
The dashboard is designed to help users have a better understanding of Airbnb in NYC and find the desired airbnbs according to their preference.
There are mainly two parts of the analysis:

* *NYC Airbnb Overview* includes basic information about airbnbs in NYC, such as the number of airbnbs and the average price of airbnbs in each borough and the composition of airbnb type.
* *Airbnb Recommendation For You* where users can require the borough where the airbnb is located, the price of the airbnb and the type of the airbnb. The system will automatically recommend corresponding airbnbs for them.

Users can click the options on left-side bar to choose the analysis they would like to explore. And they can put their preference for location, price and type of airbnbs to find the most desirable airbnbs.
            
### Data Sources
The original dataset "listing.csv" is collected by Inside Airbnb [here](http://insideairbnb.com/get-the-data.html) on 02 November, 2021.

### Data Process
First, I dropped the airbnbs that don't have any location information, such as latitude or longtitude.
Then, I found there are some airbnbs whose longitude and latitude are not in the borough where it is recorded. So I make the polygon for each borough, and check whether the latitude/longitude is consistent with the borough in the "Borough" column. By doing this, I removed the airbnbs that have inconsistent location information.
Next, I formatted the value in "Price" column. Originally, the values in this column are "string" and contain "," and "$". So I need to replace these symbols and convert them to numerical type.
Finally, I just keep the columns that I want to use in the dashboard in the cleaned dataset.

### Other Comments
clean_data.py is just used for cleaning the original data obtained from Inside Airbnb ("listing.csv") to generate the cleaned data("airbnb_ny_listing.csv") that is used for dashboard.