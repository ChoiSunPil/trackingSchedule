from pydantic import BaseModel
import datetime
from typing import Optional

class TelegramMessage(BaseModel):
    message_id: int
    from_id: int
    from_first_name: str
    from_is_bot: bool
    from_last_name: str
    from_language_code: Optional[str]
    date: int
    chat_id: int
    chat_type: str
    chat_title: str
    text: str
    register_date: datetime

    class Config:
        arbitrary_types_allowed = True
