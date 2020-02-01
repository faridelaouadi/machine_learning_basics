# machine_learning_basics
Python implementation of the algorithms covered in Coursera's ML course

Linear regression using scikitlearn
=================

see code in file "regression.py"
Steps I took
---

![](regression/pic.png)

1) Brought in the data set via quandl and cleaned it up to use features that provided valuable insight. I also created my own feature which i thought to be useful
2) Split the data into training and testing where testing was 20% of the data
3) Trained the Linear regression classifier provided in scikitlearn
4) Plotted results
5) Stored the model in a pickle file so i wouldn't have to retrain everytime i wanted to predict
6) Modified the code to load in pickle file instead of retrain.
