# SMTP Settings for e-mail notification
smtp_username = ""
smtp_psw = ""
smtp_server = ""
smtp_toaddrs = []

# Slack WebHook for notification
slack_webhook_url = ""

# Telegram Token and ChatID for notification
telegram_bot_token = "8958100650:AAF3ZJv541cfXBziFDrU4EOUfB10ecu1_oE"
telegram_chat_id = "7278628580"

# Vinted URL: change the TLD according to your country (.fr, .es, etc.)
vinted_url = "https://www.vinted.fr"

# Locale sent to the Vinted API. This can differ for multilingual markets.
vinted_locale = "fr-FR"

queries = [
    # 1. Micro mosaic boite
    {
        "page": "1",
        "per_page": "24",
        "search_text": "Boite micro mosaic",
        "order": "newest_first",
        "price_to": "15",
        "currency": "EUR",
        "filters": {
            "catalog": ["1963"],
            "brand": [],
            "size": [],
            "status": ["2"],
            "color": [],
            "material": [],
        }
    },
    # 2. Micro mosaic broche
    {
        "page": "1",
        "per_page": "24",
        "search_text": "broche micro mosaïque",
        "order": "newest_first",
        "price_to": "8",
        "currency": "EUR",
        "filters": {
            "catalog": ["21"],
            "brand": [],
            "size": [],
            "status": [],
            "color": [],
            "material": [],
        }
    },

    # 2. Micro mosaic broche
    {
        "page": "1",
        "per_page": "24",
        "search_text": " micro mosaïque",
        "order": "newest_first",
        "price_to": "12",
        "currency": "EUR",
        "filters": {
            "catalog": ["14"],
            "brand": [],
            "size": [],
            "status": [],
            "color": [],
            "material": [],
        }
    },  # <--- TUTAJ BRAKOWAŁO ZAMKNIĘCIA KLAWIATURY I PRZECINKA

    # 3. Alabaster
    {
        "page": "1",
        "per_page": "24",
        "search_text": "albâtre",
        "order": "newest_first",
        "price_to": "12",
        "currency": "EUR",
        "filters": {
            "catalog": ["1934"],
            "brand": [],
            "size": [],
            "status": [],
            "color": [
                "3", "9", "27", "17",  # Niebieskie i Turkus
                "30", "7", "28", "16", # Zielenie i Oliwki
                "24", "5", "8", "23",  # Róż, Czerwień i Bordo
                "29", "6",             # Fiolety i Lawenda
                "11", "10"             # Pomarańcz/Bursztyn oraz Wielokolorowe (dodatkowe)
            ],
            "material": [],
        }
    },

    {
        "page": "1",
        "per_page": "24",
        "search_text": "boite pivoter",
        "order": "newest_first",
        "price_to": "10",
        "currency": "EUR",
        "filters": {
            "catalog": [],
            "brand": [],
            "size": [],
            "status": [],
            "color": ["4"],
            "material": [],
        }
    },

    {
        "page": "1",
        "per_page": "24",
        "search_text": "boite compartimente",
        "order": "newest_first",
        "price_to": "10",
        "currency": "EUR",
        "filters": {
            "catalog": [],
            "brand": [],
            "size": [],
            "status": [],
            "color": ["4"],
            "material": [],
        }
    },

    {
        "page": "1",
        "per_page": "24",
        "search_text": "boite tuya",
        "order": "newest_first",
        "price_to": "7",
        "currency": "EUR",
        "filters": {
            "catalog": [],
            "brand": [],
            "size": [],
            "status": [],
            "color": ["4"],
            "material": [],
        }
    },

    {
        "page": "1",
        "per_page": "24",
        "search_text": "boite marocaine",
        "order": "newest_first",
        "price_to": "7",
        "currency": "EUR",
        "filters": {
            "catalog": [],
            "brand": [],
            "size": [],
            "status": [],
            "color": ["4"],
            "material": [],
        }
    },

    {
        "page": "1",
        "per_page": "24",
        "search_text": "caja madera tuya",
        "order": "newest_first",
        "price_to": "10",
        "currency": "EUR",
        "filters": {
            "catalog": [],
            "brand": [],
            "size": [],
            "status": [],
            "color": ["4"],
            "material": [],
        }
    } #,
    # test
  #  {
  #      "page": "1",
   #     "per_page": "10",
   #     "search_text": "nike",
  #      "order": "newest_first",
  #      "price_to": "60",
   #     "currency": "EUR",
   #     "filters": {}
  #  }
]
