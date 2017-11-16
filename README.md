# fitness_site
 
### Objectives

Build a web app that fulfils a real world purpose. It should be composed of multiple reusable apps and include an authentication mechanism, e-commerce functionality and a form with validation. The project must be connected to an SQL database.

 ### What does it do?
 
It allows users to register and login to the fitness site in order to access the forum and member benefits. It also allows users to book one of three membership options to use gym facilities. A blog and content throughout offer information on the services. 
 
### How does it work
 
This website uses Django as a framework and is styled using Bootstrap.

 
## Tech Used
 
### Some of the tech used includes:
- [Django](https://www.djangoproject.com/)
 a high-level Python framework handling user authentication, content administration, site maps, RSS feeds and more
 - [Bootstrap](http://getbootstrap.com/)
 is used to create a responsive layout
- [npm](https://www.npmjs.com/)
 is used to install http-server
- [bower](https://bower.io/)
 is used to manage front-end components
- [JavaScript](https://javascript.com/)
 is used for interactivity

## Testing

### Getting the code up and running
1. Firstly you will need to clone this repository by running the ```git clone <project's Github URL>``` command
2. After you've that you'll need to make sure that you have **npm** and **bower** installed
  1. You can get **npm** by installing Node from [here](https://nodejs.org/en/)
  2. Once you've done this you'll need to run the following command:
     `npm install -g bower # this may require sudo on Mac/Linux`
3. Once **npm** and **bower** are installed, you'll need to install all of the dependencies in *package.json* and *bower.json*
  ```
  npm install
 
  bower install
  ```
4. After those dependencies have been installed you'll need to make sure that you have **http-server** installed. You can install this by running the following: ```npm install -g http-server # this also may require sudo on Mac/Linux```
5. Once **http-server** is installed run ```http-server```
6. The project will now run on [localhost](http://127.0.0.1:8080)
