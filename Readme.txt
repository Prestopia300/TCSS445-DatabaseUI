-----------------------------------------------------------------------------------------------------
Project requirements:

This program was only tested on Windows, but may work for other operating systems

This program reqires Python 3. You can check your version using: 
python --version

To check pip:
pip -V


Tkinter and pyodbc is native to the initial python download, but if for some reason they are not downloaded you can execute the following comands

pyodbc:
pip install pyodbc

tkinter:
pip install tk

-----------------------------------------------------------------------------------------------------

Run Project:

To Run, go to cmd line in the project file, and run:
python Real_Estate_Database_UI.py

-----------------------------------------------------------------------------------------------------


Real Estate Database UI Architecture:

Startpage:

--|Scenario Button
----|City Button
-------|Q - Enter City
-------|Q - Show all Records
-------|Q - Delete All Cities
----|Country Button
-------|Q - Enter Country
-------|Q - Show all Records
-------|Q - Delete All Countries
----|StateOrProvince Button
-------|Q - Enter StateOrProvince
-------|Q - Show all Records
-------|Q - Delete All StateOrProvinces
----|Zipcode Button
-------|Q - Enter Zipcode
-------|Q - Show all Records
-------|Q - Delete All Zipcodes
----|Address Button
-------|Q - Enter Address
-------|Q - Show all Records
-------|Q - Delete All Addresses
----|Property Button
-------|Q - Enter Property 
-------|Q - Show all Records
-------|Q - Delete All Properties

--|Analitical Queries Button
----|Property Select/Delete Button
-------|Q's - Select Property with constraints
-------|Q - Delete Property with x PropertyID
----|Property_Address Button
-------|Q - Select Address of Property with x PropertyID
----|Property_Additional_Queries Button
-------|Q - Select all Properties with min # of Bedrooms x and min # of Bathrooms y
-------|Q - Select all Properties between min Square Meters x and max Square Meters y



