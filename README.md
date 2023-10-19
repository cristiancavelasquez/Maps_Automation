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

Para resolver este problema utilicé Python e implementé la libreria Selenium para automatizar una navegación web. La solucion de este problema se divide en dos archivos de código:

  - Dada una dirección, hallar una UTC - Esto se llevó a cabo navegando la web app.
  - Dadas unas cordenadas, encontrar una direccion "limpia" para poderla poner en la solución de arriba - Esto se elaboró con [Google Maps](https://www.google.com/maps).

Esto se tuvo que resolver de esta manera, ya que la web app no permite buscar cordenadas, solo direcciones. Por otra parte, muchas veces como se puede ver en la primera imagen (muestra de datos) se proporcionan direcciones no muy explicitas, por lo que las cordenadas es la unica alternativa.

a continuacion voy a describir brevemente cada archivo de código y cómo implementé selenium para resolver el problema:

### Address to UTC

ddd

### Coordinates to Adress

dedee


## Results


[^1]: A geographically delimited area for georeferencing purposes, based on the concept of a zip code. However, some modifications are made to it, with large cities being subdivided into smaller zones and small cities being treated as a single zone.
