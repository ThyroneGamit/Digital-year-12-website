### import from modules###
from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint('views', __name__)
#home route ( Must login )
@views.route('/home')
@login_required
def home():
    return render_template("home.html", user=current_user)
#statistics route
@views.route('/stat')
@login_required
def stat():
    return render_template("stat.html", user=current_user)
#Homepage route 
@views.route('/')
@views.route('/home1')
def home1():
    return render_template("home1.html", user=current_user)

#Video clips route 
#notes in video clips
@views.route('/clips', methods=['GET', 'POST'])
@login_required
def notes():
    if request.method == 'POST': 
        note = request.form.get('note')#Gets the note from the HTML 

        if len(note) < 1:
            flash('Note is too short!', category='error') 
        else:
            new_note = Note(data=note, user_id=current_user.id)  #providing the schema for the note 
            db.session.add(new_note) #adding the note to the database 
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("clips.html", user=current_user)

#notes route/ deleting Notes
@views.route('/delete-note', methods=['POST'])
def delete_note():  
    note = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})