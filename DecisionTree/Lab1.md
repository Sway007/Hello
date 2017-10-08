# Homework Repo

Lab #1 Tree ModelsPre-Lab (20 points):

1. Familiarize yourself with the following materials including those equationsinvolved:

   1. 1)  Decision tree: https://en.wikipedia.org/wiki/Decision_tree
   2. 2)  ID3 algorithm: https://en.wikipedia.org/wiki/ID3_algorithm
   3. 3)  C4.5 algorithm: https://en.wikipedia.org/wiki/C4.5_algorithm

   Think over and answer the follow questions:

   1. 1)  what are the advantages and disadvantages of decision tree algorithms?
   2. 2)  what kind of problems could be solved by decision trees?
   3. 3)  how to generate a decision tree and how to overcome the over-fit problem?
   4. 4)  what is the computational complexity of the decision tree algorithm.

2. Read materials about random forest, such as:

   https://en.wikipedia.org/wiki/Random_forest

   please summarize the difference between random forest and decision tree.

3. When the features are continuous instead of discrete, how to select cut-points in

   decision trees?

4. Could a tree model be used for regression? How to implement the corresponding

   algorithm? Please compare two cases of regression and classification by using treemodels.

Laboratory Exercises:

1. Submit your Pre-Lab in Sakai.

2. Create decision tree through ID3 Algorithm，Dataset:lenses.txt

3. Change ID3 to C4.5

4. Create regression tree with dataset “train.txt”, and predict the value of “test.txt”.

   Permissible error:1, Minimum sample size allowed to cut:4

Look at the correlation coefficient to measure regression tree:numpy.corrcoef(pred,y,rowvar=0)

\5. Prune regression tree and compare with the tree model in 4.

Grading Guidelines:Your Lab report should include

\1. Introduction
\2. Procedures
\3. Results
\4. Conclusions (including trees described by text or figure)

Additional:

Risk varies widely from customer to customer, and a deep understanding of different risk factorshelps predict the likelihood and cost of insurance claims. The goal of this dataset is to betterpredict Bodily Injury Liability Insurance claim payments based on the characteristics of theinsured customer’s vehicle.

Many factors contribute to the frequency and severity of car accidents including how, where andunder what conditions people drive, as well as what they are driving.

Each row contains one year’s worth information for insured vehicles. Since the goal of thisdataset is to improve the ability to use vehicle characteristics to accurately predict insurance claimpayments, the response variable (dollar amount of claims experienced for that vehicle in that year)has been adjusted to control for known non-vehicle effects. Some non-vehicle characteristics(labeled as such in the data dictionary) are included in the set of independent variables. It isexpected that no “main effects” corresponding will be found for these non-vehicle variables, butthere may be interesting interactions with the vehicle variables.

Calendar_Year is the year that the vehicle was insured. Household_ID is a householdidentification number that allows year-to-year tracking of each household. Since a customer mayinsure multiple vehicles in one household, there may be multiple vehicles associated with eachhousehold identification number. "Vehicle" identifies these vehicles (but the same "Vehicle"number may not apply to the same vehicle from year to year). You also have the vehicle’s modelyear and a coded form of make (manufacturer), model, and submodel. The remaining columnscontain miscellaneous vehicle characteristics, as well as other characteristics associated with theinsurance policy. See the "data dictionary" (data_dictionary.txt) for additional information.

This dataset naturally contained some missing values. Records containing missing values havebeen removed from the test data set but not from the training dataset. You can make use of therecords with missing values, or completely ignore them if you wish. They are coded as "?".

There are two datasets to download: training data and test data. You will use the training dataset tobuild your model, and will submit predictions for the test dataset. The training data hasinformation from 2005-2007, while the test data has information from 2008 and 2009.

You could get this dataset from: https://www.kaggle.com/c/ClaimPredictionChallenge/data