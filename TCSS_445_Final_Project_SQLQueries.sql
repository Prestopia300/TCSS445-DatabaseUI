
/* My code is different from these queries, due to them being created outside of SQL, 
and take in user input, 
so what I've done is fill the user input parts with example inputs.

*/


/* ------------------------- Scenario Queries ------------------------- */


/* City Page */
SELECT * FROM Cities


INSERT INTO Cities VALUES ('Lake stevens')


DELETE FROM Cities
DBCC CHECKIDENT('Cities', RESEED, 0)

/* Country Page */

INSERT INTO Countries VALUES (12345, 'United States of America')
SELECT * FROM Countries


DELETE FROM Countries
DBCC CHECKIDENT('Countries', RESEED, 0)

/* StateOrProvidence Page */
INSERT INTO StateOrProvinces VALUES (54321, 'Washington')


SELECT * FROM StateOrProvinces


DELETE FROM StateOrProvinces
DBCC CHECKIDENT('StateOrProvinces', RESEED, 0)

/* ZipCode Page */
INSERT INTO ZipCodes VALUES (1, 1, 1)


SELECT * FROM ZipCodes


DELETE FROM ZipCodes
DBCC CHECKIDENT('ZipCodes', RESEED, 0)

/* Address Page */
INSERT INTO Addresses VALUES ('23rd', 'St', 1)


SELECT * FROM Addresses


DELETE FROM Addresses
DBCC CHECKIDENT('Addresses', RESEED, 0)

/* Property Page */
INSERT INTO Properties VALUES ('2000-01-01', 1, 1, 13, 2, 5, 12352, 3)


SELECT * FROM Properties


DELETE FROM Properties
DBCC CHECKIDENT('Properties', RESEED, 0)




/* ------------------------- Analitical Queries ------------------------- */



/* Property_Select_Delete Page */

/* The way I wrote this code, the amount of SQL queries would total up to 81
The code allows the user to put input into 0-8 of the Property columns in any order, 
and all properties that meet those requirements are returned, 
where unfilled properties are checked if the element in the database is null, effectively allowing all of that column in the final selection

Instead of showing all the queries, I will show 9.
*/

/* #1 */
SELECT * FROM Properties WHERE  
PropertyDateAdded IS NOT NULL
and AddressID IS NOT NULL
and OwnerID IS NOT NULL
and PropertyNumberOfRooms IS NOT NULL
and PropertyNumberOfBedRooms IS NOT NULL
and PropertyNumberOfBathRooms IS NOT NULL
and PropertySquareMeters IS NOT NULL
and PropertyNumberOfGarages IS NOT NULL;

/* #2 */
SELECT * FROM Properties WHERE 
PropertyDateAdded IN ('2000-01-01')
and AddressID IS NOT NULL
and OwnerID IS NOT NULL
and PropertyNumberOfRooms IS NOT NULL
and PropertyNumberOfBedRooms IS NOT NULL
and PropertyNumberOfBathRooms IS NOT NULL
and PropertySquareMeters IS NOT NULL
and PropertyNumberOfGarages IS NOT NULL;

/* #3 */
SELECT * FROM Properties WHERE 
PropertyDateAdded IN ('2000-01-01')
and AddressID IN (1)
and OwnerID IS NOT NULL
and PropertyNumberOfRooms IS NOT NULL
and PropertyNumberOfBedRooms IS NOT NULL
and PropertyNumberOfBathRooms IS NOT NULL
and PropertySquareMeters IS NOT NULL
and PropertyNumberOfGarages IS NOT NULL;

/* #4 */
SELECT * FROM Properties WHERE 
PropertyDateAdded IN ('2000-01-01')
and AddressID IN (1)
and OwnerID IN (1)
and PropertyNumberOfRooms IS NOT NULL
and PropertyNumberOfBedRooms IS NOT NULL
and PropertyNumberOfBathRooms IS NOT NULL
and PropertySquareMeters IS NOT NULL
and PropertyNumberOfGarages IS NOT NULL;

/* #5 */
SELECT * FROM Properties WHERE 
PropertyDateAdded IN ('2000-01-01')
and AddressID IN (1)
and OwnerID IN (1)
and PropertyNumberOfRooms IN (13)
and PropertyNumberOfBedRooms IS NOT NULL
and PropertyNumberOfBathRooms IS NOT NULL
and PropertySquareMeters IS NOT NULL
and PropertyNumberOfGarages IS NOT NULL;

/* #6 */
SELECT * FROM Properties WHERE 
PropertyDateAdded IN ('2000-01-01')
and AddressID IN (1)
and OwnerID IN (1)
and PropertyNumberOfRooms IN (13)
and PropertyNumberOfBedRooms IN (2)
and PropertyNumberOfBathRooms IS NOT NULL
and PropertySquareMeters IS NOT NULL
and PropertyNumberOfGarages IS NOT NULL;

/* #7 */
SELECT * FROM Properties WHERE 
PropertyDateAdded IN ('2000-01-01')
and AddressID IN (1)
and OwnerID IN (1)
and PropertyNumberOfRooms IN (13)
and PropertyNumberOfBedRooms IN (2)
and PropertyNumberOfBathRooms IN (5)
and PropertySquareMeters IS NOT NULL
and PropertyNumberOfGarages IS NOT NULL;

/* #8 */
SELECT * FROM Properties WHERE 
PropertyDateAdded IN ('2000-01-01')
and AddressID IN (1)
and OwnerID IN (1)
and PropertyNumberOfRooms IN (13)
and PropertyNumberOfBedRooms IN (2)
and PropertyNumberOfBathRooms IN (5)
and PropertySquareMeters IN (12352)
and PropertyNumberOfGarages IS NOT NULL;

/* #9 */
SELECT * FROM Properties WHERE 
PropertyDateAdded IN ('2000-01-01')
and AddressID IN (1)
and OwnerID IN (1)
and PropertyNumberOfRooms IN (13)
and PropertyNumberOfBedRooms IN (2)
and PropertyNumberOfBathRooms IN (5)
and PropertySquareMeters IN (12352)
and PropertyNumberOfGarages IN (3);


DELETE FROM Properties WHERE ID = (1)
declare @max int
select @max=max([ID]) from [Properties]
if @max IS NULL   --check when max is returned as null
    SET @max = 0 
DBCC CHECKIDENT('Properties', RESEED, @max)                                 


/* Property_Address Page */
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
WHERE AddressID = (1)
)

/* Property_Additional Page */

SELECT *
FROM Properties
WHERE PropertyNumberOfBedRooms >= 1
and PropertyNumberOfBathRooms >= 1


SELECT *
FROM Properties
WHERE PropertySquareMeters between 0 and 100000

