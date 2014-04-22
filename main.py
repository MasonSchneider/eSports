import os
from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)
app.config.update(DEBUG = True,)

def getNextEvent():
    return "Club Mixer on 5/3/14"

@app.route('/')
@app.route('/index/')
def index():
    return render_template('esports.html', nextE=getNextEvent())

@app.route('/register/<event>')
def registerLoL(event):    
    if str(event) == 'lol5':
        return render_template('registerLoL.html', nextE=getNextEvent())

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
    return render_template('events.html', nextE=getNextEvent())

@app.route('/events/<message>')
def eventsWithMessage(message):
    return render_template('eventsMessage.html',message=message.replace("+"," "), nextE=getNextEvent())

@app.route('/eventinfo/<event>')
def eventinfo(event):
    if event == 'lol14':
        return render_template('lol14info.html', nextE=getNextEvent())
    elif event == 'mixer14':
        return render_template('mixer14info.html', nextE=getNextEvent())
    return redirect(url_for('index'))

@app.route('/about/')
def about():
    return render_template('about.html', nextE=getNextEvent())

@app.route('/members/')
def members():
    return render_template('members.html', nextE=getNextEvent())

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 80))
    app.run(host='0.0.0.0', port=port)