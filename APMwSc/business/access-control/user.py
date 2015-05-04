from sqlalchemy.sql.schema import PrimaryKeyConstraint
class clsUser(db.Model):
    __tablename__ = 'user'
    fullname = db.column(db.string(50),              unique=False)
    username = db.column(db.string(16),         primary_key=True )
    password = db.column(db.string(16),              unique=False)
    email    = db.column(db.string(30),              unique=True )
    iddpt    = db.column(db.Integer   ,db.ForeignKey('dpt.iddpt'))
    idrole   = db.column(db.Integer   ,db.ForeignKey('role.idrole'))

    