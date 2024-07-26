import subprocess

def test_list_customers():
    result = subprocess.run(['usepolvo', 'list-customers', '--api-key', 'test_api_key'], capture_output=True, text=True)
    assert result.returncode == 0
    assert "Customer ID" in result.stdout

def test_create_customer():
    result = subprocess.run(['usepolvo', 'create-customer', '--api-key', 'test_api_key', '--email', 'test@example.com'], capture_output=True, text=True)
    assert result.returncode == 0
    assert "Created Customer ID" in result.stdout