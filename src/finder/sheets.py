import gspread
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from config import TEST_URL, CREDS
from models import Base, Participant

GC = gspread.service_account_from_dict(CREDS)
SH = GC.open_by_url(TEST_URL)


def get_data():
    worksheet = SH.sheet1
    return worksheet.get_all_values()


def data_to_db():
    # engine = create_engine(
    #     'postgresql+psycopg2://postgres:9415892mb)@db',
    #     echo=False
    # )
    engine = create_engine('sqlite:///sqlite.db', echo=False)
    Base.metadata.create_all(bind=engine)
    session = Session(engine)

    data = get_data()

    for row in data[1:]:
        participant = Participant(
            name=row[0],
            spec=row[1],
            exp=row[2],
            available=row[3],
            worktime=row[4],
            education=row[5],
            wants=row[6],
            can_do=row[7],
            tg_nickname=row[8],
            accept=row[9],
            city=row[10],
            timezone=row[11]
        )
        session.add(participant)
    session.commit()


if __name__ == '__main__':
    data_to_db()
