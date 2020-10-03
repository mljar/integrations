## Mljar with Google Sheets
This tutorial will help you to use mljar automl with google sheets. Follow the steps below to configure Google Sheets API and train automl with your desired sheets data.
First of all, make sure that you have a google account. If you have a Google account, you can follow these steps to create a Google service account.

### Configure Google API

https://docs.google.com/spreadsheets/d/1FQfXNy-urtbs7xoenHwxDcsOk82x8jaIdNagdknK7dI/edit?usp=sharing


#### Steps
- Go to the developer’s console.
![]()
- Create a project
![]()
- In the searchbar, search for google sheets API and google drive API and enable both of them.
![]()
- Now that you have enabled the APIs, you can create credentials using service account.
![]()
- Now, select Google Drive API in the type of API required question. We will be calling the API from a non UI based platform so select Other non-UI (e.g. cron job, daemon). Select the Application Data in the next question as we do not require any user data to run our application. And also we are not using any cloud-based compute engine for our application. Finally, click on the What credentials do I need? button.
![]()
- Then, share the google spreadsheets with other people and provide permission like edit or view only. Similarly, we will provide access to our service account. We will give it the complete access so that we will be able to read as well as write the spreadsheets and download the JSON file of the credentials.
![]()