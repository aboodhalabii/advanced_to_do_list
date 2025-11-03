from sqlalchemy import MetaData, Table, Column, SERIAL, Text,Datetime,ENUM

users_table = Table(
        "users",MetaData,
        Column("id", SERIAL, primary_key=True),
        Column("username", Text, nullable=False, unique=True),
        Column("email", Text, unique=True),
        Column("password" ,default=True),
        Column("created_at",Datetime),
        Column("updated_at",Datetime)

    )

subtodo = Table(
        "subtodo",MetaData,
        Column("id", SERIAL, primary_key=True),
        Column("title", Text, nullable=False, unique=True),
        Column("email", Text, unique=True),
        Column("description", Text, unique=True),
        Column("duedate" ,Datetime),
        Column("created_at",Datetime),
        Column("updated_at",Datetime)
    )
todo = Table(
        "todo",MetaData,
        Column("id", SERIAL, primary_key=True),
        Column("title", Text, nullable=False, unique=True),
        Column("email", Text, unique=True),
        Column("description", Text, unique=True),
        Column("duedate" ,Datetime),
        Column("created_at",Datetime),
        Column("updated_at",Datetime)
    )