from app import app, db, main, socketio
db.create_all()
app.register_blueprint(main)
app.debug = True
socketio.run(app, host="0.0.0.0")
