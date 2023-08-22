import pandas as pd

data = [
    {
        "role": "SYSTEM",
        "username": "Deva",
        "content": "Hello, I am Deva. I am a chatbot. I am here to help you with your queries.",
    }
]

chdf = pd.DataFrame(data, columns=["role", "username", "content"])
chdf.role = chdf.role.astype("category")
chdf.role = chdf.role.cat.add_categories(("BOT", "USER"))
