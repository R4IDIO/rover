# Rover
Simple exercise about NASA and rovers !

 # MARS ROVERS

A squad of robotic rovers are to be landed by NASA on a plateau on Mars.
This plateau, which is curiously rectangular, must be navigated by the
rovers so that their on-board cameras can get a complete view of the
surrounding terrain to send back to Earth.

A rover's position and location is represented by a combination of x and y
co-ordinates and a letter representing one of the four cardinal compass
points. The plateau is divided up into a grid to simplify navigation. An
example position might be 0, 0, N, which means the rover is in the bottom
left corner and facing North.

In order to control a rover, NASA sends a simple string of letters. The
possible letters are 'L', 'R' and 'M'. 'L' and 'R' makes the rover spin 90
degrees left or right respectively, without moving from its current spot.
'M' means move forward one grid point, and maintain the same heading.

Assume that the square directly North from (x, y) is (x, y+1).

INPUT:
The first line of input is the upper-right coordinates of the plateau, the
lower-left coordinates are assumed to be 0,0.

The rest of the input is information pertaining to the rovers that have
been deployed. Each rover has two lines of input. The first line gives the
rover's position, and the second line is a series of instructions telling
the rover how to explore the plateau.

The position is made up of two integers and a letter separated by spaces,
corresponding to the x and y co-ordinates and the rover's orientation.

Each rover will be finished sequentially, which means that the second rover
won't start to move until the first one has finished moving.

OUTPUT
The output for each rover should be its final co-ordinates and heading.

INPUT AND OUTPUT

Test Input:

5 5 1 2 N LMLMLMLMM 3 3 E MMRMMRMRRM

Expected Output:  
1 3 N  
5 1 E

# OPTIONAL EXTENSION EXERCISE

Using the implementation of your solution to the "Mars Rover" problem as a base, implement a mechanism whereby your solution can be used remotely. How this is implemented is up to you. You may wish to choose to implement your own client or to use an existing widely available client such as telnet, curl or a web browser for interacting with your solution. Please include a brief description detailing the usage of this remote interface.

# INSTRUCTIONS

The project can be used on its own but also comes with an api to deploy if needed. 

### Requirements

- Python 3.6+

If you want to use the API, you also need to install the packages listed in the requirements.txt file with the command :  
`pip install -r requirements.txt`

### Run the project

To run the project, simply type the following command at the base of the project

`python main.py`

The program will then ask you to enter the script to be executed.  
Fill in the whole script and validate with the enter key.  

Example of script : `5 5 1 2 N LMLMLMLMM 3 3 E MMRMMRMRRM`  
 
As explained above, the first two numbers represent the x, y coordinates of the point at the top right of the board. The rest of the script concerns the location of the rovers, their orientation and the movement to be made.  

Once the execution is finished, if the script is judged correct, you should get the location of the rovers after their moves. 
 
Example of script result :  

- `1 3 N`
- `5 1 E`


### Errors

***What happens if the script is incorrect?*** 

- If the plateau dimensions are incorrect, or if the script does not have enough content, the following message should be displayed : "The dimensions of the plateau or the script are not correct."
- If any of the rover's movements are not correct the following message should be displayed: "Invalid instruction : {Error}" where {Error} is the unrecognized movement.
- If one of the movements causes the exit of the plateau, the following message should be displayed : "Invalid instruction, rover would leave the plateau !"

*Please note that the incorrect movement of a rover does not prevent the rest of the execution of the script and therefore you will get the final location of the other rovers if their movements are correct.*


### Deploying the api

Once you have installed the requirements, you must deploy the api using a web server.
Personally, I chose to use the ASGI web server "uvicorn".  
Installation : `pip install uvicorn`  
Docs : https://www.uvicorn.org/

Then, at the root of the project, just run the following command: `uvicorn api:app --reload`  
*Note that the --reload flag should not be used in production*

The server will then be deployed, and you can use the api. The default port is 8000.  
A Swagger documentation is available at the following address : http://127.0.0.1:8000/docs  

### Use of api

**Security** 

For each request, a "basic auth" authentication must be included.  
You can change the reference values for authentication in the api.py file by filling in the "NASA_USER" and "NASA_PASS" variables.  
By default, the values are retrieved in the system environment variables under the same name "NASA_USER" and "NASA_PASS". 

**Api path**

The use of the api is quite simple. Indeed, to execute a script, you must use the one and only path "/mission".  
You must of course include the authentication information in the request but also fill in the script as JSON in the body of the request according to the following format:  
`
{
    "script":"5 5 1 1 N MMRMM"
}
`

Thus, we get a query like this: 

`curl --location --request GET 'http://127.0.0.1:8000' \
--header 'Authorization: Basic {crypted_auth}' \
--header 'Content-Type: application/json' \
--data-raw '{
    "script":"5 5 1 1 N MMRMM"
}'
`    
where {crypted_auth} is the "user:pass" base64 encoded information

**and voilà!**