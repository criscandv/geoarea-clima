from app import db


class Day(db.Model):
    __tablename__ = 'day'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    city = db.Column(db.String(50), nullable=True)
    date = db.Column(db.Date, nullable=True)
    humidity = db.Column(db.Integer, nullable=True)
    icon = db.Column(db.String(10), nullable=True)
    icon_wind = db.Column(db.String(50), nullable=True)
    moon_phases_icon = db.Column(db.Integer, nullable=True)
    moonrise = db.Column(db.Time, nullable=True)
    moonset = db.Column(db.Time, nullable=True)
    sunrise = db.Column(db.Time, nullable=True)
    sunset = db.Column(db.Time, nullable=True)
    temperature_max = db.Column(db.Integer, nullable=True)
    temperature_min = db.Column(db.Integer, nullable=True)
    text = db.Column(db.String(120), nullable=True)
    wind = db.Column(db.Integer, nullable=True)
    wind_direction = db.Column(db.String(50), nullable=True)
    hours = db.relationship('Hour', backref='day', lazy=True)

    def __repr__(self):
        return f'<date {self.date}> <localidad {self.city}>'


class Hour(db.Model):
    __tablename__ = 'hour'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    day_id = db.Column(db.Integer, db.ForeignKey('day.id'), nullable=False)
    date = db.Column(db.Date, nullable=True)
    hour_data = db.Column(db.Time, nullable=True)
    humidity = db.Column(db.Integer, nullable=True)
    icon = db.Column(db.String(10), nullable=True)
    icon_wind = db.Column(db.String(50), nullable=True)
    pressure = db.Column(db.Integer, nullable=True)
    temperature = db.Column(db.Integer, nullable=True)
    text = db.Column(db.String(120), nullable=True)
    wind = db.Column(db.Integer, nullable=True)
    wind_direction = db.Column(db.String(50), nullable=True)

    def __repr__(self):
        return f'<hour_data {self.hour_data}>'
