**Ask – Defining the Business Task**

Cyclisitc believes increasing its number of members as key to growth since they are more profitable than the casual riders. The main scope of this project is to find out how to convert casual riders into annual members. We aim to do this by studying the difference in usage patterns among the two and then designing a marketing strategy based on that.

Three questions will guide the future marketing program:

1. How do annual members and casual riders use Cyclistic bikes differently?
2. Why would casual riders buy Cyclistic annual memberships?
3. How can Cyclistic use digital media to influence casual riders to become members?

**Prepare – Description of Data Sources Used**

Use Cyclist’s historical trip data to analyze and identify trends. The data used has been made available by Motivate International Inc. The data is public data and can be used for research purposes like this without exposing the rider’s personally identifiable information to avoid privacy concerns.

For this case study, we will use the data for the first quarter of 2020. We will download the csv file for all the months one by one from the data repository. The source data is large at about 426k data points.

**Process – Documentation of Cleaning and Manipulating Process**

1. Made the backup of initial data before modifying them
2. Imported the file into excel using “_Get Data_” function in “_Data_” tab of excel
3. Used Power Query Editor to manipulate the data
4. Selected the relevant columns for our analysis
5. Calculated “_ride_length”_ and fields using “_Custom Column_” function in Power Query
6. Added the following columns by performing transformations on duplicated “_started_at_” column: _day_of_ride, hour_of_ride_
7. Categorized _ride_length_ into _ride_length_buckets_ in a separate column to make the analysis more meaningful.
8. Used the “_Group By”_ function from “_Transform”_ tab.
9. Loaded the final cleaned data into worksheet from the Power Query Editor.

**Analyze – Summary of Analysis**

The two types of riders are defined as follows:

1. **Casual Riders**: Customers who purchase single-ride or full-day passes
2. **Members**: customers who purchase annual memberships

We will study the difference in usage patterns among the two.

We can use Pivot Table to find the relevant summary statistics for relevant fields by making use of the Filters and Excel Formulas,

| **Statistic** | **Whole Data** | **For Casual Riders** | **For Members** |
| --- | --- | --- | --- |
| Most Frequent Ride Length | 5-10 minutes | More than 20 minutes | 5-10 minutes |
| Average Ride Length | 11.6 minutes | 20 minutes | 10 minutes |
| Maximum Ride Length | 59 minutes | 59 minutes | 59 minutes |
| Busiest Hour | 5 pm | 2 pm | 5 pm |
| Busiest Day | Tuesday | Sunday | Tuesday |

**Share – Visualizations and Key Findings**

Now we use “Pivot Charts” to make visualizations to see the difference in usage patterns between them.

**Total Number of Rides**
![](https://github.com/harigovindr2003/projects/blob/main/Cyclistic%20Case%20Study/casual%20vs%20members.png)

This supports our initial assumptions that members are indeed more profitable than casual riders since they make many times more rides than casual riders.

**Rides by day of the week**
![](https://github.com/harigovindr2003/projects/blob/main/Cyclistic%20Case%20Study/distribution%20by%20day.png)

Members use the bikes more on workdays and casual rides use it more on weekends, most on Sunday. Together they use the bike service most on Tuesday. So, Tuesday is most traffic day for Cyclist.

This suggests that the members are mainly office commuters and the casual riders are mostly tourists.

**Rides by hour of day**
![](https://github.com/harigovindr2003/projects/blob/main/Cyclistic%20Case%20Study/distribution%20by%20hour.png)

Members use the service the most during office commute hours, i.e. early morning and in the evenings. This further proves that the bulk of members are office commuters. The casual riders see a very sharp decline in the early morning commuting hours, this is also in line with our earlier observation that they are mostly made up of tourists.

**Rides by ride length buckets**
![](https://github.com/harigovindr2003/projects/blob/main/Cyclistic%20Case%20Study/ride%20length%20bucket%20of%20casual%20riders.png)

Here we can see that the casual riders frequently make rides that are more than 20 minutes. This might mean that casual riders are using the bikes for leisure exploration. The frequencies for “Less than 5 minutes” ride are the least for casual riders. This suggests that the tourists would have more rides that are longer.
![](https://github.com/harigovindr2003/projects/blob/main/Cyclistic%20Case%20Study/ride%20length%20bucket%20of%20members.png)

Member riders most frequently make rides that are 5-10 minutes long. We see that the members have often fixed commute times. If the commute time was higher, they would most likely for other transportation methods. So, “More than 20 minutes” rides are least for them.

**Act – Recommendations**

Here are our observations about casual riders based on the data:

1. Ride more on weekends
2. Low ride counts during early morning
3. Most rides during midday
4. Makes rides that are longer than 20 minutes frequently

By analyzing data for the whole year, we can hope to find many more patterns on bike usage by monthly and seasonal variations. But these variations might be producing mostly the same effect on both casual and member riders.

Strategies to convert Casual Riders into Members:

1. Since they ride more on weekends, a yearly or monthly riding plan might not seem useful for them, a Weekend Subscription Plan at lower prices might seem interesting to them. Commuters who don’t take bikes for various reasons, might also take this plan to ride on weekends for leisure.
2. There might be people who don’t commute during the early office hours but only start later, they may not see the value in a Single Day pass, so having an Afternoon Plan at half the price of a full day pass might interest them.
3. This Afternoon Plan can have a time window like 12 pm to 6 pm. This will also interest people who are free in the afternoon regularly to spend their time.
4. Loyalty programs that reward extra free minutes based on how long and how much they drive can incentivize them to sign up for the Loyalty Program Plan.
5. Loyalty Program Plan is free to signup and offers no free ride time windows, but the riders can accumulate extra free minutes on a ride which they can use for the next ride.
6. Since the casual riders make longer riders frequently, we can introduce a loyalty program that rewards them for each minute after 20-minute mark with extra free minutes which can be used in later rides.

**Recommended New Plan Structure:**

| Loyalty Program Plan | Incentivize more rides and longer ones. |
| --- | --- |
| Afternoon Plan (12 pm – 6 pm on all days) | For people who don’t use the bikes full day. |
| Weekend Plan (Saturdays and Sundays) | For tourists and people exploring. |
