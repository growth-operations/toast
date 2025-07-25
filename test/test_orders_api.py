# coding: utf-8

"""
    Toast API

    ## Authentication API  The authentication API returns an authentication token that you can present when your integration client software uses other Toast APIs. For more information about authentication, see [the Toast Developer Guide](https://doc.toasttab.com/doc/devguide/authentication.html).  ## Menus API  Returns information about a restaurant's menus.  _Important:_ Ordering integrations should use menus API V3. Other integration types should continue to use menus API V2 until further notice. See <a href=\"https://doc.toasttab.com/doc/devguide/apiComparingMenusAPIV2AndV3.html\">Comparing menus API V2 and V3</a> for more information.  ## Orders API  The orders API includes operations that create, update, and retrieve information about restaurant guest orders.  Information on orders includes the checks, items ordered, prices, payments, discounts, and customer data.  You can create a new order. The orders API includes an operation to retrieve the order prices before you `POST` the order.  You can add items to an existing check.  The orders API also allows you to retrieve payment information for the order and add a credit card payment to the order. You cannot update an existing payment, but you can update the tip amount.  For delivery orders, you can update the delivery information.  You can retrieve the applicable discounts for an order, and then add a discount to a menu item selection or a check.  The orders API supports email addresses that:    - Are up to 53 characters long.    - Start with the email prefix, ends with the email domain name, where the prefix and domain are separated by an @.    - Use the following supported characters:     - a-z     - A-Z     - 0-9     - _ (underscore)     - International characters are not supported  ## Labor API  Toast labor API is a set of REST web services that you can use to  manage the employees, jobs, and shifts for your restaurant. The  labor API is intended for software engineers, managers, and  technical staff who are responsible for integrating third-party  systems with the Toast platform. ## Restaurants API  Returns information about the configuration of restaurant.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from toastapi.api.orders_api import OrdersApi


class TestOrdersApi(unittest.IsolatedAsyncioTestCase):
    """OrdersApi unit test stubs"""

    async def asyncSetUp(self) -> None:
        self.api = OrdersApi()

    async def asyncTearDown(self) -> None:
        await self.api.api_client.close()

    async def test_orders_bulk_get(self) -> None:
        """Test case for orders_bulk_get

        Get multiple orders
        """
        pass

    async def test_orders_get(self) -> None:
        """Test case for orders_get

        Get order identifiers (deprecated)
        """
        pass

    async def test_orders_guid_get(self) -> None:
        """Test case for orders_guid_get

        Get an order
        """
        pass

    async def test_orders_order_guid_checks_check_guid_selections_post(self) -> None:
        """Test case for orders_order_guid_checks_check_guid_selections_post

        Add items to a check
        """
        pass

    async def test_orders_order_guid_delivery_info_patch(self) -> None:
        """Test case for orders_order_guid_delivery_info_patch

        Update delivery information
        """
        pass

    async def test_orders_post(self) -> None:
        """Test case for orders_post

        Post an order
        """
        pass

    async def test_prices_post(self) -> None:
        """Test case for prices_post

        Get order prices
        """
        pass

    async def test_void_order(self) -> None:
        """Test case for void_order

        Void an order
        """
        pass


if __name__ == '__main__':
    unittest.main()
