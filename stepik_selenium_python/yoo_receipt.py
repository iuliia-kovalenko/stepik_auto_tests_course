from yookassa import Receipt, Configuration
import uuid

Configuration.account_id = "824834"
Configuration.secret_key = "test_yo8TGYEaib9QpBUOBSfJMZVd7pHhytkszQZdN--M4mM"

idempotence_key = str(uuid.uuid4())
response = Receipt.create({
    "customer": {
        "full_name": "Иванов Иван Иванович",
        "email": "email@email.ru",
        "phone": "79000000000",
        # "inn": "6321000014"
    },

    "refund_id": "2a04b88c-0015-5000-9000-13b762ca0907",
    "type": "refund",
    "send": True,
    "items": [
        {
            "description": "test_2 839362",
            "quantity": "1",
            "amount": {
                "value": "777.00",
                "currency": "RUB"
            },
            "vat_code": "2",
            "payment_mode": "full_payment",
            "payment_subject": "service",
            "agent_type": "agent",
            "supplier": {
                "full_name": "ООО Ромашка",
                "email": "email@email.ru",
                "phone": "79000000000",
                "inn": "6666666666"
            },

            # "country_of_origin_code": "CN",
        }
    ],
    "settlements": [
        {
            "type": "cashless",
            "amount": {
                "value": "777.00",
                "currency": "RUB"
            },
        }
    ],
    "on_behalf_of": "839362",
    "tax_system_code": 1,
}, idempotence_key)
