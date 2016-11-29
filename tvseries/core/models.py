from tvseries.ext import db


class TVSerie(db.Model):
    id = db.Column(db.Integer(),
                   nullable=False, unique=True,
                   autoincrement=True, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)
    episodies_number = db.Column(db.Integer, nullable=False, default=1)
    author = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        if self.description:
            self.description = "{0}...".format(self.description[0:10])

        return ("TVSerie(id={!r}, name={!r}, "
                "description={!r}, episodies_number={!r})").format(
            self.id, self.name,
            self.description,
            self.episodies_number)
