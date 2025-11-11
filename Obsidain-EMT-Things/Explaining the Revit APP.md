# Introduction
This repository is for an Final Year Project The details explained here will include the way to solve on of the issues that was found within the existing code, which i do not have a copy of. This issue revolves around the issue of linking a window to a room in the Revit API. This is because although  the API detects the windows attached to a wall, which attaches to the room, it attaches to the whole section of wall. This means that the window cannot be pinpointed to a specific room. This causes issues with the calculation of ETTV. So my code was the solution for this issue. The next chapter will show the problem in a more detailed way.

# Problem
The below diagram show cases a example of a floor plan that the plugin will be run on. The model has 3 rooms, toilet, bedroom and living room. As you can see, the toilet and bedroom have 1 window each, labeled $W_b$ and $W_a$ . This is an important distinction that is needed to be made for the application as it is important to know which windows belong to each room, for proper and accurate calculation. 

# Solutions
## Solution 1 (Attached to Wall)
This is one of the first solutions that my group came up with. This involves using the .Host method on a window, which is collected as a FamilyInstance. This gives the result on which wall is the one that the window is attached to. This is the most effective way to link a window to a wall, however this means that the whole section of wall is linked to the window. This means that a section of wall cannot be checked/linked to a room, thus making no viable for our use. However, it is a great way to check the number of windows on a wall area.

## Solution 2 (BoundingBox)
This solution uses a bounding box, what each element in Revit has. This allows us to use collision to check if a BoundingBox is within another and thus linking them. The issue with this method is best addressed below in the figure.
![[29ABC1B3-45BD-4E08-A240-2E9B860CC532.jpeg]]
Here in the above figure, the Living Room has 2 points, L1 & L2, which are orange in colour. While the bedroom also has 2 points, B1 & B2, which are in blue. As you can see, both L2 & B2 are the same point. Thus a bounding box of the Living Room will encompass the area with the white border. This means that the windows $W_a$ & $W_b$ will both clash with the Living Room bounding box and thus be linked to it. This wrong as $W_a$ should only be linked with the bedroom. This is because the BoundingBox method in the Revit API uses to points to create a box, thus it cannot fit the abnormal shape of the Living Room.

## Solution 3 (Geometry)
The solution uses geometry to find the room that a window should be linked with. In Revit a curve is a 2d object, with the properties of Length and 2 points, endpoint(0) and endpoint(1). These are the most important properties for the solution. As it involves getting the Curves of all the Rooms and Windows on one side of a building. Using another method, we can just get the curve of the edges of the Rooms, reducing computational load. 

After the curves are collected, we next run it through a function that makes it so the endpoints are in the correct orientation. Below is the correct orientation for where each of the endpoints should ideally be. This makes it so that all the curves have the endpoint(0) on the top left when on the X-Y graph. This method is also used for the windows.  ![[Screenshot 2025-09-17 at 19.31.41.png]]
This allows the distance between each endpoint(0)s and endpoint(1)s to be measured. Below is a description of how it is measured. ![[Screenshot 2025-09-17 at 19.41.46.png]] In the above image 