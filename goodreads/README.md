![alt text](https://s.gr-assets.com/assets/icons/goodreads_icon_100x100-4a7d81b31d932cfc0be621ee15a14e70.png)
# Rate a Read with goodreads

[Goodreads](https://www.goodreads.com) is a social cataloging website for people who love **Books**.Users can just sign up and then create a reading list or update the books they have read or currently reading or even write a review. They can also form their own groups of book suggestions, surveys, polls, blogs, and discussions.
<br><br> 
In this project, I will explore the different features extracted from Books and Authors to determine what makes a book popular or what are the determinants in a book which earns a good rating?
### Who can use this?
This project is a tool to any prospective writer who is planning to write a book.
<br>
Well, they say:
>*If you want to be a writer, you must do two things above all others: read a lot and write a lot* 

Sure!
<br>But in this age of Data, some science and some analysis can work as a magic!
### Where the Data comes from?
I am grabbing all the Book Details on Science Fiction and the corresponding Author Details from goodreads using an API.  
<br>
The first version of this tool is to search and explore the **"Science Fiction/Fantasy"** Genre. In the later versions, I intend to work on the genre as an input parameter and thus this tool will work for any genre or search keyword.
<br>
### What are the steps followed?
Let's divide the whole project in a few steps:
1. [Data Extraction and Load Database](https://github.com/Oindrila-Sen/Springboard/blob/master/Capstone1/goodreads/GoodReads_Data_Extraction_Load_Database.ipynb)
2. [Data Wrangling and Features Extraction](https://github.com/Oindrila-Sen/Springboard/blob/master/Capstone1/goodreads/GoodReads_Data_Wrangling.ipynb)
3. [Exploratory Data Analysis](https://github.com/Oindrila-Sen/Springboard/blob/master/Capstone1/goodreads/GoodReads_EDA.ipynb)
4. [Fit a Model to predict Average Rating of a book](https://github.com/Oindrila-Sen/Springboard/blob/master/Capstone1/goodreads/Goodreads_Fit_a_Model.ipynb)
### Conclusion
There is a popular saying:

>*It is far better to foresee even without certainty than not to foresee at all.*

Machine Learning Algorithms have evolved with time and made it possible to foresee future with more certainty. The Machine Learning approach involves learning from DATA by identifying patterns and thus using them to automatically make some predictions. 

In this project, I have used **Multivariate Regression Algorithms** to predict an Average Rating of a Book. Multiple regression analysis is a powerful technique used for predicting the unknown value of a variable from the known value of two or more variables(the predictors).

It is difficult to predict the exact rating of a book since a Book gains popularity over time and the Rating of a book gets better with time and with more readers. Keeping those constraints in mind, in this project, I have tried to explore different features which a Writer can consider checking out before launching a book on Scienec Fiction/Fantasy.

Thank You!
