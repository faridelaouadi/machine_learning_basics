<details open>
<summary>Already open...</summary>

<p>...</p>
</details>  


[Linear regression using scikitlearn](/regression)
=================

![](regression/pic.png)

1) Brought in the data set via quandl and cleaned it up to use features that provided valuable insight. I also created my own feature which i thought to be useful
2) Split the data into training and testing where testing was 20% of the data
3) Trained the Linear regression classifier provided in scikitlearn
4) Plotted results
5) Stored the model in a pickle file so i wouldn't have to retrain everytime i wanted to predict
6) Modified the code to load in pickle file instead of retrain.

[Linear regression from scratch](/regression_from_scratch)
=================

![](regression_from_scratch/pic.png)

1) Got the formulas for needed to find the gradient and intercept and coded a function for it
2) Created 2 test arrays to use and plotted the data in matplotlib
3) Plotted the regression line to see if it fit the data
4) Coded a function for the coefficient of determination to see if our line fit the data well
