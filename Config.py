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
    {
        "filters": {
            "search_text": "Christofle micro mosaic",
            "price_to": 15,
            "order": "newest_first"
        }
    }
]
