""" Mimics a typical file structure when using models classes and database witin an app

See https://sqlmodel.tiangolo.com/tutorial/code-structure/
There is no actual app code yet though!
"""
from activities.starter.db_wk8.database import create_db_and_tables


def main():
    create_db_and_tables()


if __name__ == '__main__':
    main()
