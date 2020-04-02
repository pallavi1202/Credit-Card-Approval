Predicting Credit Card Approval 
For this project I’m using a credit card approval dataset from UCI Machine Leaning Repository with 16 attributes and 690 rows.
Steps of the Project:
1.	Libraries used:
•	Numpy to create and use data frames
•	Pandas to pre - process and analyse data
•	Scikit- learn (sklearn) to scale the data,  split data into test train, for logistic regression, confusion matrix,  Random Classifier, and label encoder,
•	Matplotlib to plot the feature importance
2.	Load and view the data
3.	Get the information of all the attributes and their data types 
4.	Gest the description of the numeric attributes like mean, median, min , max etc
5.	Pre-process the data:
a.	Replace all the ‘?’(they are used in the dataset instead of empty cells) with NA to make the computation easier
b.	Convert ‘Age’ to numeric 
c.	Imputing missing values of the numeric attributed with mean of the column to make the data relevant and to avoid anomalies
d.	Fill the non – numeric empty cells with the most frequent values of the column 
e.	Converting the non-numeric attributes to numeric for ease of computation using label encoder
6.	Driver’s License(if the applicant has a driver’s license or not) and Zip Code(the zip code of the applicant) were dropped from the dataset as they were less relevant to the data and had low correlation with an applicant being ‘Approved’ or not.
7.	Splitting the data into test and train in 20/80 ratio to prepare the dataset for two different phases of Regression. 
8.	The split data is scaled to have a uniform range (0-1). The data is scaled after splitting as in ideal regression model the test and train data must be independent of each other.
9.	The rescaled train data is fit into logistic regression model. The predictive model gives the accuracy and a confusion matrix
10.	To find the feature importance Random Forest tool is used. The scaled train data is fir in the Random forest model which gives out a feature importance. A bar plot is generated to show which features are most important and which are least importance for an applicant to get approval for their credit card application 
11.	The model shows an accuracy of 87% which is pretty good and the confusion matrix shows that Out of 138 test samples, 74 applications were predicted to be approved. Out of which  66 were correctly predicted and 8 were predicted approved but were not approved.


