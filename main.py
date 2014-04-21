import os
from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)
app.config.update(DEBUG = True,)

@app.route('/')
@app.route('/index/')
def index():
    return render_template('esports.html')

@app.route('/register/<event>')
def registerLoL(event):    
    if str(event) == 'lol5':
        return render_template('registerLoL.html')

@app.route('/registerteam/<event>', methods=['POST'])
def registerTeam(event):
    if str(event) == 'lol5':
        teamString = "Team: " + str(request.form['team']) + "  Members: "
        for i in range(0,5):
            memString = "(" + request.form[str(i)+'email'] + ", " + request.form[str(i)+'summoner'] + ")"
            if i < 5:
                memString += " | "
            teamString += memString
        teamString += '\n'
        with open("teams.txt",'a') as teamFile:
            teamFile.write(teamString)
        return redirect(url_for('eventsWithMessage',message="Team+Registered+Successfully"))


@app.route('/events/')
def events():
    return render_template('events.html')

@app.route('/events/<message>')
def eventsWithMessage(message):
    return render_template('eventsMessage.html',message=message.replace("+"," "))

@app.route('/eventinfo/<event>')
def eventinfo(event):
    if str(event) == 'lol':
        return render_template('eventinfo.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/members/')
def members():
    return render_template('members.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 80))
    app.run(host='0.0.0.0', port=port)