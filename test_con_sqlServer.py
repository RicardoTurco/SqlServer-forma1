from sqlalchemy import create_engine


engine = create_engine("mssql+pymssql://sa:Secret1234@localhost:1433/master")
con = engine.connect()

print("")
print("criou o CON")

try:
    query = "select * from dbo.account"
    result = con.execute(query)
    print("")
    print("criou o RESULT")
    print("")

    for row in result:
        print(row)

    print("")
    print("exibiu os RESULTADOS !!!")

except Exception as error:
    print("")
    print(f"error: {error}")
    

print("")
print("final...")
print("")
