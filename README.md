# Fibonacci number calculation REST backend
This Python sample application uses the [Flask](http://flask.pocoo.org/) framework.

This version of the application can be packaged and deployed as a Docker container. 


1. To build the container run (from the directory containing dockerfile):
	
		sudo docker build -t dg-fibonacci-be .        
        
2. To run the container run:
			
		sudo docker run -p 5000:5000 dg-fibonacci-be

3. To access the API:
		
		http://<app-ip>:5000/api/fibonacci/<num>

 
        
        
