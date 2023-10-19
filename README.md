# Maps Automation
The main purpose of this project is to automate the process of determining the geographical area in which given coordinates are located. In the case of the company where the project was developed, these geographical areas are known as UTC and can be interpreted in a certain way as postal zones.

## Context
The company where this project was developed is a data analysis firm specializing in the pharmaceutical sector. Their information sources are pharmacy chains, and their clients are pharmaceutical laboratories. When a new supplier joins the company, a person within the company receives the addresses of all the supplier's retail locations and must place them within a UTC[^1]. Sometimes, the suppliers include coordinates for their retail locations as part of the address.

![initialData](https://github.com/cristiancavelasquez/Maps_Automation/blob/1027b61c1fc6bdacc9b60a44f6faaed0a4a7919a/Screenhot_folder/Captura%20de%20pantalla%202023-10-19%20145322.png)

In the previous image, you can see a brief series of data. However, to grasp the scale of the total amount of data, the smallest provider associated with the company has around 3000 points of sale, and there are approximately more than 132 providers (pharmacy chains associated). This means that there are hundreds of thousands of addresses that a single person must assign manually whenever there are changes or when a new provider enters.

Currently, the person in charge has a web application that operates with a Google Maps API. On the map of Colombia, the UTC areas are loaded. What the person needs to do manually is to type or copy and paste the address into the search bar. This action pins a specific point on the map. By clicking on the area where that point is located, the person can view the UTC associated with that address. Finally, they must copy and paste this UTC into a final Excel file where they correlate the address with the found UTC.

//imagen de app de cristo

As you can imagine, this process needs to be repeated countless times for each provided address, making it a highly demanding and time-consuming task.


## Solution - Development

To solve this problem, I used Python and implemented the Selenium library to automate web navigation. The solution to this problem is divided into two code files:

  - Finding a UTC for a given address - This was accomplished by navigating the web application.
  - Given some coordinates, finding a "clean" address to use in the solution above - This was achieved using [Google Maps](https://www.google.com/maps).

The above had to be solved in this way because the web application doesn't allow searching by coordinates, only by addresses. Additionally, as can be seen in the first image (data sample), sometimes less explicit addresses are provided, making coordinates the only alternative.

> [!IMPORTANT]
> **Inside the  ```.py``` files, you should be able to find well-documented documentation in English for the process that was carried out in the creation of each script.**

## Results

The result was an automated process created with Python, where you need to organize the addresses you want to search for in an Excel file, run the program, and obtain a final dataframe with the provided data along with the data that was found.

- **Result of the script ```addressToUtc.pý```**
  
  imagen

- **Result of the script ```coordsToAddress.py```**

imagen

With this structure, the person in charge can compare the initially entered address with the found address and determine visually whether they are a close match. If they are very similar, it is assumed that the UTC was assigned correctly. For those that are not, manual assignment is necessary.

From the tests that have been conducted, this code successfully matches information in approximately 70% of cases. The remaining 30% needs to be assigned manually, but this tool has significantly reduced time and costs.


Thank you for reading this markdown, I hope it has been very useful to you 😊.



[^1]: A geographically delimited area for georeferencing purposes, based on the concept of a zip code. However, some modifications are made to it, with large cities being subdivided into smaller zones and small cities being treated as a single zone.
