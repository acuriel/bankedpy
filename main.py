from bankedpy.payment_session.schemas import PaymentSessionRequest
from bankedpy import BankedClient

client = BankedClient.with_credentials(
    key='pk_test_9Xtn2-Bz-Slemck2wPmUZg', 
    secret='sk_test_e29a981df827266f308a69956eafb206')


args = {
    "reference": "Illuminate",
    "success_url": "https://3c33cc39225337611e80d99bd9c5f230.m.pipedream.net/success?id=__PAYMENT_ID__",
    "error_url": "https://3c33cc39225337611e80d99bd9c5f230.m.pipedream.net/error",
    "line_items": [
      {
        "name": "Candles",
        "amount": 100,
        "currency": "GBP",
        "quantity": 2
      }
    ],
    "payee": {
      "name": "Gerald Wiley",
      "account_number": "12345678",
      "sort_code": "010203"
      },
    "email_receipt": True
}

test = PaymentSessionRequest(**args)

res = client.payment_session.retrieve('7428685e-b4c6-4b61-a5f4-809b4eb4f5c6').json()

print(res)