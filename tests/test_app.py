from app import create_app


def test_health_endpoint_reports_service_status():
    app = create_app()
    response = app.test_client().get("/health")

    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_dashboard_displays_aggregated_synthetic_sales_metrics():
    app = create_app()
    response = app.test_client().get("/")

    assert response.status_code == 200
    page = response.get_data(as_text=True)
    assert "Sales performance dashboard" in page
    assert "Total revenue" in page
    assert "Orders" in page
    assert "Top region" in page
    assert "North" in page
    assert "€10,470" in page
    assert "24" in page
