# TCSS445-DatabaseUI
This is my final project for my Databases class. It uses MySQL for the database, and pythons tkinter library to create the UI. 
 
 
----------------------------------------------------------------------------------------------------- <br />
Project requirements: <br />
 
This program was only tested on Windows, but may work for other operating systems <br />
 
This program reqires Python 3. You can check your version using:  <br /><br />
python --version <br />
 
To check pip: <br />
pip -V <br />
 
 
Tkinter and pyodbc is native to the initial python download, but if for some reason they are not downloaded you can execute the following comands <br />
 
pyodbc: <br />
pip install pyodbc <br />
 
tkinter: <br />
pip install tk <br />
 
----------------------------------------------------------------------------------------------------- 
 
Run Project: <br />
 
To Run, go to cmd line in the project file, and run: <br />
python Real_Estate_Database_UI.py <br />
 
----------------------------------------------------------------------------------------------------- 
 
 
Real Estate Database UI Architecture: <br />
 
Startpage: <br />
 
--|Scenario Button <br />
----|City Button <br />
-------|Q - Enter City <br />
-------|Q - Show all Records <br />
-------|Q - Delete All Cities <br />
----|Country Button <br />
-------|Q - Enter Country <br />
-------|Q - Show all Records <br />
-------|Q - Delete All Countries <br />
----|StateOrProvince Button <br />
-------|Q - Enter StateOrProvince <br />
-------|Q - Show all Records <br />
-------|Q - Delete All StateOrProvinces <br />
----|Zipcode Button <br />
-------|Q - Enter Zipcode <br />
-------|Q - Show all Records <br />
-------|Q - Delete All Zipcodes <br />
----|Address Button <br />
-------|Q - Enter Address <br />
-------|Q - Show all Records <br />
-------|Q - Delete All Addresses <br />
----|Property Button <br />
-------|Q - Enter Property  <br />
-------|Q - Show all Records <br />
-------|Q - Delete All Properties <br />
 <br />
--|Analitical Queries Button <br />
----|Property Select/Delete Button <br />
-------|Q's - Select Property with constraints <br />
-------|Q - Delete Property with x PropertyID <br />
----|Property_Address Button <br />
-------|Q - Select Address of Property with x PropertyID <br />
----|Property_Additional_Queries Button <br />
-------|Q - Select all Properties with min # of Bedrooms x and min # of Bathrooms y <br />
-------|Q - Select all Properties between min Square Meters x and max Square Meters y <br />
 
 
