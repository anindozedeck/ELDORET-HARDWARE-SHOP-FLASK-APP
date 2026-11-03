from flask import Flask, jsonify, render_template_string, request

app = Flask(__name__)

balances = {
    "Melkzadeck Anindo": 12500,
    "Brian Kiptoo": 7800,
    "Ruth Adhiambo": 15300,
    "Daniel Wambua": 8200,
    "Faith Jepchirchir": 9600,
}

HOME_PAGE = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Eldoret Hardware Shop - Customer Balances</title>
  <style>
    body {
      max-width: 38rem;
      margin: 4rem auto;
      padding: 0 1rem;
      color: #202b35;
      font: 1rem/1.5 system-ui, sans-serif;
    }
    main {
      padding: 2rem;
      border: 1px solid #d5dde5;
      border-radius: 0.75rem;
    }
    label, input, button { display: block; }
    input, button {
      box-sizing: border-box;
      width: 100%;
      margin-top: 0.5rem;
      padding: 0.75rem;
      font: inherit;
    }
    button { margin-top: 1rem; cursor: pointer; }
    #result { margin-top: 1.5rem; font-weight: 600; }
  </style>
</head>
<body>
  <main>
    <h1>Eldoret Hardware Shop</h1>
    <p>Check a customer's outstanding balance.</p>
    <form id="balance-form">
      <label for="customer-name">Customer name</label>
      <input id="customer-name" name="name" type="text" required>
      <button type="submit">Search balance</button>
    </form>
    <p id="result" aria-live="polite"></p>
  </main>
  <script>
    const form = document.querySelector("#balance-form");
    const result = document.querySelector("#result");

    form.addEventListener("submit", async (event) => {
      event.preventDefault();
      const name = new FormData(form).get("name").trim();
      result.textContent = "Searching...";

      try {
        const response = await fetch(
          `/api/balance?name=${encodeURIComponent(name)}`
        );
        const data = await response.json();
        result.textContent = response.ok
          ? `${data.customer} owes KSh ${data.balance.toLocaleString()}.`
          : data.error;
      } catch {
        result.textContent = "Unable to retrieve the balance. Please try again.";
      }
    });
  </script>
</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(HOME_PAGE)


@app.route("/api/balance")
def get_balance():
    customer_name = request.args.get("name", "").strip()
    if not customer_name:
        return jsonify({"error": "Please provide a customer name using the 'name' query parameter."}), 400

    for customer, balance in balances.items():
        if customer.casefold() == customer_name.casefold():
            return jsonify({"customer": customer, "balance": balance, "currency": "KES"})

    return jsonify({"error": f"Customer '{customer_name}' not found."}), 404


if __name__ == "__main__":
    app.run(debug=True)