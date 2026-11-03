# Eldoret Hardware Shop Balance Lookup

A small Flask web app for looking up customer credit balances. The home page provides a search form, and the API returns a customer's balance as JSON. Customer names and balances are currently hardcoded in `Day16_exercise.py` for demonstration.

## Requirements

- Python 3
- Flask (`python -m pip install flask`)

## Run locally

From this folder, start the app:

```powershell
python Day16_exercise.py
```

Open [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in a browser and search for a customer. Stop the server with `Ctrl+C`.

## Routes

- `GET /` — serves the shop page and customer search form.
- `GET /api/balance?name=<customer name>` — returns a matching balance as JSON. Names are matched without regard to letter case.

For example, `/api/balance?name=Melkzadeck%20Anindo` returns:

```json
{
  "customer": "Melkzadeck Anindo",
  "balance": 12500,
  "currency": "KES"
}
```

The API returns HTTP 400 if the `name` parameter is missing and HTTP 404 if the customer is not found.

## Price

I would charge a hardware shop owner **KES 15,000** for this tool.
