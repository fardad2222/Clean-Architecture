

For Create Migrations in project

1- Create Migrations folder in folder of infrastructure of project using alembic
    
    - alembic init -t generic migrations

2- Create DB Model Configurations in persistence layer
    -- cities
        -- CityDBModelConfig.py

3-
export PYTHONPATH=$PYTHONPATH:"/home/taavv1/anaconda3/envs/py3113/lib/python3.11/site-packages"
export PYTHONPATH=$PYTHONPATH:"/home/taavv1/Templates/newthree/Clean-Architecture-RestAPI-Flask"


4- Generate migration of database using alembic with models

    - alembic revision --autogenerate -m "Adding CityDBModelConfig"

5- Apply the migration

    - alembic upgrade head

