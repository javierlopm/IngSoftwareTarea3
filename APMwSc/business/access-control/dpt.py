from sqlalchemy.sql.schema import PrimaryKeyConstraint
class clsDpt(db.Model):
    __tablename__ = 'dpt'
    namedpt = db.column(db.string(50),         unique=False )
    iddpt    = db.column(db.Integer   ,primary_key= True)