from app.factory import create_app, celery_app,db

app = create_app(config_name="DEVELOPMENT")
app.app_context().push()

if __name__ == "__main__":
    print(app.url_map)
    app.run()

    # db.create_all()
