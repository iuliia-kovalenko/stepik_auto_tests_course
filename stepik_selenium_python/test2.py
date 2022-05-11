from yookassa import Refund, Configuration
import uuid

Configuration.account_id = "824834"
Configuration.secret_key = "test_yo8TGYEaib9QpBUOBSfJMZVd7pHhytkszQZdN--M4mM"

idempotence_key = str(uuid.uuid4())
refund = Refund.create({
    "amount": {
        "value": "777.00",
        "currency": "RUB"
    },
    "sources": [
            {
                "account_id": "839362",
                "amount": {
                    "value": "777.00",
                    "currency": "RUB"
                }
            }
        ],
    "payment_id": "2a04b7b7-000f-5000-9000-1bd07a518c2f"
}, idempotence_key)

print(refund.json())
