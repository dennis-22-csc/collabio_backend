from datetime import datetime, timedelta
import uuid

# Generate timestamp and interval
now = datetime.now()
interval = timedelta(minutes=60)

messages_data = [
    {
        "message_id": str(uuid.uuid4()),
        "sender_name": "Dennis",
        "sender_email": "denniskoko@gmail.com",
        "receiver_name": "Kunle",
        "receiver_email": "kunleajayi@gmail.com",
        "message": "Hi Kunle, how are you?",
        "timestamp": (now - interval * 8).strftime('%Y-%m-%d %H:%M:%S')
    },
    {
        "message_id": str(uuid.uuid4()),
        "sender_name": "Ola",
        "sender_email": "olasmith@gmail.com",
        "receiver_name": "Rachel",
        "receiver_email": "racheloniga@gmail.com",
        "message": "Hi Ola, how are you?",
        "timestamp": (now - interval * 7).strftime('%Y-%m-%d %H:%M:%S')
    },
    {
        "message_id": str(uuid.uuid4()),
        "sender_name": "Dennis",
        "sender_email": "denniskoko@gmail.com",
        "receiver_name": "Alimat",
        "receiver_email": "alimatsadiat@gmail.com",
        "message": "Hi Alimat, how are you?",
        "timestamp": (now - interval * 6).strftime('%Y-%m-%d %H:%M:%S')
    },
    {
        "message_id": str(uuid.uuid4()),
        "sender_name": "Rachel",
        "sender_email": "racheloniga@gmail.com",
        "receiver_name": "Dennis",
        "receiver_email": "denniskoko@gmail.com",
        "message": "Hi Dennis, how are you?",
        "timestamp": (now - interval * 5).strftime('%Y-%m-%d %H:%M:%S')
    },
    {
        "message_id": str(uuid.uuid4()),
        "sender_name": "Kunle",
        "sender_email": "kunleajayi@gmail.com",
        "receiver_name": "Dennis",
        "receiver_email": "denniskoko@gmail.com",
        "message": "Hi Dennis, I'm good.",
        "timestamp": (now - interval * 4).strftime('%Y-%m-%d %H:%M:%S')
    },
    {
        "message_id": str(uuid.uuid4()),
        "sender_name": "Rachel",
        "sender_email": "racheloniga@gmail.com",
        "receiver_name": "Ola",
        "receiver_email": "olasmith@gmail.com",
        "message": "Hi Ola, I'm good.",
        "timestamp": (now - interval * 3).strftime('%Y-%m-%d %H:%M:%S')
    },
    {
        "message_id": str(uuid.uuid4()),
        "sender_name": "Alimat",
        "sender_email": "alimatsadiat@gmail.com",
        "receiver_name": "Dennis",
        "receiver_email": "denniskoko@gmail.com",
        "message": "Hi Dennis, I'm good.",
        "timestamp": (now - interval * 2).strftime('%Y-%m-%d %H:%M:%S')
    },
    {
        "message_id": str(uuid.uuid4()),
        "sender_name": "Dennis",
        "sender_email": "denniskoko@gmail.com",
        "receiver_name": "Rachel",
        "receiver_email": "racheloniga@gmail.com",
        "message": "Hi Rachel, I'm good.",
        "timestamp": (now - interval * 1).strftime('%Y-%m-%d %H:%M:%S')
    }
]
