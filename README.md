# Flask Blog with Docker
Simple CRUD Flask app based off of the quickstart/tutorial from Flask. This has been taken a bit further by Dockerizing it.
If for some reason someone is reading this here is how you can immediately start playing with the web app on your own localhost. Clone the repo and run the following in a terminal (you need Docker and Docker Compose installed)

```sh
docker-compose up
```

then go to the  [localhost:8080](http://localhost:8080/) (or whatever port you may have modified it to)

If for some reason docker-compose isn't working for you try something like

```sh
docker build -t flaskapp:latest . 
```
followed by

```sh
docker run -p 8080:8080 flaskapp
```
and THEN go to the appropriate localhost. 

### Example pics (CSS in pics are old, but otherwise the rest is the same)

main index page where you can look at existing blog entries! Edit/Delete your own!


![index](./pix/index.jpg) 

Register as a new user!

![reg](./pix/reg.jpg) 

Make a new blog entry!

![new](./pix/new.jpg) 