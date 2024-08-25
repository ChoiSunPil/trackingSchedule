import pytest
import telegram_message as tm

from model.TelegramMessage import TelegramMessage


@pytest.fixture(scope='module')
def connect_db():
    connection = next(tm.connect_db())
    yield connection


def test_fetch_messages(connect_db):
    connection = connect_db
    result = tm.fetch_messages(connection, 6000, 10)

    assert len(result) == 10


def test_tuple_to_pydantic(connect_db):
    # Pydantic 모델의 필드 이름을 가져옴
    connection = connect_db
    telegram_message_tuple = tm.fetch_messages(connection, 6000, 1)
    print(telegram_message_tuple[0])
    telegram_message = tm.convert_tuple_to_pydantic(telegram_message_tuple[0])

    assert type(telegram_message) == TelegramMessage
