from address import Address
from mailing import Mailing

from_addr = Address("125426", "Москва", "Смоленская", "12", "9")
to_addr = Address("197378", "Санкт-Петербург", "Пушкинская", "12", "35")

mail = Mailing(
    to_address=to_addr,
    from_address=from_addr,
    cost=500.0,
    track="RC256958RU"
)

track_info = f"Отправление {mail.track} из "
from_info = f"{mail.from_address.formatted()}"
to_info = f" в {mail.to_address.formatted()}"
cost_info = f". Стоимость {mail.cost} рублей."

print(track_info + from_info + to_info + cost_info)

