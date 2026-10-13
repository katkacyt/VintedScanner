# SMTP Settings for e-mail notification
smtp_username = ""
smtp_psw = ""
smtp_server = ""
smtp_toaddrs = []

# Slack WebHook for notification
slack_webhook_url = ""

# Telegram Token and ChatID for notification
telegram_bot_token = "8958100650:AAEyR0RHLkMKcUdjEP_NlOWli9G3qK_7G4E"
telegram_chat_id = "7278628580"

# Vinted URL: change the TLD according to your country (.fr, .es, etc.)
vinted_url = "https://www.vinted.fr"

# Locale sent to the Vinted API. This can differ for multilingual markets.
vinted_locale = "fr-FR"

# Vinted search queries
queries = [
    # 1. Micro mosaic boite (skrzynki / pudełka w kategorii 1963, do 15 EUR)
    {
        "page": "1",
        "per_page": "24",
        "search_text": "Boite micro mosaic",
        "order": "newest_first",
        "filters": {
            "catalog": ["1963"],
            "price_to": "15",
            "currency": "EUR",
            "status": ["2"]
        }
    },
    # 2. Micro mosaic broche (broszki w kategorii 21, do 8 EUR)
    {
        "page": "1",
        "per_page": "24",
        "search_text": "broche micro mosaïque",
        "order": "newest",
        "filters": {
            "catalog": ["21"],
            "price_to": "8",
            "currency": "EUR"
        }
    },
    # 3. Alabaster (kategoria 1934, do 12 EUR)
    {
        "page": "1",
        "per_page": "24",
        "search_text": "albâtre",
        "order": "relevance",
        "filters": {
            "catalog": ["1934"],
            "price_to": "12",
            "currency": "EUR",
            "color_ids": ["26", "9"]
        }
    },
    # 4. Christofle (kategoria sztućce/srebra 1920, do 25 EUR)
    {
        "page": "1",
        "per_page": "24",
        "search_text": "Christofle",
        "order": "newest_first",
        "filters": {
            "catalog": ["1920"],
            "price_to": "25",
            "currency": "EUR"
        }
    },
    # 5. Ercuis (kategoria 1920, do 25 EUR)
    {
        "page": "1",
        "per_page": "24",
        "search_text": "Ercuis",
        "order": "newest_first",
        "filters": {
            "catalog": ["1920"],
            "price_to": "25",
            "currency": "EUR"
        }
    },
    # 6. Poinçon argent (srebro / cechy probiercze, kategoria 1920, do 20 EUR)
    {
        "page": "1",
        "per_page": "24",
        "search_text": "Poinçon argent",
        "order": "newest_first",
        "filters": {
            "catalog": ["1920"],
            "price_to": "20",
            "currency": "EUR"
        }
    }
]
