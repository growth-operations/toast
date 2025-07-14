# Toast API Client Wrapper

A simplified wrapper around the generated OpenAPI client that provides automatic authentication, retry logic, and easy access to all Toast API endpoints.

## Features

- **Automatic Authentication**: Handles OAuth2 token management automatically
- **Retry Logic**: Built-in retry mechanism with exponential backoff
- **Simplified API Access**: Easy access to all API endpoints through a single client
- **Async Support**: Full async/await support for all operations
- **Context Manager**: Use with `async with` for automatic cleanup
- **Token Management**: Automatic token refresh and expiration handling

## Installation

The client wrapper is included with the generated Toast API client. Make sure you have the required dependencies:

```bash
pip install -r requirements.txt
```

## Quick Start

```python
import asyncio
from toasttab import Toast, RetryConfig

async def main():
    # Initialize the client
    async with Toast(
        client_id="your_client_id",
        client_secret="your_client_secret",
        environment="sandbox"  # or "production"
    ) as toast:
        
        # Get orders (authentication happens automatically)
        orders = await toast.orders.orders_get()
        print(f"Found {len(orders.orders)} orders")
        
        # Get employees
        employees = await toast.employees.employees_get()
        print(f"Found {len(employees.employees)} employees")

asyncio.run(main())
```

## Configuration

### Basic Configuration

```python
from toasttab import Toast

# Sandbox environment (for testing)
toast = Toast(
    client_id="your_client_id",
    client_secret="your_client_secret",
    environment="sandbox"
)

# Production environment
toast = Toast(
    client_id="your_client_id",
    client_secret="your_client_secret",
    environment="production"
)

# Custom host URL
toast = Toast(
    client_id="your_client_id",
    client_secret="your_client_secret",
    host="https://custom-oauth.toasttab.com"
)
```

### Retry Configuration

```python
from toasttab import Toast, RetryConfig

# Custom retry configuration
retry_config = RetryConfig(
    max_retries=5,           # Maximum number of retry attempts
    base_delay=2.0,          # Initial delay between retries (seconds)
    max_delay=30.0,          # Maximum delay between retries (seconds)
    backoff_factor=1.5,      # Multiplier for delay after each retry
    retry_on_exceptions=(Exception,),  # Exceptions to retry on
)

toast = Toast(
    client_id="your_client_id",
    client_secret="your_client_secret",
    environment="sandbox",
    retry_config=retry_config
)
```

### Custom Retry Conditions

```python
from toasttab import Toast, RetryConfig

def should_retry(exception):
    """Custom retry condition."""
    # Only retry on network errors, not authentication errors
    return "network" in str(exception).lower()

retry_config = RetryConfig(
    max_retries=3,
    retry_condition=should_retry
)

toast = Toast(
    client_id="your_client_id",
    client_secret="your_client_secret",
    retry_config=retry_config
)
```

## Available API Endpoints

The client provides access to all Toast API endpoints through the following properties:

- `toast.auth` - Authentication API
- `toast.orders` - Orders API
- `toast.employees` - Employees API
- `toast.jobs` - Jobs API
- `toast.shifts` - Shifts API
- `toast.time_entries` - Time Entries API
- `toast.payments` - Payments API
- `toast.discounts` - Discounts API
- `toast.default` - Default API

## Usage Examples

### Authentication

```python
async with Toast(client_id="...", client_secret="...") as toast:
    # Authentication happens automatically on first API call
    # You can also manually authenticate:
    token = await toast.authenticate()
    print(f"Token: {token}")
    
    # Check if token is valid
    if toast.is_token_valid():
        print("Token is still valid")
```

### Working with Orders

```python
async with Toast(client_id="...", client_secret="...") as toast:
    # Get all orders
    orders_response = await toast.orders.orders_get()
    
    # Get orders with filters
    orders_response = await toast.orders.orders_get(
        start_date="2024-01-01",
        end_date="2024-01-31"
    )
    
    # Get a specific order
    order = await toast.orders.orders_guid_get("order-guid-here")
    
    # Create a new order
    from toasttab.models import OrderRequest
    new_order = OrderRequest(...)
    created_order = await toast.orders.orders_post(new_order)
```

### Working with Employees

```python
async with Toast(client_id="...", client_secret="...") as toast:
    # Get all employees
    employees_response = await toast.employees.employees_get()
    
    # Get a specific employee
    employee = await toast.employees.employees_guid_get("employee-guid-here")
    
    # Get employee jobs
    jobs = await toast.employees.employees_guid_jobs_get("employee-guid-here")
```

### Working with Shifts

```python
async with Toast(client_id="...", client_secret="...") as toast:
    # Get all shifts
    shifts_response = await toast.shifts.shifts_get()
    
    # Get shifts for a specific employee
    employee_shifts = await toast.shifts.shifts_get(
        employee_guid="employee-guid-here"
    )
    
    # Get shifts within a date range
    shifts = await toast.shifts.shifts_get(
        start_date="2024-01-01",
        end_date="2024-01-31"
    )
```

### Working with Payments

```python
async with Toast(client_id="...", client_secret="...") as toast:
    # Get all payments
    payments_response = await toast.payments.payments_get()
    
    # Get payments for a specific order
    order_payments = await toast.payments.payments_get(
        order_guid="order-guid-here"
    )
```

### Error Handling

```python
async with Toast(client_id="...", client_secret="...") as toast:
    try:
        orders = await toast.orders.orders_get()
    except Exception as e:
        print(f"Error fetching orders: {e}")
        # The client will automatically retry based on the retry configuration
```

## Environment Variables

You can use environment variables for credentials:

```python
import os
from toasttab import Toast

async def main():
    async with Toast(
        client_id=os.getenv("TOAST_CLIENT_ID"),
        client_secret=os.getenv("TOAST_CLIENT_SECRET"),
        environment="sandbox"
    ) as toast:
        # Your code here
        pass
```

## Token Management

The client automatically handles token management:

```python
async with Toast(client_id="...", client_secret="...") as toast:
    # Get current token
    token = toast.token
    
    # Check if token is valid
    is_valid = toast.is_token_valid()
    
    # Get token expiration time
    expires_at = toast.token_expires_at
    
    # Manually refresh token
    new_token = await toast.authenticate()
```

## Advanced Usage

### Custom API Client Configuration

```python
from toasttab import Toast, Configuration

# Create custom configuration
config = Configuration(
    host="https://custom-oauth.toasttab.com",
    debug=True  # Enable debug logging
)

# Use custom configuration
toast = Toast(
    client_id="...",
    client_secret="...",
    host="https://custom-oauth.toasttab.com"
)
```

### Manual Authentication Flow

```python
async with Toast(client_id="...", client_secret="...") as toast:
    # Authenticate manually
    token = await toast.authenticate()
    
    # Use the token for other operations
    orders = await toast.orders.orders_get()
    
    # Check token validity
    if not toast.is_token_valid():
        # Re-authenticate
        await toast.authenticate()
```

## Troubleshooting

### Common Issues

1. **Authentication Errors**: Make sure your `client_id` and `client_secret` are correct
2. **Network Errors**: The client will automatically retry on network errors
3. **Token Expiration**: The client automatically refreshes expired tokens
4. **Rate Limiting**: The retry mechanism helps handle rate limiting

### Debug Mode

Enable debug mode to see detailed API requests and responses:

```python
from toasttab import Toast, Configuration

config = Configuration(debug=True)
toast = Toast(
    client_id="...",
    client_secret="...",
    environment="sandbox"
)
```

## API Reference

For detailed API documentation, see the generated OpenAPI client documentation. The wrapper provides the same methods as the underlying API classes, but with automatic authentication and retry logic.

## Contributing

The client wrapper is designed to be simple and maintainable. If you need additional features or have suggestions, please open an issue or submit a pull request. 