# Web Based Query System

This application is web-based query system to search for API and Mashup services

## Features of the Application – 
   * User can search for APIs by keywords separated by comma (,). 
     The keywords will be searched against title, summary, and the description of the API service.
   * User can search for API using selected criteria like ID, rating, Tags, Updated Year, etc.
   * User can search for Mashups services by keywords separated by comma (,). 
     The keywords will be searched against title, summary, and the description of the API service.
   * User can search for Mashups using selected criteria like ID, rating, Tags, Updated Year, etc.

   
## Technical details of the application - 
   * The application contains 2 data sets in the DB, API_DATA and MASHUP_DATA. 
   * MongoDB is used as backend database.
   * Python and FastAPI is used to develop the web service and pyMongo is used to connect to the MongoDB.
        
      
 ## Structure and design of the code - 
   
   * The db_helper.py file contains all the helper function for database operations.
   * There are 4 endpoints - search APIs with criteria, search APIs with keywords, search Mashups with criteria and search Mashups with keywords.
   * For searching with keywords, bson regex is used to search for keywords.
   * Each keyword is searched against title, summary, and the description of the API service.
   * If there are multiple keywords, the results filtered will contain all the keywords but necessarily not in the same column.
   * For the criteria based searching, all the filled entries are searched and filtered information is written.
   * For rating, $lt, $gt tags of MongoDB is used to give better flexibility for the user.
## Installation

#### Requirements
 * fastapi==0.95.0
 * pandas==1.3.5
 * pymongo==4.3.3
 * uvicorn==0.21.1

     
## Usage


To start the web-services, please run the command - 
```python
    python app.py
```
    