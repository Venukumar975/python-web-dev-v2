from sqlalchemy import create_engine , text
db_connection_string = 'mysql+pymysql://admin:joviancareers975@jovian-careers-db.cbwysoeg2qt7.eu-north-1.rds.amazonaws.com/jovian_careers?charset=utf8mb4'
engine = create_engine(db_connection_string,connect_args={
  "ssl":
})

with engine.connect() as conn:
  result = conn.execute(text("select * from jobs"))
  print(result.all())
