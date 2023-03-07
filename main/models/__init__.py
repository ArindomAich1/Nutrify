from main import db, app
class foodData(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    foodName = db.Column(db.String(100), nullable=False)
    carbs= db.Column(db.Float)
    protein= db.Column(db.Float)
    fats= db.Column(db.Float)
    energy= db.Column(db.Float)

    def __repr__(self) -> str:
        return f"{self.id}-{self.foodName}"

class admin(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    username= db.Column(db.String(100),unique=True)
    password=db.Column(db.String(200))

    def __repr__(self) -> str:
        return f"{self.id}"

with app.app_context():
    db.create_all()

