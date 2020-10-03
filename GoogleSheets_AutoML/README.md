## Mljar with Google Sheets
This tutorial will help you to use mljar automl with google sheets. Follow the steps below to configure Google Sheets API and train automl with your desired sheets data.
First of all, make sure that you have a google account. If you have a Google account, you can follow these steps to create a Google service account.

The dataset used here is from [kaggle credit card fraud data](https://www.kaggle.com/mlg-ulb/creditcardfraud)

### Configure Google API

#### Steps
- Go to the developer’s console.

![](https://user-images.githubusercontent.com/25312635/94990284-876a7180-0598-11eb-8d02-de28229eb2a3.png)

- Create a project

![](https://user-images.githubusercontent.com/25312635/94990340-ec25cc00-0598-11eb-9983-e75fa0618b68.png)

- In the searchbar, search for google sheets API and google drive API and enable both of them.


- Now that you have enabled the APIs, you can create credentials using service account.

![](https://user-images.githubusercontent.com/25312635/94990325-d4e6de80-0598-11eb-8cc7-53ce3595ee4b.png)

- Now, select Google Drive API in the type of API required question. We will be calling the API from a non UI based platform so select Other non-UI (e.g. cron job, daemon). Select the Application Data in the next question as we do not require any user data to run our application. And also we are not using any cloud-based compute engine for our application. Finally, click on the What credentials do I need? button.

![](https://user-images.githubusercontent.com/25312635/94990350-f778f780-0598-11eb-94c0-dda59d709780.png)

- Then, share the google spreadsheets with other people and provide permission like edit or view only. Similarly, we will provide access to our service account. We will give it the complete access so that we will be able to read as well as write the spreadsheets and download the JSON file of the credentials.

![](https://user-images.githubusercontent.com/25312635/94990357-0364b980-0599-11eb-8566-1b564fdb1af3.png)