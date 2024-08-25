import pymysql
from dotenv import load_dotenv
from pathlib import Path
import os
from model.TelegramMessage import TelegramMessage

def connect_db():
    load_dotenv()
    host = os.getenv('DB_HOST')
    port = int(os.getenv('DB_PORT'))
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    database = os.getenv('DB_DATABASE')

    base_dir = Path(__file__).resolve().parent
    ca_path = base_dir / 'resource' / 'singlestore_bundle.pem'

    connection = pymysql.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database,
        ssl={
            'ca': str(ca_path)  # 현재 디렉토리에 있는 경우
        }

    )

    yield connection

    connection.close()


def fetch_messages(connect_db: pymysql.connections.Connection
                   , message_id: int
                   , limit: int) -> tuple:
    cursor = connect_db.cursor()
    cursor.execute('SELECT * FROM messages WHERE message_id >= %s  ORDER BY message_id ASC LIMIT %s ',(message_id, limit))
    result = cursor.fetchall()
    return result


def convert_tuple_to_pydantic(message:tuple):
    fields = TelegramMessage.model_fields

    # 필드 이름과 튜플 값을 매핑하여 딕셔너리 생성
    data_dict = {field: value for field, value in zip(fields, message)}
    # 생성된 딕셔너리를 사용해 Pydantic 모델 인스턴스 생성
    telegram_message = TelegramMessage(**data_dict)

    return telegram_message