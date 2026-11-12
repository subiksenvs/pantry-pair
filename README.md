# Pantry Pair — AI kitchen studio

Pantry Pair combines a kitchen inventory, expiry awareness, recipe matching, AI meal suggestions, saved recipes, and a shopping list. It helps reduce forgotten ingredients and makes meal planning easier without making nutrition or medical claims.

## Features

- Inventory with quantities, categories, and best-before dates.
- “Use soon” counter for ingredients expiring within three days.
- Recipe ranking based on pantry overlap and preparation time.
- Optional AI meal suggestions from the pantry, servings, and cooking preferences.
- Save recipe ideas, add missing ingredients to a shopping list, and check items off.
- Persistent local SQLite database with JSON API endpoints.
- Works in demo mode without an AI key.

## Stack and run

Python 3.13+, Django 5.2, SQLite, server-rendered Django templates, and a small fetch-based client. No build chain is required.

```sh
py -3.13 -m venv .venv
```

Activate the environment, then run:

```sh
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open `http://127.0.0.1:8000`.

## AI configuration

Set `OPENAI_API_KEY` in the server environment and optionally `OPENAI_MODEL` (default `gpt-6-astra`). The browser never receives the key. Without a key, Pantry Pair returns local recipe matches. Never add a real key to Git; see the [official OpenAI quickstart](https://developers.openai.com/api/docs/quickstart).

## Endpoints

`GET/POST /api/pantry`, `PATCH/DELETE /api/pantry/:id`, `POST /api/recipes/suggest`, `GET/POST /api/recipes`, `DELETE /api/recipes/:id`, `GET/POST /api/shopping`, `PATCH/DELETE /api/shopping/:id`, and `GET /api/metrics`.

## Verify

```sh
python manage.py test
```

This is a local kitchen workspace, not a medical or allergen-safety product. Check ingredients and allergy risks yourself.
