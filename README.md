# FeedbackForm
[![Check Style](https://github.com/jgil325/FeedbackForm/actions/workflows/checkStyle.yml/badge.svg)](https://github.com/jgil325/FeedbackForm/actions/workflows/checkStyle.yml)
[![Tests](https://github.com/jgil325/FeedbackForm/actions/workflows/test.yaml/badge.svg)](https://github.com/jgil325/FeedbackForm/actions/workflows/test.yaml)

## Installation

Use the package manager pip3 to install the following dependencies:
  *Flask

```bash
sudo pip3 install flask
sudo pip3 install flask-wtf
sudo pip3 install SpeechRecognition
sudo pip3 install turbo-flask
sudo pip3 install Flask-SQLAlchemy
sudo pip3 install flask-login
```

## Usage

```python
from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
```

## To Run
```bash
export FLASK_APP=main.py
flask run --host=0.0.0.0
```
