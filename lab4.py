from flask import Blueprint, render_template, request
lab4 = Blueprint('lab4', __name__)

@lab4.route('/lab4/')
def lab():
    return render_template('lab4/lab4.html')