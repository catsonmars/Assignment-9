# Assignment-9 Microservice project, Milestone #2.
**1)Clear instructions for how to programmatically REQUEST data from the microservice you implemented. Include an example call.
**
To request data. Go into the client.py file, then read line 12, there is a variable, {data}. {data} is used to send sql queries from client.py to host.py. As of now, "SELECT*FROM users works". 
That is, all book information will be returned.Note that data being send out is on line 19, s.sendlall(byte_data)

**2)Clear instructions for how to programmatically RECEIVE data from the microservice you implemented.
** To receive data, look at client.py again, go to line 21. See data = s.recv(1024). This will be what contains the SQL query data.

UML
![image](https://github.com/catsonmars/Assignment-9/assets/11530542/5f521eb6-dfd6-4107-bdee-8c63c2edacc5)

#Microservice examples
<img width="875" alt="Screen Shot 2023-11-20 at 10 17 29 PM" src="https://github.com/catsonmars/Assignment-9/assets/11530542/249dae76-6fb4-43f0-b427-2606d49e41f4">

#Mismatch between client and host port numbers
<img width="785" alt="Screen Shot 2023-11-20 at 10 18 39 PM" src="https://github.com/catsonmars/Assignment-9/assets/11530542/8a85c11c-5975-4edf-ab64-e75d6a4a1ef3">

I can't get the error to repeat, but if it ever says the port/ connection is busy, just rerun the program.
