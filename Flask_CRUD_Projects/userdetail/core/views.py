from flask import Flask, render_template, redirect, request, Blueprint

core = Blueprint('core',__name__)

@core.route('/')
def index():

    return render_template('index.html')

@core.route('/info')
def info():

    return render_template('info.html')