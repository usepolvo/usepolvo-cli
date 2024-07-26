import click
import asyncio
from usepolvo.stripe.customers import StripeCustomerClient
from src.config import get_api_key

@click.group()
def stripe():
    """Stripe integration commands."""
    pass

@click.command()
def list_customers():
    """List customers in Stripe."""
    api_key = get_api_key('stripe')
    if not api_key:
        click.echo("Stripe API key is not configured. Please run 'usepolvo config stripe --api-key <your_api_key>' to configure it.")
        return
    client = StripeCustomerClient(api_key)
    asyncio.run(_list_customers(client))

async def _list_customers(client):
    customers = await client.list_customers()
    for customer in customers:
        click.echo(f'Customer ID: {customer.id}, Email: {customer.email}')

@click.command()
@click.option('--email', prompt='Customer Email', help='The email of the customer.')
def create_customer(email):
    """Create a new customer in Stripe."""
    api_key = get_api_key('stripe')
    if not api_key:
        click.echo("Stripe API key is not configured. Please run 'usepolvo config stripe --api-key <your_api_key>' to configure it.")
        return
    client = StripeCustomerClient(api_key)
    asyncio.run(_create_customer(client, email))

async def _create_customer(client, email):
    customer = await client.create_customer(email=email)
    click.echo(f'Created Customer ID: {customer.id}, Email: {customer.email}')

stripe.add_command(list_customers)
stripe.add_command(create_customer)