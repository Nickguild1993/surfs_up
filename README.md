# Surfs Up Analysis: Surf and Ice Cream Shop 

## Overview:

The purpose of this analysis was to query the SQLite database of weather related data in order to further ascertain the viability of opening a Surf and Ice Cream shop on the island of Oahu, Hawaii.  Specifically, our lead investor was interested in the weather for the months of June and December.  To allow for more informed decisions, we examined over 1,500 temperature readings for each month, before going deeper into other aspects of Oahu's weather patterns later in the analysis. For your consideration, all temperatures are in fahrenheit and all precipitation recordings are in inches. 

## Results:

- The average temperature for the days in June of which we have data is 74.9 degrees, with the lowest and highest recorded temperature recorded being 64 and 85 degrees respectively. The histogram below illustrates the frequency of recorded temperatures for June.

![Alt_text](https://github.com/Nickguild1993/surfs_up/blob/master/Resources/Module_9_June_Temp_Histo.png)

- The average temperature for the days in December of which we have data is 71.0 degrees, with the lowest and highest recorded temperatures being 56 and 83 degrees respectively. Again, the histogram below illustrates the frequency of recorded temperatures for December.  

![Alt_text](https://github.com/Nickguild1993/surfs_up/blob/master/Resources/Module_9_Dec_Temp_Histo.png)

- Recordings from June reveal less daily temperature fluctuation, with a range of temperatures spanning 21 degrees when compared to December, which shows recorded temperature readings with a range of 27 degrees.

- Both months have rather even distributions without many outliers to speak of. 


## Summary and Further Analysis:

Oahu has a wonderful climate that is suitable for year round surfing- it is no wonder that some of the worlds biggest surfing competitions take place here. The temperatures for both June and December, which coincide with the height of the summer and winter surf seasons, respectively, are amenable for both of our businesse's revenue streams: surfing and ice cream.  While December does have more daily variance in temperature than June, neither month has the sort of extreme temperatures across the thousands of readings we examined that would warrant further concern of the viabilty of our business based on temperature alone. 

One area of the weather on Oahu that we can delve into further for the requested windows of June and December is recorded precipitation.  Precipitation, of course, comes in many forms but for a business model that is based on warm sunny weather, in general it's not ideal to have percipitation of any kind in the forcast. At its mmost extreme, preciptiation can be accompanied by hazardous conditions, which certainly inhibit both of our potential revenue streams (the surfing revenue stream by precluding people from venturing into the water and the ice cream revenue stream by the nature of people not wanting to eat ice cream in such wet conditions). Given that, querying the database for precipitation data is good idea to further understand the relationship between weather and our venture.

To examine the precipitation data, we filtered the database for all recordings in June and December in which precipatiation was observed (meaning any amount greater than 0.00). Our summary findings and SQLite queries for each month can be found below.

```
june_precip = session.query(Measurement.date, Measurement.prcp).filter(extract("month", Measurement.date) == 6).all()
```

```
dec_precip = session.query(Measurement.date, Measurement.prcp).filter(extract("month", Measurement.date) == 12).all()
```

We found records of precipitation for 55% of the days in June.  As shown in the summary statistics listed below, the average daily rainfall (mean) was .136 inches, with a maximum recorded rainfall of 4.43 inches.

![Alt_text](https://github.com/Nickguild1993/surfs_up/blob/master/Resources/Module_9_June_prcp_describe.png)

For December, we found that 59% of days in the database showed records of precipitation. Again, as illustrated in hte summary statistics below, the average daily rainfall was .216 inches, wtih a maximum recorded rainfall of 6.42 inches.

![Alt_text](https://github.com/Nickguild1993/surfs_up/blob/master/Resources/Module_9_Dec_prcp_describe.png)

(For context, preciptiation was recorded on 55% on all days in the database, after excluding NaNs with an average recorded rainfall of .293 inches and a maximum rainfall of 11.53 inches)

So while it does rain on average on more than 50% of the days we have on record for June and December, not only is the average amount of precipitation relatively negligible, it's also less than the daily average rainfall plotted over the calendar year. Having said that, this does give more creedence to the notion that the weather in December could be negatively impactful on our renveue streams, especially when compared to June.  But again, nothing to suggest that opening a surf and ice cream shop is a catastrophic idea, at least based on the data we have available. 
