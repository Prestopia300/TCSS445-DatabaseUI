# Real Estate Database UI 
# This program can minipulate Various Tables in the Parsons_Preston_db, and retrieve information about Property data that may be useful to the user.
# A detailed description of the Real Estate Database UI Architecture can be found in the Readme.txt file.


import tkinter as tk
from tkinter import ttk
import pyodbc 


# connect to database
conx = pyodbc.connect("DRIVER={SQL SERVER};"
                      "SERVER=DESKTOP-983AIBU\SQLEXPRESS;"
                      "DATABASE=Parsons_Preston_db;"
                      "TRUSTED_CONNECTION=yes;")

# create cursor
cursor = conx.cursor()

# Database GUI
 
LARGEFONT =("Verdana", 35)
  
class tkinterApp(tk.Tk):
     
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
         
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a container
        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True)
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
  
        # initializing frames to an empty array
        self.frames = {} 
  
        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, ScenarioPage, AnaliticalQueryPage, City_Page, Country_Page, Zipcode_Page, Address_Page, StateOrProvince_Page, Property_Page, Property_Select_Delete, Property_Address, Property_Additional_Queries):
  
            frame = F(container, self)
  
            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(StartPage)
  
    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
  
# first window frame startpage
  
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # ----- Navigation Buttons -----
         
        # label of frame Layout 2
        label = ttk.Label(self, text ="Startpage", font = LARGEFONT)
         
        # putting the grid in its place by using
        # grid
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
  
        # ScenarioPage Button
        button1 = ttk.Button(self, text ="ScenarioPage",
                            command = lambda : controller.show_frame(ScenarioPage))
        # Place : Left #1
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)


        # AnaliticalQueryPage Button
        button2 = ttk.Button(self, text ="AnaliticalQueryPage",
                            command = lambda : controller.show_frame(AnaliticalQueryPage))
        # Place : Left #2
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)



        
      


class ScenarioPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # ----- Navigation Buttons -----
         
        # label of frame Layout 2
        label = ttk.Label(self, text ="ScenarioPage", font = LARGEFONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)

        # StartPage Button
        button1 = ttk.Button(self, text ="StartPage",
                            command = lambda : controller.show_frame(StartPage))
        # Place : Left #1 
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)


        # City Button 
        button2 = ttk.Button(self, text ="City",
                            command = lambda : controller.show_frame(City_Page))
        # Place : Left #2
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)


        # Country Button        
        button3 = ttk.Button(self, text ="Country",
                            command = lambda : controller.show_frame(Country_Page))
        # Place : Left #3
        button3.grid(row = 3, column = 1, padx = 10, pady = 10)


        # StateOrProvince Button        
        button4 = ttk.Button(self, text ="StateOrProvince",
                            command = lambda : controller.show_frame(StateOrProvince_Page))
        # Place : Left #4
        button4.grid(row = 4, column = 1, padx = 10, pady = 10)


        # Zipcode Button        
        button5 = ttk.Button(self, text ="Zipcode",
                            command = lambda : controller.show_frame(Zipcode_Page))
        # Place : Left #5
        button5.grid(row = 5, column = 1, padx = 10, pady = 10)


        # Address Button        
        button6 = ttk.Button(self, text ="Address",
                            command = lambda : controller.show_frame(Address_Page))
        # Place : Left #6
        button6.grid(row = 6, column = 1, padx = 10, pady = 10)


        # Property Button        
        button7 = ttk.Button(self, text ="Property",
                            command = lambda : controller.show_frame(Property_Page))
        # Place : Left #7
        button7.grid(row = 7, column = 1, padx = 10, pady = 10)



class AnaliticalQueryPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        # ----- Navigation Buttons -----

        # label of frame Layout 2
        label = ttk.Label(self, text ="AnaliticalQueryPage", font = LARGEFONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)

        # StartPage Button
        button1 = ttk.Button(self, text ="StartPage",
                            command = lambda : controller.show_frame(StartPage))
        # Place : Left #1 
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)


        # Property_Select_Delete Button
        button3 = ttk.Button(self, text ="Property Select/Delete",
                            command = lambda : controller.show_frame(Property_Select_Delete))
        # Place : Left #2
        button3.grid(row = 2, column = 1, padx = 10, pady = 10)

        # Property_Address Button
        button4 = ttk.Button(self, text ="Property_Address",
                            command = lambda : controller.show_frame(Property_Address))
        # Place : Left #3
        button4.grid(row = 3, column = 1, padx = 10, pady = 10)

         # Property_Additional_Queries Button
        button5 = ttk.Button(self, text ="Property_Additional_Queries",
                            command = lambda : controller.show_frame(Property_Additional_Queries))
        # Place : Left #3
        button5.grid(row = 4, column = 1, padx = 10, pady = 10)


# First Scenario Page (City Add, Select All, Delete All)
class City_Page(tk.Frame):
     
    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="City", font = LARGEFONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
  
        # ----- Navigation Buttons -----

        # StartPage Button
        button1 = ttk.Button(self, text ="StartPage",
                            command = lambda : controller.show_frame(StartPage))
        # Place : Left #1 
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
        
  
        # ScenarioPage Button
        button2 = ttk.Button(self, text ="ScenarioPage",
                            command = lambda : controller.show_frame(ScenarioPage))
        # Place : Left #2 
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)      
        
        # ----- Page Content Items -----

        # Create Text Boxes
        city_name = ttk.Entry(self, width=30)
        city_name.grid(row=2, column=4, padx=0)

        # Create Text Box Labels

        city_name_label = ttk.Label(self, text="City Name")
        city_name_label.grid(row=2, column=3, padx=0)

        # Create Submit Function For Database
        def submit():
            # connect to database
            conx = pyodbc.connect("DRIVER={SQL SERVER};"
                      "SERVER=DESKTOP-983AIBU\SQLEXPRESS;"
                      "DATABASE=Parsons_Preston_db;"
                      "TRUSTED_CONNECTION=yes;")

            # create cursor
            cursor = conx.cursor()

            cursor.execute("INSERT INTO Cities VALUES (?)",
                           city_name.get()
            )
            # Commit changes
            conx.commit()
            # Close connection
            conx.close()

            print('submitted city')

            # Clear the Text Boxes
            city_name.delete(0, 'end')
        
        # Create Query Function
        def query():
            # connect to database
            conx = pyodbc.connect("DRIVER={SQL SERVER};"
                      "SERVER=DESKTOP-983AIBU\SQLEXPRESS;"
                      "DATABASE=Parsons_Preston_db;"
                      "TRUSTED_CONNECTION=yes;")

            # create cursor
            cursor = conx.cursor()

            cursor.execute("SELECT * FROM Cities")
            records = cursor.fetchall()

            print_records = ''
            for record in records:
                print_records += str(record) + '\n'
            
            query_label = ttk.Label(self, text=print_records)
            query_label.grid(row= 4, column=4, columnspan=2)

            # Commit changes
            conx.commit()
            # Close connection
            conx.close()

        # Create Query Function
        def delete_all():
            # connect to database
            conx = pyodbc.connect("DRIVER={SQL SERVER};"
                      "SERVER=DESKTOP-983AIBU\SQLEXPRESS;"
                      "DATABASE=Parsons_Preston_db;"
                      "TRUSTED_CONNECTION=yes;")

            # create cursor
            cursor = conx.cursor()

            cursor.execute("""DELETE FROM Cities
                              DBCC CHECKIDENT('Cities', RESEED, 0)
                                """)
            
            # Commit changes
            conx.commit()
            # Close connection
            conx.close()

        # Create Submit Button
        submit_btn = ttk.Button(self, text="Enter", command=submit)
        submit_btn.grid(row=2, column=5, columnspan=2, pady=10, padx=10, ipadx=100)

        # Create Query Button
        query_btn = ttk.Button(self, text="Show Records", command=query)
        query_btn.grid(row=3, column=4, columnspan=2, pady=10, ipadx=137)

        # Create Delete Button
        delete_btn = ttk.Button(self, text='Delete All', command=delete_all)
        delete_btn.grid(row=3, column=6, columnspan=2, pady=10, ipadx=137)



# Scond Scenario Page (Country Add, Select All, Delete All)
class Country_Page(tk.Frame):
     
    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Countries", font = LARGEFONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
  
        # ----- Navigation Buttons -----

        # StartPage Button
        button1 = ttk.Button(self, text ="StartPage",
                            command = lambda : controller.show_frame(StartPage))
        # Place : Left #1
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)


        # ScenarioPage Button
        button2 = ttk.Button(self, text ="ScenarioPage",
                            command = lambda : controller.show_frame(ScenarioPage))
        # Place : Left #2
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)


        # ----- Page Content Items -----
        
        # Create Text Boxes
        country_code = ttk.Entry(self, width=30)
        country_code.grid(row=2, column=4, padx=0)
        country_name = ttk.Entry(self, width=30)
        country_name.grid(row=3, column=4, padx=0)

        # Create Text Box Labels
        country_code_label = ttk.Label(self, text="Country Code")
        country_code_label.grid(row=2, column=3, padx=0)
        country_name_label = ttk.Label(self, text="Country Name")
        country_name_label.grid(row=3, column=3, padx=0)
        
        # Create Submit Function For Database
        def submit():
            # connect to database
            conx = pyodbc.connect("DRIVER={SQL SERVER};"
                      "SERVER=DESKTOP-983AIBU\SQLEXPRESS;"
                      "DATABASE=Parsons_Preston_db;"
                      "TRUSTED_CONNECTION=yes;")

            # create cursor
            cursor = conx.cursor()

            cursor.execute("INSERT INTO Countries VALUES (?, ?)",
                           country_code.get(),
                           country_name.get()
            )
            # Commit changes
            conx.commit()
            # Close connection
            conx.close()

            print('submitted city')

            # Clear the Text Boxes
            country_code.delete(0, 'end')
            country_name.delete(0, 'end')
        
        # Create Query Function
        def query():
            # connect to database
            conx = pyodbc.connect("DRIVER={SQL SERVER};"
                      "SERVER=DESKTOP-983AIBU\SQLEXPRESS;"
                      "DATABASE=Parsons_Preston_db;"
                      "TRUSTED_CONNECTION=yes;")

            # create cursor
            cursor = conx.cursor()

            cursor.execute("SELECT * FROM Countries")
            records = cursor.fetchall()

            print_records = ''
            for record in records:
                print_records += str(record) + '\n'
            
            query_label = ttk.Label(self, text=print_records)
            query_label.grid(row= 5, column=4, columnspan=2)

            # Commit changes
            conx.commit()
            # Close connection
            conx.close()

        # Create Query Function
        def delete_all():
            # connect to database
            conx = pyodbc.connect("DRIVER={SQL SERVER};"
                      "SERVER=DESKTOP-983AIBU\SQLEXPRESS;"
                      "DATABASE=Parsons_Preston_db;"
                      "TRUSTED_CONNECTION=yes;")

            # create cursor
            cursor = conx.cursor()

            cursor.execute("""DELETE FROM Countries
                              DBCC CHECKIDENT('Countries', RESEED, 0)
                                """)
            
            # Commit changes
            conx.commit()
            # Close connection
            conx.close()

        # Create Submit Button
        submit_btn = ttk.Button(self, text="Enter", command=submit)
        submit_btn.grid(row=2, column=5, columnspan=2, pady=10, padx=10, ipadx=100)

        # Create Query Button
        query_btn = ttk.Button(self, text="Show Records", command=query)
        query_btn.grid(row=4, column=4, columnspan=2, pady=10, ipadx=137)

        # Create Delete Button
        delete_btn = ttk.Button(self, text='Delete All', command=delete_all)
        delete_btn.grid(row=4, column=6, columnspan=2, pady=10, ipadx=137)



# Third Scenario Page (StateOrProvinces Add, Select All, Delete All)
class StateOrProvince_Page(tk.Frame):
     
    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="StateOrProvinces", font = LARGEFONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
  
        # ----- Navigation Buttons -----

        # StartPage Button
        button1 = ttk.Button(self, text ="StartPage",
                            command = lambda : controller.show_frame(StartPage))
        # Place : Left #1
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)


        # ScenarioPage Button
        button2 = ttk.Button(self, text ="ScenarioPage",
                            command = lambda : controller.show_frame(ScenarioPage))
        # Place : Left #2
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)


        # ----- Page Content Items -----
        
        # Create Text Boxes
        StateOrProvinceCode = ttk.Entry(self, width=30)
        StateOrProvinceCode.grid(row=2, column=4, padx=0)
        StateOrProvinceName = ttk.Entry(self, width=30)
        StateOrProvinceName.grid(row=3, column=4, padx=0)

        # Create Text Box Labels
        StateOrProvinceCode_label = ttk.Label(self, text="StateOrProvinceCode")
        StateOrProvinceCode_label.grid(row=2, column=3, padx=0)
        StateOrProvinceName_label = ttk.Label(self, text="StateOrProvinceName")
        StateOrProvinceName_label.grid(row=3, column=3, padx=0)
        
        # Create Submit Function For Database
        def submit():
            # connect to database
            conx = pyodbc.connect("DRIVER={SQL SERVER};"
                      "SERVER=DESKTOP-983AIBU\SQLEXPRESS;"
                      "DATABASE=Parsons_Preston_db;"
                      "TRUSTED_CONNECTION=yes;")

            # create cursor
            cursor = conx.cursor()

            cursor.execute("INSERT INTO StateOrProvinces VALUES (?, ?)",
                           StateOrProvinceCode.get(),
                           StateOrProvinceName.get()
            )
            # Commit changes
            conx.commit()
            # Close connection
            conx.close()

            print('submitted city')

            # Clear the Text Boxes
            StateOrProvinceCode.delete(0, 'end')
            StateOrProvinceName.delete(0, 'end')
        
        # Create Query Function
        def query():
            # connect to database
            conx = pyodbc.connect("DRIVER={SQL SERVER};"
                      "SERVER=DESKTOP-983AIBU\SQLEXPRESS;"
                      "DATABASE=Parsons_Preston_db;"
                      "TRUSTED_CONNECTION=yes;")

            # create cursor
            cursor = conx.cursor()

            cursor.execute("SELECT * FROM StateOrProvinces")
            records = cursor.fetchall()

            print_records = ''
            for record in records:
                print_records += str(record) + '\n'
            
            query_label = ttk.Label(self, text=print_records)
            query_label.grid(row= 5, column=4, columnspan=2)

            # Commit changes
            conx.commit()
            # Close connection
            conx.close()

        # Create Query Function
        def delete_all():
            # connect to database
            conx = pyodbc.connect("DRIVER={SQL SERVER};"
                      "SERVER=DESKTOP-983AIBU\SQLEXPRESS;"
                      "DATABASE=Parsons_Preston_db;"
                      "TRUSTED_CONNECTION=yes;")

            # create cursor
            cursor = conx.cursor()

            cursor.execute("""DELETE FROM StateOrProvinces
                              DBCC CHECKIDENT('StateOrProvinces', RESEED, 0)
                                """)
            
            # Commit changes
            conx.commit()
            # Close connection
            conx.close()

        # Create Submit Button
        submit_btn = ttk.Button(self, text="Enter", command=submit)
        submit_btn.grid(row=2, column=5, columnspan=2, pady=10, padx=10, ipadx=100)

        # Create Query Button
        query_btn = ttk.Button(self, text="Show Records", command=query)
        query_btn.grid(row=4, column=4, columnspan=2, pady=10, ipadx=137)

        # Create Delete Button
        delete_btn = ttk.Button(self, text='Delete All', command=delete_all)
        delete_btn.grid(row=4, column=6, columnspan=2, pady=10, ipadx=137)


# Fourth Scenario Page (Zipcode Add, Select All, Delete All)
class Zipcode_Page(tk.Frame):
     
    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Zipcodes", font = LARGEFONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
  
        # ----- Navigation Buttons -----

        # StartPage Button
        button1 = ttk.Button(self, text ="StartPage",
                            command = lambda : controller.show_frame(StartPage))
        # Place : Left #1
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)


        # ScenarioPage Button
        button2 = ttk.Button(self, text ="ScenarioPage",
                            command = lambda : controller.show_frame(ScenarioPage))
        # Place : Left #2
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)


        # ----- Page Content Items -----
        
        # Create Text Boxes
        CountryID = ttk.Entry(self, width=30)
        CountryID.grid(row=2, column=4, padx=0)
        StateOrProvinceID = ttk.Entry(self, width=30)
        StateOrProvinceID.grid(row=3, column=4, padx=0)
        CityID = ttk.Entry(self, width=30)
        CityID.grid(row=4, column=4, padx=0)

        # Create Text Box Labels
        CountryID_label = ttk.Label(self, text="CountryID")
        CountryID_label.grid(row=2, column=3, padx=0)
        StateOrProvinceID_label = ttk.Label(self, text="StateOrProvinceID")
        StateOrProvinceID_label.grid(row=3, column=3, padx=0)
        CityID_label = ttk.Label(self, text="CityID")
        CityID_label.grid(row=4, column=3, padx=0, pady=15)
        
        # Create Submit Function For Database
        def submit():
            # connect to database
            conx = pyodbc.connect("DRIVER={SQL SERVER};"
                      "SERVER=DESKTOP-983AIBU\SQLEXPRESS;"
                      "DATABASE=Parsons_Preston_db;"
                      "TRUSTED_CONNECTION=yes;")

            # create cursor
            cursor = conx.cursor()

            cursor.execute("INSERT INTO ZipCodes VALUES (?, ?, ?)",
                           CountryID.get(),
                           StateOrProvinceID.get(),
                           CityID.get()
            )
            # Commit changes
            conx.commit()
            # Close connection
            conx.close()

            print('submitted city')

            # Clear the Text Boxes
            CountryID.delete(0, 'end')
            StateOrProvinceID.delete(0, 'end')
            CityID.delete(0, 'end')
        
        # Create Query Function
        def query():
            # connect to database
            conx = pyodbc.connect("DRIVER={SQL SERVER};"
                      "SERVER=DESKTOP-983AIBU\SQLEXPRESS;"
                      "DATABASE=Parsons_Preston_db;"
                      "TRUSTED_CONNECTION=yes;")

            # create cursor
            cursor = conx.cursor()

            cursor.execute("SELECT * FROM ZipCodes")
            records = cursor.fetchall()

            print_records = ''
            for record in records:
                print_records += str(record) + '\n'
            
            query_label = ttk.Label(self, text=print_records)
            query_label.grid(row= 6, column=4, columnspan=2)

            # Commit changes
            conx.commit()
            # Close connection
            conx.close()

        # Create Query Function
        def delete_all():
            # connect to database
            conx = pyodbc.connect("DRIVER={SQL SERVER};"
                      "SERVER=DESKTOP-983AIBU\SQLEXPRESS;"
                      "DATABASE=Parsons_Preston_db;"
                      "TRUSTED_CONNECTION=yes;")

            # create cursor
            cursor = conx.cursor()

            cursor.execute("""DELETE FROM ZipCodes
                              DBCC CHECKIDENT('ZipCodes', RESEED, 0)
                                """)
            
            # Commit changes
            conx.commit()
            # Close connection
            conx.close()

        # Create Submit Button
        submit_btn = ttk.Button(self, text="Enter", command=submit)
        submit_btn.grid(row=2, column=5, columnspan=2, pady=10, padx=10, ipadx=100)

        # Create Query Button
        query_btn = ttk.Button(self, text="Show Records", command=query)
        query_btn.grid(row=5, column=4, columnspan=2, pady=10, ipadx=137)

        # Create Delete Button
        delete_btn = ttk.Button(self, text='Delete All', command=delete_all)
        delete_btn.grid(row=5, column=6, columnspan=2, pady=10, ipadx=137)



# Fith Scenario Page (Address_Page Add, Select All, Delete All)
class Address_Page(tk.Frame):
     
    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Addresses", font = LARGEFONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
  
        # ----- Navigation Buttons -----

        # StartPage Button
        button1 = ttk.Button(self, text ="StartPage",
                            command = lambda : controller.show_frame(StartPage))
        # Place : Left #1
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)


        # ScenarioPage Button
        button2 = ttk.Button(self, text ="ScenarioPage",
                            command = lambda : controller.show_frame(ScenarioPage))
        # Place : Left #2
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)


        # ----- Page Content Items -----
        
        # Create Text Boxes
        AddressStreet = ttk.Entry(self, width=30)
        AddressStreet.grid(row=2, column=4, padx=0)
        AddressType = ttk.Entry(self, width=30)
        AddressType.grid(row=3, column=4, padx=0)
        ZipCodeID = ttk.Entry(self, width=30)
        ZipCodeID.grid(row=4, column=4, padx=0)

        # Create Text Box Labels
        AddressStreet_label = ttk.Label(self, text="AddressStreet")
        AddressStreet_label.grid(row=2, column=3, padx=0)
        AddressType_label = ttk.Label(self, text="AddressType")
        AddressType_label.grid(row=3, column=3, padx=0)
        ZipCodeID_label = ttk.Label(self, text="ZipCodeID")
        ZipCodeID_label.grid(row=4, column=3, padx=0, pady=15)
        
        # Create Submit Function For Database
        def submit():
            # connect to database
            conx = pyodbc.connect("DRIVER={SQL SERVER};"
                      "SERVER=DESKTOP-983AIBU\SQLEXPRESS;"
                      "DATABASE=Parsons_Preston_db;"
                      "TRUSTED_CONNECTION=yes;")

            # create cursor
            cursor = conx.cursor()

            cursor.execute("INSERT INTO Addresses VALUES (?, ?, ?)",
                           AddressStreet.get(),
                           AddressType.get(),
                           ZipCodeID.get()
            )
            # Commit changes
            conx.commit()
            # Close connection
            conx.close()

            print('submitted city')

            # Clear the Text Boxes
            AddressStreet.delete(0, 'end')
            AddressType.delete(0, 'end')
            ZipCodeID.delete(0, 'end')
        
        # Create Query Function
        def query():
            # connect to database
            conx = pyodbc.connect("DRIVER={SQL SERVER};"
                      "SERVER=DESKTOP-983AIBU\SQLEXPRESS;"
                      "DATABASE=Parsons_Preston_db;"
                      "TRUSTED_CONNECTION=yes;")

            # create cursor
            cursor = conx.cursor()
            cursor.execute("SELECT * FROM Addresses")
            records = cursor.fetchall()

            print_records = ''
            for record in records:
                print_records += str(record) + '\n'
            
            query_label = ttk.Label(self, text=print_records)
            query_label.grid(row= 6, column=4, columnspan=2)

            # Commit changes
            conx.commit()
            # Close connection
            conx.close()

        # Create Query Function
        def delete_all():
            # connect to database
            conx = pyodbc.connect("DRIVER={SQL SERVER};"
                      "SERVER=DESKTOP-983AIBU\SQLEXPRESS;"
                      "DATABASE=Parsons_Preston_db;"
                      "TRUSTED_CONNECTION=yes;")

            # create cursor
            cursor = conx.cursor()

            cursor.execute("""DELETE FROM Addresses
                              DBCC CHECKIDENT('Addresses', RESEED, 0)
                                """)
            
            # Commit changes
            conx.commit()
            # Close connection
            conx.close()

        # Create Submit Button
        submit_btn = ttk.Button(self, text="Enter", command=submit)
        submit_btn.grid(row=2, column=5, columnspan=2, pady=10, padx=10, ipadx=100)

        # Create Query Button
        query_btn = ttk.Button(self, text="Show Records", command=query)
        query_btn.grid(row=5, column=4, columnspan=2, pady=10, ipadx=137)

        # Create Delete Button
        delete_btn = ttk.Button(self, text='Delete All', command=delete_all)
        delete_btn.grid(row=5, column=6, columnspan=2, pady=10, ipadx=137)



# Sixth Scenario Page (Property_Page Add, Select All, Delete All)
class Property_Page(tk.Frame):
     
    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Properties", font = LARGEFONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 5)
  
        # ----- Navigation Buttons -----

        # StartPage Button
        button1 = ttk.Button(self, text ="StartPage",
                            command = lambda : controller.show_frame(StartPage))
        # Place : Left #1
        button1.grid(row = 1, column = 1, padx = 10, pady = 5)


        # ScenarioPage Button
        button2 = ttk.Button(self, text ="ScenarioPage",
                            command = lambda : controller.show_frame(ScenarioPage))
        # Place : Left #2
        button2.grid(row = 2, column = 1, padx = 10, pady = 5)


        # ----- Page Content Items -----
        
        # Create Text Boxes
        PropertyDateAdded = ttk.Entry(self, width=30)
        PropertyDateAdded.grid(row=2, column=4, padx=0)
        AddressID = ttk.Entry(self, width=30)
        AddressID.grid(row=3, column=4, padx=0)
        OwnerID = ttk.Entry(self, width=30)
        OwnerID.grid(row=4, column=4, padx=0)
        PropertyNumberOfRooms = ttk.Entry(self, width=30)
        PropertyNumberOfRooms.grid(row=5, column=4, padx=0)
        PropertyNumberOfBedRooms = ttk.Entry(self, width=30)
        PropertyNumberOfBedRooms.grid(row=6, column=4, padx=0)
        PropertyNumberOfBathRooms = ttk.Entry(self, width=30)
        PropertyNumberOfBathRooms.grid(row=7, column=4, padx=0)
        PropertySquareMeters = ttk.Entry(self, width=30)
        PropertySquareMeters.grid(row=8, column=4, padx=0)
        PropertyNumberOfGarages = ttk.Entry(self, width=30)
        PropertyNumberOfGarages.grid(row=9, column=4, padx=0)


        # Create Text Box Labels
        PropertyDateAdded_label = ttk.Label(self, text="PropertyDateAdded")
        PropertyDateAdded_label.grid(row=2, column=3, padx=0)
        AddressID_label = ttk.Label(self, text="AddressID")
        AddressID_label.grid(row=3, column=3, padx=0)
        OwnerID_label = ttk.Label(self, text="OwnerID")
        OwnerID_label.grid(row=4, column=3, padx=0, pady=5)
        PropertyNumberOfRooms_label = ttk.Label(self, text="PropertyNumberOfRooms")
        PropertyNumberOfRooms_label.grid(row=5, column=3, padx=0, pady=5)
        PropertyNumberOfBedRooms_label = ttk.Label(self, text="PropertyNumberOfBedRooms")
        PropertyNumberOfBedRooms_label.grid(row=6, column=3, padx=0, pady=5)
        PropertyNumberOfBathRooms_label = ttk.Label(self, text="PropertyNumberOfBathRooms")
        PropertyNumberOfBathRooms_label.grid(row=7, column=3, padx=0, pady=5)
        PropertySquareMeters_label = ttk.Label(self, text="PropertySquareMeters")
        PropertySquareMeters_label.grid(row=8, column=3, padx=0, pady=5)
        PropertyNumberOfGarages_label = ttk.Label(self, text="PropertyNumberOfGarages")
        PropertyNumberOfGarages_label.grid(row=9, column=3, padx=0, pady=5)


        
        # Create Submit Function For Database
        def submit():
            # connect to database
            conx = pyodbc.connect("DRIVER={SQL SERVER};"
                      "SERVER=DESKTOP-983AIBU\SQLEXPRESS;"
                      "DATABASE=Parsons_Preston_db;"
                      "TRUSTED_CONNECTION=yes;")

            # create cursor
            cursor = conx.cursor()

            cursor.execute("INSERT INTO Properties VALUES (?, ?, ?, ?, ?, ?, ?, ?)",                          
                            PropertyDateAdded.get(),
                            AddressID.get(),
                            OwnerID.get(),
                            PropertyNumberOfRooms.get(),
                            PropertyNumberOfBedRooms.get(),
                            PropertyNumberOfBathRooms.get(), 
                            PropertySquareMeters.get(), 
                            PropertyNumberOfGarages.get()
            )
            # Commit changes
            conx.commit()
            # Close connection
            conx.close()

            print('submitted city')

            # Clear the Text Boxes
            PropertyDateAdded.delete(0, 'end')
            AddressID.delete(0, 'end')
            OwnerID.delete(0, 'end')
            PropertyNumberOfRooms.delete(0, 'end')
            PropertyNumberOfBedRooms.delete(0, 'end')
            PropertyNumberOfBathRooms.delete(0, 'end')
            PropertySquareMeters.delete(0, 'end')
            PropertyNumberOfGarages.delete(0, 'end')

        
        # Create Query Function
        def query():
            # connect to database
            conx = pyodbc.connect("DRIVER={SQL SERVER};"
                      "SERVER=DESKTOP-983AIBU\SQLEXPRESS;"
                      "DATABASE=Parsons_Preston_db;"
                      "TRUSTED_CONNECTION=yes;")

            # create cursor
            cursor = conx.cursor()

            cursor.execute("SELECT * FROM Properties")
            records = cursor.fetchall()

            print_records = ''
            for record in records:
                print_records += str(record) + '\n'
            
            query_label = ttk.Label(self, text=print_records)
            query_label.grid(row= 13, column=4, columnspan=2)

            # Commit changes
            conx.commit()
            # Close connection
            conx.close()

        # Create Query Function
        def delete_all():
            # connect to database
            conx = pyodbc.connect("DRIVER={SQL SERVER};"
                      "SERVER=DESKTOP-983AIBU\SQLEXPRESS;"
                      "DATABASE=Parsons_Preston_db;"
                      "TRUSTED_CONNECTION=yes;")

            # create cursor
            cursor = conx.cursor()

            cursor.execute("""DELETE FROM Properties
                              DBCC CHECKIDENT('Properties', RESEED, 0)
                                """)
            
            # Commit changes
            conx.commit()
            # Close connection
            conx.close()

        # Create Submit Button
        submit_btn = ttk.Button(self, text="Enter", command=submit)
        submit_btn.grid(row=2, column=5, columnspan=2, pady=10, padx=10, ipadx=100)

        # Create Query Button
        query_btn = ttk.Button(self, text="Show Records", command=query)
        query_btn.grid(row=12, column=4, columnspan=2, pady=10, ipadx=137)

        # Create Delete Button
        delete_btn = ttk.Button(self, text='Delete All', command=delete_all)
        delete_btn.grid(row=12, column=6, columnspan=2, pady=10, ipadx=137)



# First Anallitical Query Page (Property Info Query)
# Can select any column to narrow down selection of properties
# Thus the new name is Property Narrow Donw / Delete Property Based on ID
class Property_Select_Delete(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Property Selection/\n             Deletion", font = LARGEFONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
        
         # ----- Navigation Buttons -----

        # StartPage Button
        button1 = ttk.Button(self, text ="StartPage",
                            command = lambda : controller.show_frame(StartPage))
        # Place : Left #1
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
        

        # AnaliticalQueryPage Button
        button2 = ttk.Button(self, text ="AnaliticalQueryPage",
                            command = lambda : controller.show_frame(AnaliticalQueryPage))
        # Place : Left #2
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)

# 1000 lines - Wow! *winks, then disapears (not part of code ;)
         # Create Text Boxes
        PropertyDateAdded = ttk.Entry(self, width=30)
        PropertyDateAdded.grid(row=2, column=4, padx=0)

        AddressID = ttk.Entry(self, width=30)
        AddressID.grid(row=3, column=4, padx=0)
        OwnerID = ttk.Entry(self, width=30)
        OwnerID.grid(row=4, column=4, padx=0)
        PropertyNumberOfRooms = ttk.Entry(self, width=30)
        PropertyNumberOfRooms.grid(row=5, column=4, padx=0)

        PropertyNumberOfRooms = ttk.Entry(self, width=30)
        PropertyNumberOfRooms.grid(row=5, column=4, padx=0)
        PropertyNumberOfBedRooms = ttk.Entry(self, width=30)
        PropertyNumberOfBedRooms.grid(row=6, column=4, padx=0)
        PropertyNumberOfBathRooms = ttk.Entry(self, width=30)
        PropertyNumberOfBathRooms.grid(row=7, column=4, padx=0)
        PropertySquareMeters = ttk.Entry(self, width=30)
        PropertySquareMeters.grid(row=8, column=4, padx=0)
        PropertyNumberOfGarages = ttk.Entry(self, width=30)
        PropertyNumberOfGarages.grid(row=9, column=4, padx=0)

        DeletePropertyID = ttk.Entry(self, width=30)
        DeletePropertyID.grid(row=9, column=5, padx=0)


        # Create Text Box Labels
        PropertyDateAdded_label = ttk.Label(self, text="PropertyDateAdded")
        PropertyDateAdded_label.grid(row=2, column=3, padx=0)

        AddressID_label = ttk.Label(self, text="AddressID")
        AddressID_label.grid(row=3, column=3, padx=0)
        OwnerID_label = ttk.Label(self, text="OwnerID")
        OwnerID_label.grid(row=4, column=3, padx=0, pady=5)
        PropertyNumberOfRooms_label = ttk.Label(self, text="PropertyNumberOfRooms")
        PropertyNumberOfRooms_label.grid(row=5, column=3, padx=0, pady=5)

        PropertyNumberOfBedRooms_label = ttk.Label(self, text="PropertyNumberOfBedRooms")
        PropertyNumberOfBedRooms_label.grid(row=6, column=3, padx=0, pady=5)
        PropertyNumberOfBathRooms_label = ttk.Label(self, text="PropertyNumberOfBathRooms")
        PropertyNumberOfBathRooms_label.grid(row=7, column=3, padx=0, pady=5)
        PropertySquareMeters_label = ttk.Label(self, text="PropertySquareMeters")
        PropertySquareMeters_label.grid(row=8, column=3, padx=0, pady=5)
        PropertyNumberOfGarages_label = ttk.Label(self, text="PropertyNumberOfGarages")
        PropertyNumberOfGarages_label.grid(row=9, column=3, padx=0, pady=5)


        DeletePropertyID_label = ttk.Label(self, text="DeletePropertyID")
        DeletePropertyID_label.grid(row=8, column=5, padx=0)
       
        # NEW PLAN FOR IMPLIMENTATION:
            # check if empty,
            # if yes, then str var = 'WHERE column is not null
            # if no, then str var = where column IN (?)
       
        # Create Query Function
        def query_specific():
            # connect to database
            conx = pyodbc.connect("DRIVER={SQL SERVER};"
                    "SERVER=DESKTOP-983AIBU\SQLEXPRESS;"
                    "DATABASE=Parsons_Preston_db;"
                    "TRUSTED_CONNECTION=yes;")

            # create cursor
            cursor = conx.cursor()

            # Initialize Inputs and Queries

            # Columns w/ Input data
            filled_arr = [0,0,0,0,0,0,0,0]

            # Inputs
            g1 = PropertyDateAdded.get()
            g2 = AddressID.get()
            g3 = OwnerID.get()
            g4 = PropertyNumberOfRooms.get()
            g5 = PropertyNumberOfBedRooms.get()
            g6 = PropertyNumberOfBathRooms.get()
            g7 = PropertySquareMeters.get()
            g8 = PropertyNumberOfGarages.get()

            value_arr = [g1, g2, g3, g4, g5, g6, g7, g8]

            # Queries
            q1 = "PropertyDateAdded IS NOT NULL"
            q2 = "AddressID IS NOT NULL"
            q3 = "OwnerID IS NOT NULL"
            q4 = "PropertyNumberOfRooms IS NOT NULL"
            q5 = "PropertyNumberOfBedRooms IS NOT NULL"
            q6 = "PropertyNumberOfBathRooms IS NOT NULL"
            q7 = "PropertySquareMeters IS NOT NULL"
            q8 = "PropertyNumberOfGarages IS NOT NULL"

            query_arr = [q1, q2, q3, q4, q5, q6, q7, q8]


            # Checks Entities for Data Input
            if len(PropertyDateAdded.get()) != 0:
                filled_arr[0] = 1
                query_arr[0] = "PropertyDateAdded IN (?)"

            if len(AddressID.get()) != 0:
                filled_arr[1] = 1
                query_arr[1] = "AddressID IN (?)"

            if len(OwnerID.get()) != 0:
                filled_arr[2] = 1
                query_arr[2] = "OwnerID IN (?)"

            if len(PropertyNumberOfRooms.get()) != 0:
                filled_arr[3] = 1
                query_arr[3] = "PropertyNumberOfRooms IN (?)"

            if len(PropertyNumberOfBedRooms.get()) != 0:
                filled_arr[4] = 1
                query_arr[4] = "PropertyNumberOfBedRooms IN (?)"

            if len(PropertyNumberOfBathRooms.get()) != 0:
                filled_arr[5] = 1
                query_arr[5] = "PropertyNumberOfBathRooms IN (?)"

            if len(PropertySquareMeters.get()) != 0:
                filled_arr[6] = 1
                query_arr[6] = "PropertySquareMeters IN (?)"

            # If User Input
            if len(PropertyNumberOfGarages.get()) != 0:
                # Update filled_arr
                filled_arr[7] = 1
                # Update Query command
                query_arr[7] = "PropertyNumberOfGarages IN (?)"

            
            # Count is the number of colums that contain user input
            # v_arr is/are the values from user input
            count = 0
            v_arr = []

            i = 0
            for num in filled_arr:
                if num == 1:
                    count += 1
                    v_arr.append(value_arr[i])
                i += 1
            # print(filled_arr)

            # Executes Query, with specific # of inputs
            # My first attempt involved using WHERE column_name IN (?), 
            # but ? cannot be a list, so I did this instead.

            v_and = " and "
            
            # 0 Values Inputted
            if count == 0:
                cursor.execute("SELECT * FROM Properties WHERE " 
                                + query_arr[0] + v_and + query_arr[1] + v_and + query_arr[2] + v_and + query_arr[3] + v_and 
                                + query_arr[4] + v_and + query_arr[5] + v_and + query_arr[6] + v_and + query_arr[7]
                                 )
            # 1 Value Inputted                     
            elif count == 1:
                cursor.execute("SELECT * FROM Properties WHERE " 
                                + query_arr[0] + v_and + query_arr[1] + v_and + query_arr[2] + v_and + query_arr[3] + v_and 
                                + query_arr[4] + v_and + query_arr[5] + v_and + query_arr[6] + v_and + query_arr[7],
                                v_arr[0]
                                 )
            # 2 Values Inputted                     
            elif count == 2:
                cursor.execute("SELECT * FROM Properties WHERE " 
                                + query_arr[0] + v_and + query_arr[1] + v_and + query_arr[2] + v_and + query_arr[3] + v_and 
                                + query_arr[4] + v_and + query_arr[5] + v_and + query_arr[6] + v_and + query_arr[7],
                                v_arr[0], v_arr[1]
                                 )
            # 3 Values Inputted
            elif count == 3:
                cursor.execute("SELECT * FROM Properties WHERE " 
                                + query_arr[0] + v_and + query_arr[1] + v_and + query_arr[2] + v_and + query_arr[3] + v_and 
                                + query_arr[4] + v_and + query_arr[5] + v_and + query_arr[6] + v_and + query_arr[7],
                                v_arr[0], v_arr[1], v_arr[2]
                                 )
            # 4 Values Inputted
            elif count == 4:
                cursor.execute("SELECT * FROM Properties WHERE " 
                                + query_arr[0] + v_and + query_arr[1] + v_and + query_arr[2] + v_and + query_arr[3] + v_and 
                                + query_arr[4] + v_and + query_arr[5] + v_and + query_arr[6] + v_and + query_arr[7],
                                v_arr[0], v_arr[1], v_arr[2], v_arr[3]
                                 )
            # 5 Values Inputted
            elif count == 5:
                cursor.execute("SELECT * FROM Properties WHERE " 
                                + query_arr[0] + v_and + query_arr[1] + v_and + query_arr[2] + v_and + query_arr[3] + v_and 
                                + query_arr[4] + v_and + query_arr[5] + v_and + query_arr[6] + v_and + query_arr[7],
                                v_arr[0], v_arr[1], v_arr[2], v_arr[3], v_arr[4]
                                 )
            # 6 Values Inputted
            elif count == 6:
                cursor.execute("SELECT * FROM Properties WHERE " 
                                + query_arr[0] + v_and + query_arr[1] + v_and + query_arr[2] + v_and + query_arr[3] + v_and 
                                + query_arr[4] + v_and + query_arr[5] + v_and + query_arr[6] + v_and + query_arr[7],
                                v_arr[0], v_arr[1], v_arr[2], v_arr[3], v_arr[4], v_arr[5]
                                 )
            # 7 Values Inputted
            elif count == 7:
                cursor.execute("SELECT * FROM Properties WHERE " 
                                + query_arr[0] + v_and + query_arr[1] + v_and + query_arr[2] + v_and + query_arr[3] + v_and 
                                + query_arr[4] + v_and + query_arr[5] + v_and + query_arr[6] + v_and + query_arr[7],
                                v_arr[0], v_arr[1], v_arr[2], v_arr[3], v_arr[4], v_arr[5], v_arr[6]
                                 )
            # 8 Values Inputted
            elif count == 8:
                cursor.execute("SELECT * FROM Properties WHERE " 
                                + query_arr[0] + v_and + query_arr[1] + v_and + query_arr[2] + v_and + query_arr[3] + v_and 
                                + query_arr[4] + v_and + query_arr[5] + v_and + query_arr[6] + v_and + query_arr[7],
                                v_arr[0], v_arr[1], v_arr[2], v_arr[3], v_arr[4], v_arr[5], v_arr[6], v_arr[7]
                                 )

            # fetches executed SELECT query
            records = cursor.fetchall()

            # prints record to a Label
            print_records = ''
            for record in records:
                print_records += str(record) + '\n'
            
            query_label = ttk.Label(self, text=print_records)
            query_label.grid(row= 13, column=4, columnspan=2)

            # Commit changes
            conx.commit()
            # Close connection
            conx.close()

        # Create Query Function
        def delete_prop():
            # connect to database
            conx = pyodbc.connect("DRIVER={SQL SERVER};"
                      "SERVER=DESKTOP-983AIBU\SQLEXPRESS;"
                      "DATABASE=Parsons_Preston_db;"
                      "TRUSTED_CONNECTION=yes;")

            # create cursor
            cursor = conx.cursor()

            cursor.execute("""DELETE FROM Properties WHERE ID = (?)""",
                                DeletePropertyID.get()
            )
            cursor.execute("""  declare @max int
                                select @max=max([ID]) from [Properties]
                                if @max IS NULL   --check when max is returned as null
                                  SET @max = 0 
            
                                DBCC CHECKIDENT('Properties', RESEED, @max)                                 
                                """)
            
            # Commit changes
            conx.commit()
            # Close connection
            conx.close()

        # Create Query Button
        query_btn = ttk.Button(self, text="Show Records", command=query_specific)
        query_btn.grid(row=12, column=4,  ipadx=70)

        # Create Delete Button
        delete_btn = ttk.Button(self, text='Delete Property', command=delete_prop)
        delete_btn.grid(row=12, column=5, columnspan=1, pady=10, ipadx=0)



# Second Anallitical Query Page (Property Address Query)
# Can select any PropertyID, which returns the address in the correct format
class Property_Address(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Property Address\n           Selection", font = LARGEFONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
        
         # ----- Navigation Buttons -----

        # StartPage Button
        button1 = ttk.Button(self, text ="StartPage",
                            command = lambda : controller.show_frame(StartPage))
        # Place : Left #1
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
        

        # AnaliticalQueryPage Button
        button2 = ttk.Button(self, text ="AnaliticalQueryPage",
                            command = lambda : controller.show_frame(AnaliticalQueryPage))
        # Place : Left #2
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)

        # -------- Button/Label/Entry SQL Query Code --------

        # Create Text Boxes
        AddressID = ttk.Entry(self, width=30)
        AddressID.grid(row=1, column=4, padx=0)


        # Create Text Box Labels
        AddressID_label = ttk.Label(self, text="Address of PropertyID")
        AddressID_label.grid(row=1, column=3, padx=0)
        
       
        # NEW PLAN FOR IMPLIMENTATION:
            # check if empty,
            # if yes, then str var = 'WHERE column is not null
            # if no, then str var = where column IN (?)
       
        # Create Query Function
        def query_address():
            # connect to database
            conx = pyodbc.connect("DRIVER={SQL SERVER};"
                    "SERVER=DESKTOP-983AIBU\SQLEXPRESS;"
                    "DATABASE=Parsons_Preston_db;"
                    "TRUSTED_CONNECTION=yes;")

            # create cursor
            cursor = conx.cursor()

            cursor.execute("""
                            SELECT SP.StateOrProvinceCode, A.AddressStreet, A.AddressType, CI.CityName, CO.CountryName
                            FROM Addresses A JOIN ZipCodes ZC
                            ON A.ZipCodeID = ZC.ID
                            inner JOIN Cities CI
                            ON ZC.CityID = CI.ID
                            inner JOIN Countries CO
                            ON ZC.CountryID = CO.ID
                            inner JOIN StateOrProvinces SP
                            ON ZC.StateOrProvinceID = SP.ID
                            WHERE A.ID = 
                            (                            
                            SELECT AddressID 
                            FROM Properties 
                            WHERE AddressID = (?)
                            )
                            """,
                          AddressID.get()
                        )


            # fetches executed SELECT query
            records = cursor.fetchall()
            
            print_records = ''
            # no items returned
            if len(records) == 0:
                print_records = "No Items Returned" 
            # items returned
            else:
                for record in records:
                    print_records += str(record) + '\n'
            
            query_label = ttk.Label(self, text=print_records)
            query_label.grid(row= 7, column=4, columnspan=2)

            # Commit changes
            conx.commit()
            # Close connection
            conx.close()

        # Create Query Button
        query_btn = ttk.Button(self, text="Show Records", command=query_address)
        query_btn.grid(row=3, column=4,  ipadx=70)


# Third Anallitical Query Page (Property Additional Queries)
# There are 2 Queries:
# Select Properties with i minimum of x bed rooms and y bathrooms
# Select properties with a PropertySquareMeters between x and y

class Property_Additional_Queries(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Property Q2", font = LARGEFONT) # min bed/bath rooms, PropertySquareMeters between x and 
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
        
         # ----- Navigation Buttons -----

        # StartPage Button
        button1 = ttk.Button(self, text ="StartPage",
                            command = lambda : controller.show_frame(StartPage))
        # Place : Left #1
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
        

        # AnaliticalQueryPage Button
        button2 = ttk.Button(self, text ="AnaliticalQueryPage",
                            command = lambda : controller.show_frame(AnaliticalQueryPage))
        # Place : Left #2
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)

        # -------- Button/Label/Entry SQL Query Code --------

        # Create Text Boxes
        PropertyNumberOfBedRooms = ttk.Entry(self, width=30)
        PropertyNumberOfBedRooms.grid(row=2, column=4, padx=0)
        PropertyNumberOfBathRooms = ttk.Entry(self, width=30)
        PropertyNumberOfBathRooms.grid(row=3, column=4, padx=0)
        
        PropertySquareMeters_min = ttk.Entry(self, width=30)
        PropertySquareMeters_min.grid(row=2, column=6, padx=0)
        PropertySquareMeters_max = ttk.Entry(self, width=30)
        PropertySquareMeters_max.grid(row=3, column=6, padx=0)


        # Create Text Box Labels
        PropertyNumberOfBedRooms_label = ttk.Label(self, text="PropertyNumberOfBedRooms Min")
        PropertyNumberOfBedRooms_label.grid(row=2, column=3, padx=0, pady=5)
        PropertyNumberOfBathRooms_label = ttk.Label(self, text="PropertyNumberOfBathRooms Min")
        PropertyNumberOfBathRooms_label.grid(row=3, column=3, padx=0, pady=5)

        PropertySquareMeters_min_label = ttk.Label(self, text="PropertySquareMeters Min")
        PropertySquareMeters_min_label.grid(row=2, column=5, padx=0, pady=5)
        PropertySquareMeters_max_label = ttk.Label(self, text="PropertySquareMeters Max")
        PropertySquareMeters_max_label.grid(row=3, column=5, padx=0, pady=5)

        first_query_label = ttk.Label(self, text="All Properties with min\n# of Bed/Bath rooms")
        first_query_label.grid(row=1, column=4, padx=0, pady=5)

        first_query_label = ttk.Label(self, text="All Properties between \nmin/max sq meters")
        first_query_label.grid(row=1, column=6, padx=0, pady=5)
        
        
        # Create Query Function
        def query_min_bedroom_bathroom_num():
            # connect to database
            conx = pyodbc.connect("DRIVER={SQL SERVER};"
                    "SERVER=DESKTOP-983AIBU\SQLEXPRESS;"
                    "DATABASE=Parsons_Preston_db;"
                    "TRUSTED_CONNECTION=yes;")

            # create cursor
            cursor = conx.cursor()

            bed_r = PropertyNumberOfBedRooms.get()
            bath_r = PropertyNumberOfBathRooms.get()

            # Checks if both Entries are Numerical
            bed_r_numerical = True
            bath_r_numerical = True
            
            try:
                x = int(bed_r)
            except ValueError:
                bed_r_numerical = False

            try:
                x = int(bath_r)
            except ValueError:
                bath_r_numerical = False

            # Execute Query if both Values are Int
            error_msg = ''
            query_executed = False
            if bed_r_numerical == True and bath_r_numerical == True and len(bed_r) > 0 and len(bath_r) > 0:
                cursor.execute("""
                                SELECT *
                                FROM Properties
                                WHERE PropertyNumberOfBedRooms >= ? 
                                and PropertyNumberOfBathRooms >= ?
                                """,
                                PropertyNumberOfBedRooms.get(),
                                PropertyNumberOfBathRooms.get()
                            )
                query_executed = True
            # Both are not Int, Prepare Error Msg
            else:
                error_msg = "Both bed and bath inputs are not numerical"



            # Fetches query data (nothing if no query executed) (nothing if no properties fit the requirements)
            records = ''
            if query_executed == True:
                records = cursor.fetchall()
            
            # Prepare output str
            print_records = ''
            
            # Set Output to error
            if len(records) == 0:
                if error_msg == '':
                    print_records = "No Items Returned" 
                else:
                    print_records = error_msg
            # Set output to Properties found
            else:
                for record in records:
                    print_records += str(record) + '\n'
            
            # Output struct
            query_label = ttk.Label(self, text=print_records)
            query_label.grid(row= 6, column=4, columnspan=1)

            # Commit changes
            conx.commit()
            # Close connection
            conx.close()

        # Create Query Button
        query_btn = ttk.Button(self, text="Show Records", command=query_min_bedroom_bathroom_num)
        query_btn.grid(row=4, column=4,  ipadx=70)



        # Create Query Function
        def query_PropertySquareMeters_between_x_and_y():
            # connect to database
            conx = pyodbc.connect("DRIVER={SQL SERVER};"
                    "SERVER=DESKTOP-983AIBU\SQLEXPRESS;"
                    "DATABASE=Parsons_Preston_db;"
                    "TRUSTED_CONNECTION=yes;")

            # create cursor
            cursor = conx.cursor()


            prop_sq_met_min = PropertySquareMeters_min.get()
            prop_sq_met_max = PropertySquareMeters_max.get()

            # check if bed and bath inputs are numerical
            prop_sq_met_min_numerical = True
            prop_sq_met_max_numerical = True
            try:
                x = int(prop_sq_met_min)
            except ValueError:
                prop_sq_met_min_numerical = False

            try:
                x = int(prop_sq_met_max)
            except ValueError:
                prop_sq_met_max_numerical = False

            # Execute Query if both Values are Int
            error_msg = ''
            query_executed = False
            if prop_sq_met_min_numerical == True and prop_sq_met_max_numerical == True and len(prop_sq_met_min) > 0 and len(prop_sq_met_max) > 0:
                query_executed = True
                cursor.execute("""
                                SELECT *
                                FROM Properties
                                WHERE PropertySquareMeters between ? and ?
                                """,
                                prop_sq_met_min,
                                prop_sq_met_max
                            )
            else:
                error_msg = "Both min and max inputs are not numerical"


            # Fetches query data (nothing if no query executed) (nothing if no properties fit the requirements)
            records = ''
            
            if query_executed == True:
                records = cursor.fetchall()
            
            # Prepare output str
            print_records = ''
            
            # Set Output to error
            if len(records) == 0:
                if error_msg == '':
                    print_records = "No Items Returned" 
                else:
                    print_records = error_msg
            # Set output to Properties found
            else:
                for record in records:
                    print_records += str(record) + '\n'
            
            # Output struct
            query_label = ttk.Label(self, text=print_records)
            query_label.grid(row= 6, column=6, columnspan=1)

            # Commit changes
            conx.commit()
            # Close connection
            conx.close()

        # Create Query Button
        query_btn = ttk.Button(self, text="Show Records", command=query_PropertySquareMeters_between_x_and_y)
        query_btn.grid(row=4, column=6,  ipadx=70)




# Driver Code
app = tkinterApp()
app.title('Database UI')
app.geometry("990x600")
app.mainloop()

conx.close()