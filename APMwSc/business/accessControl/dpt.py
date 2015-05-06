from sqlalchemy.sql.schema import PrimaryKeyConstraint
class clsDpt(db.Model):
    __tablename__ = 'dpt'
    namedpt = db.column(db.string(50),   nullable=False )
    iddpt    = db.column(db.Integer   ,primary_key= True)