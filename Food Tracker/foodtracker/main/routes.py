from flask import Blueprint, render_template, request, redirect, url_for

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def index():
    log_dates = []  
    return render_template('index.html', log_dates=log_dates)

@main.route('/create_log', methods=['POST'])
def create_log():
    date = request.form.get('date')
    if not date:
        return "Date is required", 400

    print(f"New log created for date: {date}")
    return redirect(url_for('main.index'))

@main.route('/add', methods=['GET'])
def add():
    return render_template('add.html')

@main.route('/view', methods=['GET'])
def view():
    return render_template('view.html')