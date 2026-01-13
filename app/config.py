class Config:
    SQLALCHEMY_DATABASE_URI = (
        "mysql+pymysql://root:123456@localhost:3306/flask_test"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
