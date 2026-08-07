from address import Address
from mailing import Mailing

first_mailing = Mailing(Address(659000, "Tokio", "Lenina", 15, 7),
                        Address(659100, "Paris", "New", 3, 59),
                        5000, "a800f300")

print(f"Отправление {first_mailing.track} из {first_mailing.from_address} в {first_mailing.to_address}. Стоимость {first_mailing.cost} рублей")



