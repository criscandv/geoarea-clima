from app import db
from datetime import datetime


def process_dict(row):
    my_dict = {}
    now = datetime.now()
    for key in row.keys():
        if key.startswith('_'):
            continue

        my_dict[key] = row[key]
        if type(row[key]) == type(now.time()):
            my_dict[key] = row[key].strftime("%H:%M")
        elif type(row[key]) == type(now.date()):
            my_dict[key] = row[key].strftime("%Y-%m-%d")

    return my_dict


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
    hours = db.relationship('Hour', backref='day', lazy='joined')

    def __repr__(self):
        return f'<date {self.date}> <localidad {self.city}>'

    def get_dict_data(self, localidad):
        days = Day.query
        if localidad:
            days = Day.query.filter(Day.city.ilike(f'%{localidad}%'))

        days = days.all()
        
        to_dict = []
        for d in days:
            day = process_dict(d.__dict__)
            hours = []
            for h in day['hours']:
                hour = process_dict(h.__dict__)
                hours.append(hour)

            day['hours'] = hours
            to_dict.append(day)

        return to_dict


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
