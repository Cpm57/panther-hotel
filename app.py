from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory list of reservations
reservations = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/reserve', methods=['GET', 'POST'])
def reserve():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        room_type = request.form['room_type']
        check_in = request.form['check_in']
        check_out = request.form['check_out']

        # Add reservation with unique 'id'
        reservation = {
            'id': len(reservations) + 1,  # Unique ID for each reservation
            'name': name,
            'email': email,
            'room_type': room_type,
            'check_in': check_in,
            'check_out': check_out
        }

        reservations.append(reservation)

        return redirect(url_for('confirmation', name=name, room_type=room_type, check_in=check_in, check_out=check_out))

    return render_template('reservation.html')

@app.route('/confirmation')
def confirmation():
    name = request.args.get('name')
    room_type = request.args.get('room_type')
    check_in = request.args.get('check_in')
    check_out = request.args.get('check_out')

    return render_template('confirmation.html', name=name, room_type=room_type, check_in=check_in, check_out=check_out)

@app.route('/view')
def view_all():
    return render_template('list.html', reservations=reservations)

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    global reservations
    # Find reservation with matching ID and delete it
    reservations = [res for res in reservations if res['id'] != id]
    
    return redirect(url_for('view_all'))  # Redirect back to view all reservations

if __name__ == '__main__':
    app.run(debug=True)



