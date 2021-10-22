Last login: Fri Oct 22 13:05:31 on ttys002
(base) rahuljain@RJAIN-MAC ~ % ls
Applications	Boostnote	Desktop		Documents	Downloads	EMLO		EPAi		Library		Mobiledgex	Movies		Music		Pictures	Postman		Public		VIA		anaconda2	docker_edge	go		vaccine		venv
(base) rahuljain@RJAIN-MAC ~ % cd EMLO
(base) rahuljain@RJAIN-MAC EMLO % ls
session2	session3
(base) rahuljain@RJAIN-MAC EMLO % mkdir toniq
(base) rahuljain@RJAIN-MAC EMLO % cd toniq
(base) rahuljain@RJAIN-MAC toniq % git clone https://github.com/toniqapps/EMLO.git
Cloning into 'EMLO'...
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (3/3), 585 bytes | 292.00 KiB/s, done.
(base) rahuljain@RJAIN-MAC toniq % ls
EMLO
(base) rahuljain@RJAIN-MAC toniq % cd EMLO
(base) rahuljain@RJAIN-MAC EMLO % mkdir session3
(base) rahuljain@RJAIN-MAC EMLO % open .
(base) rahuljain@RJAIN-MAC EMLO % cd ..
(base) rahuljain@RJAIN-MAC toniq % cd ..
(base) rahuljain@RJAIN-MAC EMLO % ls
session2	session3	toniq
(base) rahuljain@RJAIN-MAC EMLO % cd session3
(base) rahuljain@RJAIN-MAC session3 % cd ass*
(base) rahuljain@RJAIN-MAC assignment % ls
Pytorch-Flask-Starter
(base) rahuljain@RJAIN-MAC assignment % cd P*
(base) rahuljain@RJAIN-MAC Pytorch-Flask-Starter % open .
(base) rahuljain@RJAIN-MAC Pytorch-Flask-Starter % cd ..
(base) rahuljain@RJAIN-MAC assignment % cd .
(base) rahuljain@RJAIN-MAC assignment % cd ..
(base) rahuljain@RJAIN-MAC session3 % ks
zsh: command not found: ks
(base) rahuljain@RJAIN-MAC session3 % ls
assignment
(base) rahuljain@RJAIN-MAC session3 % cd ..
(base) rahuljain@RJAIN-MAC EMLO % ls
session2	session3	toniq
(base) rahuljain@RJAIN-MAC EMLO % cd ton*
(base) rahuljain@RJAIN-MAC toniq % cd se*
zsh: no matches found: se*
(base) rahuljain@RJAIN-MAC toniq % ls
EMLO
(base) rahuljain@RJAIN-MAC toniq % cd EM*
(base) rahuljain@RJAIN-MAC EMLO % ls
README.md	session3
(base) rahuljain@RJAIN-MAC EMLO % cd se*
(base) rahuljain@RJAIN-MAC session3 % ls
Dockerfile		LICENSE			Procfile		README.md		app.py			assets			heroku.yml		imagenet_classes.txt	models.py		requirements.txt	runtime.txt		static			templates
(base) rahuljain@RJAIN-MAC session3 % ls -a
.			.DS_Store		LICENSE			README.md		assets			imagenet_classes.txt	requirements.txt	static
..			Dockerfile		Procfile		app.py			heroku.yml		models.py		runtime.txt		templates
(base) rahuljain@RJAIN-MAC session3 % rm -rf .DS_Store
(base) rahuljain@RJAIN-MAC session3 % ls -a
.			..			Dockerfile		LICENSE			Procfile		README.md		app.py			assets			heroku.yml		imagenet_classes.txt	models.py		requirements.txt	runtime.txt		static			templates
(base) rahuljain@RJAIN-MAC session3 % cd ..
(base) rahuljain@RJAIN-MAC EMLO % cd ..
(base) rahuljain@RJAIN-MAC toniq % ls
EMLO
(base) rahuljain@RJAIN-MAC toniq % cd EMLO
(base) rahuljain@RJAIN-MAC EMLO % git status
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	.DS_Store
	session3/

nothing added to commit but untracked files present (use "git add" to track)
(base) rahuljain@RJAIN-MAC EMLO % rm -rf .DS_Store
(base) rahuljain@RJAIN-MAC EMLO % git add .
(base) rahuljain@RJAIN-MAC EMLO % git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	new file:   session3/Dockerfile
	new file:   session3/LICENSE
	new file:   session3/Procfile
	new file:   session3/README.md
	new file:   session3/app.py
	new file:   session3/assets/screenshot.png
# Flask/Pytorch/Docker starter app

This project is aimed to help machine learning developers to quickly build and deploy a Flask web app that take advantage of their machine learning  ready PyTorch model. The documentation explains how to get up and running with either virtualenv or Docker.

![Website mockup](assets/screenshot.png)

This website is deployed in Heroku: https://flaskpytorch.herokuapp.com/

By default, this app uses MobileNetV2 image classifier that was pre-trained on the ImageNet dataset. This can be easily changed with any custom deep learning model.

## Getting Started (using Python virtualenv)

You need to have Python installed in your computer.

1. Install `virtualenv`:
    ```
    pip install virtualenv
    ```
2. Create a Python virtual environment:
    ```
    virtualenv venv
    ```
3. Activate virtual environment:
    1. Windows:
    ```
    cd venv\Scripts
    activate
    cd ..\..
    ```
    2. Lunix / Mac:
    ```
    source venv/bin/activate
    ```
4. Install libraries:

   ```
   pip install -r requirements.txt
   ```

### Run the code

* Run the app:
    ```
    flask run
    ```
* Run on a specific port:
    ```
    flask run -p <port>
    ```

## Getting Started (using Docker)

1. Create a Docker image
    ```
    docker build -t pytorchflask .
    ```
    This will create an image with the name `pytorchflask`. You can replace that with a custom name for your app.

2. Run the docker image
    ```
    docker run -d -p 127.0.0.1:5000:80 pytorchflask
    ```
    This will run the app on port `5000`. You can replace that with which ever port that is more suitable.

## Deploying to Heroku

- Create Heroku app
    ```
    heroku create
    git push heroku master
    ```

OR

- Add to existing Heroku app
    ```
    heroku git:remote -a <your-app-name>
    git push heroku master
    ```



"README.md" 104L, 2403C# Flask/Pytorch/Docker starter app

This project is aimed to help machine learning developers to quickly build and deploy a Flask web app that take advantage of their machine learning  ready PyTorch model. The documentation explains how to get up and running with either virtualenv or Docker.

![Website mockup](assets/screenshot.png)

This website is deployed in Heroku: https://flaskpytorch.herokuapp.com/

By default, this app uses MobileNetV2 image classifier that was pre-trained on the ImageNet dataset. This can be easily changed with any custom deep learning model.

## Getting Started (using Python virtualenv)

You need to have Python installed in your computer.

1. Install `virtualenv`: 
    ```
    pip install virtualenv
    ```
2. Create a Python virtual environment:
    ```
    virtualenv venv
    ```
3. Activate virtual environment:
    1. Windows:
    ```
    cd venv\Scripts
    activate
    cd ..\..
    ```
    2. Lunix / Mac:
    ```
    source venv/bin/activate
    ```
4. Install libraries:
   
   ```
   pip install -r requirements.txt
   ```

### Run the code

* Run the app:
    ```
    flask run
    ```
* Run on a specific port:
    ```
    flask run -p <port>
    ```

## Getting Started (using Docker)

1. Create a Docker image
    ```
    docker build -t pytorchflask .
    ```
    This will create an image with the name `pytorchflask`. You can replace that with a custom name for your app.

2. Run the docker image
    ```
    docker run -d -p 127.0.0.1:5000:80 pytorchflask
    ```
    This will run the app on port `5000`. You can replace that with which ever port that is more suitable.

## Deploying to Heroku

- Create Heroku app
    ```
    heroku create 
    git push heroku master
    ```
    
OR

- Add to existing Heroku app
    ```
    heroku git:remote -a <your-app-name>
    git push heroku master
    ```



## Changing the model

1. Go to `models.py`
2. Follow the structure of the class `MobileNet`to create a custom model class
3. Use your class in `app.py`

## Built With

* [Pytorch](https://pytorch.org/) - The Machine Learning framework used
* [Flask](http://flask.palletsprojects.com/en/1.1.x/) - The web server library

## Authors

* **Imad Eddine Toubal** - *Initial work* - [imadtoubal](https://github.com/imadtoubal)


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details


 Happy coding!
