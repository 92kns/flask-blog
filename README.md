# flask-blog
Simple CRUD Flask app based off of the quickstart/tutorial from Flask. This has been taken a bit further by Dockerizing it.
If for some reason someone is reading this here is how you can immediately start playing with the web app on a local host. Clone the repo and in the root folder run something like this in a terminal 
```
docker build -t flaskapp:latest .
```

followed by

```
docker run -p 5000:5000 flaskapp
```

At the moment it is using development server because well you're running it locally and not in production. Stay tuned!


main index page where you can look at existing blog entries! Edit/Delete your own!


![index](./pix/index.jpg) 

Register as a new user!

![reg](./pix/reg.jpg) 

Make a new blog entry!

![new](./pix/new.jpg) 