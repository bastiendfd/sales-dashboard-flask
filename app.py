from flask import Flask, jsonify, render_template_string

SALES_DATA = (
    {"region": "North", "category": "Software", "revenue": 3820, "orders": 8},
    {"region": "South", "category": "Services", "revenue": 2760, "orders": 6},
    {"region": "West", "category": "Software", "revenue": 2310, "orders": 5},
    {"region": "East", "category": "Hardware", "revenue": 1580, "orders": 5},
)

DASHBOARD_TEMPLATE = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Sales Dashboard</title>
  <style>
    body { background: #f5f7fb; color: #172033; font-family: Arial, sans-serif; margin: 0; }
    main { margin: 0 auto; max-width: 960px; padding: 48px 24px; }
    h1 { margin-bottom: 6px; } .subtle { color: #5f6b80; }
    .metrics { display: grid; gap: 16px; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); margin: 32px 0; }
    .card, .panel { background: white; border: 1px solid #e2e8f0; border-radius: 12px; padding: 20px; }
    .label { color: #5f6b80; font-size: .9rem; margin: 0; } .value { font-size: 2rem; font-weight: 700; margin: 8px 0 0; }
    table { border-collapse: collapse; width: 100%; } th, td { border-bottom: 1px solid #e2e8f0; padding: 12px 8px; text-align: left; }
    th { color: #5f6b80; font-size: .85rem; text-transform: uppercase; } td:last-child, th:last-child { text-align: right; }
  </style>
</head>
<body>
  <main>
    <header>
      <h1>Sales performance dashboard</h1>
      <p class="subtle">Local demo using embedded synthetic sales data.</p>
    </header>
    <section class="metrics" aria-label="Key metrics">
      <article class="card"><p class="label">Total revenue</p><p class="value">€{{ "{:,}".format(metrics.revenue) }}</p></article>
      <article class="card"><p class="label">Orders</p><p class="value">{{ metrics.orders }}</p></article>
      <article class="card"><p class="label">Average order value</p><p class="value">€{{ "{:,}".format(metrics.average_order_value) }}</p></article>
      <article class="card"><p class="label">Top region</p><p class="value">{{ metrics.top_region }}</p></article>
    </section>
    <section class="panel" aria-labelledby="region-heading">
      <h2 id="region-heading">Revenue by region</h2>
      <table>
        <thead><tr><th>Region</th><th>Category</th><th>Orders</th><th>Revenue</th></tr></thead>
        <tbody>{% for sale in sales %}<tr><td>{{ sale.region }}</td><td>{{ sale.category }}</td><td>{{ sale.orders }}</td><td>€{{ "{:,}".format(sale.revenue) }}</td></tr>{% endfor %}</tbody>
      </table>
    </section>
  </main>
</body>
</html>"""


def dashboard_metrics(sales: tuple[dict, ...]) -> dict[str, int | str]:
    revenue = sum(sale["revenue"] for sale in sales)
    orders = sum(sale["orders"] for sale in sales)
    top_sale = max(sales, key=lambda sale: sale["revenue"], default=None)
    return {
        "revenue": revenue,
        "orders": orders,
        "average_order_value": revenue // orders if orders else 0,
        "top_region": top_sale["region"] if top_sale else "—",
    }


def create_app() -> Flask:
    app = Flask(__name__)

    @app.get("/")
    def dashboard():
        return render_template_string(
            DASHBOARD_TEMPLATE, metrics=dashboard_metrics(SALES_DATA), sales=SALES_DATA
        )

    @app.get("/health")
    def health():
        return jsonify(status="ok")

    return app


app = create_app()


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
