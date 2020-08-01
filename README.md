# :sunrise_over_mountains: wecken

## I. :books: About

This project serves as a starter Rest API. It is a FastAPI application served on uvicorn. MongoDB is used for the database. It comes with a pre-written docker file for easy CI/CD integration. The plan is to add support for scaling to a Kubernetes cluster.

## II. :package: Development Setup

### 1. Clone the [wecken api](https://github.com/raynaglieri/wecken_api.git) using [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

```zsh
git clone <https://github.com/raynaglieri/wecken_api.git>
```

### 2. Install [**Python 3**](https://www.python.org/downloads/) for your prefered development OS

### 3. Install **virtualenv**

```zsh
sudo pip3 install virtualenv
```

### 4. Create a new virtual environment and activate it

Within the wecken project directory enter the following commands:

```zsh
virtualenv *wecken_api_env* && source *wecken_api_env*/bin/activate
```

Your prompt will change to indicate that you are now operating within the virtual environment. It will look something like this:

```zsh
(*wecken_api_env*)user@host:~%.
```

### 5. Install dependencies within your new virtual environment using the provided *requrements.txt*

```zsh
pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt
```

### 6. Install MongoDB

On MacOS using [Brew](https://brew.sh/):

```zsh
brew tap mongodb/brew
brew install mongodb-community@4.2
brew services start mongodb-community@4.2
```

If you are using another OS please visit the [offical MongoDB Documentation](https://docs.mongodb.com/manual/administration/install-community/)

### 7. Run the wecken API

```zsh
uvicorn --reload  app.main:app
```
