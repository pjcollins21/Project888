Sport book platform  
Author: Patrick Collins  
Python, Flask, Mongodb  (Windows10)  
Work based on following tutorial:  
https://towardsdatascience.com/creating-a-beautiful-web-api-in-python-6415a40789af  
Run Instructions:  
{Installation assuming not present on PC}  
1. Download install Mongodb and Mongodb Database Tools  
	- Tools is a zip archive, once extracted, get the path to \bin and add that to your PATH  
2. Install Python  
3. Install pip  
	- Optional - Install VirtualEnv  
4. Clone this Git Repo  
5. Navigate into Repo directory and initial venv:  
	- c:\users\(your_user_name)\myenv\Scripts\activate.bat  
6. Run:  
	- pip install -r requirements.txt  
7. Initialize MongoDb:  
	- "C:\Program Files\MongoDB\Server\4.4\bin\mongod.exe"  
8. Load project db:  
	- mongorestore -h localhost c:\{path-to-cloned-repo}\db  
9. Initialize FlaskAPI:  
	- from root of cloned repo, run: python app.python  
10. Using Postman or similar API test tool (or a browser with dev console to deliver JSON payloads)  
11. Create a user  
	- http://127.0.0.1:5000/authentication/signup/  
	- pass in user information in following format:  
		{  
		 "email": "radmin@nowhere.com",  
		 "password": "security",  
		 "access": {  
		  "admin": "True"  
		 },  
		 "name": "D.B. Admini",  
		 "phone": "555-555-5432"  
		}  
12. Sign in with user credentials:  
	- http://127.0.0.1:5000/authentication/login/  
	- pass in credentials as follows:  
		{  
		 "email": "radmin@nowhere.com",  
		 "password": "security"  
		}  
**NOTE:**You should be able to skip the create user step by using credentials above  
13. Capture JWT bearer token  
	- Sample token:  
		eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2MDUzODMyNDksIm5iZiI6MTYwNTM4MzI0OSwianRpIjoiNWY5MmQ1ZTctYmM3MS00ZjBjLWFhOTUtYmJkNzRhNGU4NjBhIiwiZXhwIjoxNjA1ODE1MjQ5LCJpZGVudGl0eSI6IjVmYjAzM2ZjNDczYzc1YjJkN2FlYTY0MyIsImZyZXNoIjpmYWxzZSwidHlwZSI6ImFjY2VzcyJ9.UWpsxPEFJ22T_BNDOO3eCfocQbtEcpLrkaBrKX5nCew  
	- This specific token won't be present, you'll need to capture this from the response when you log in.  
14. Query endpoints using bearer token auth   
	- http://localhost:5000/events/  
	- You'll need to pass in the bearer token in the auth field for all CRUD functions  
	and include json format information for Creates and Updates  
	  
What the API does:  
- dead simple access to DB
- reads work, creates don'test
- I think db data model is correct (first experience with non-relational db)
- user auth, token handling, and hashing of passwords via bcrypt  
What the API Does not have/does not do:  
- tests - ran out of time
- does not have preconfigured views
- other than simple login, does not feature user access control (views, updates, etc), but test spec suggested all actions were from a single provider...

	
