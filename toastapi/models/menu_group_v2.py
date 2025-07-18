# coding: utf-8

"""
    Toast API

    ## Authentication API  The authentication API returns an authentication token that you can present when your integration client software uses other Toast APIs. For more information about authentication, see [the Toast Developer Guide](https://doc.toasttab.com/doc/devguide/authentication.html).  ## Menus API  Returns information about a restaurant's menus.  _Important:_ Ordering integrations should use menus API V3. Other integration types should continue to use menus API V2 until further notice. See <a href=\"https://doc.toasttab.com/doc/devguide/apiComparingMenusAPIV2AndV3.html\">Comparing menus API V2 and V3</a> for more information.  ## Orders API  The orders API includes operations that create, update, and retrieve information about restaurant guest orders.  Information on orders includes the checks, items ordered, prices, payments, discounts, and customer data.  You can create a new order. The orders API includes an operation to retrieve the order prices before you `POST` the order.  You can add items to an existing check.  The orders API also allows you to retrieve payment information for the order and add a credit card payment to the order. You cannot update an existing payment, but you can update the tip amount.  For delivery orders, you can update the delivery information.  You can retrieve the applicable discounts for an order, and then add a discount to a menu item selection or a check.  The orders API supports email addresses that:    - Are up to 53 characters long.    - Start with the email prefix, ends with the email domain name, where the prefix and domain are separated by an @.    - Use the following supported characters:     - a-z     - A-Z     - 0-9     - _ (underscore)     - International characters are not supported  ## Labor API  Toast labor API is a set of REST web services that you can use to  manage the employees, jobs, and shifts for your restaurant. The  labor API is intended for software engineers, managers, and  technical staff who are responsible for integrating third-party  systems with the Toast platform. ## Restaurants API  Returns information about the configuration of restaurant.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from toastapi.models.item_tag_v2 import ItemTagV2
from toastapi.models.menu_item_v2 import MenuItemV2
from typing import Optional, Set
from typing_extensions import Self

class MenuGroupV2(BaseModel):
    """
    Information about a menu group configured for this restaurant, including an array of menu items contained in the group. 
    """ # noqa: E501
    name: Optional[StrictStr] = Field(default=None, description="A descriptive name for this menu group, for example, \"Appetizers\" or \"Sandwiches\". ")
    guid: Optional[StrictStr] = Field(default=None, description="A unique identifier for this menu group, assigned by the Toast POS system. ")
    multi_location_id: Optional[StrictStr] = Field(default=None, description="An identifier that is used to identify and consolidate menu entities that are versions of each other.", alias="multiLocationId")
    master_id: Optional[StrictInt] = Field(default=None, description="This value is deprecated. Instead of masterId, use multiLocationId.", alias="masterId")
    description: Optional[StrictStr] = Field(default=None, description="An optional short description of this menu group. ")
    pos_name: Optional[StrictStr] = Field(default=None, description="The button label name that appears for this menu entity in the Toast POS app.", alias="posName")
    pos_button_color_light: Optional[StrictStr] = Field(default=None, description="The color of the menu entity's button on the Toast POS app, when the app is running in light mode.", alias="posButtonColorLight")
    pos_button_color_dark: Optional[StrictStr] = Field(default=None, description="The color of the menu entity's button on the Toast POS app, when the app is running in dark mode.", alias="posButtonColorDark")
    image: Optional[StrictStr] = Field(default=None, description="The URL to an image that has been uploaded for this menu entity.")
    visibility: Optional[List[StrictStr]] = Field(default=None, description="An array of strings that indicate where this menu entity is visible.")
    item_tags: Optional[List[ItemTagV2]] = Field(default=None, description="An array of `ItemTag` objects that are assigned to this menu group. Item tags are used to assign identifying characteristics, for example, vegetarian, gluten-free, or alcohol. ", alias="itemTags")
    menu_groups: Optional[Annotated[List[MenuGroupV2], Field(min_length=0)]] = Field(default=None, description="An array of the `MenuGroup` objects that are children of this menu group. The array is empty if the menu group has no child menu groups. ", alias="menuGroups")
    menu_items: Optional[Annotated[List[MenuItemV2], Field(min_length=0)]] = Field(default=None, description="An array of the `MenuItem` objects contained in this menu group. ", alias="menuItems")
    __properties: ClassVar[List[str]] = ["name", "guid", "multiLocationId", "masterId", "description", "posName", "posButtonColorLight", "posButtonColorDark", "image", "visibility", "itemTags", "menuGroups", "menuItems"]

    @field_validator('visibility')
    def visibility_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['POS', 'KIOSK', 'GRUBHUB', 'TOAST_ONLINE_ORDERING', 'ORDERING_PARTNERS']):
                raise ValueError("each list item must be one of ('POS', 'KIOSK', 'GRUBHUB', 'TOAST_ONLINE_ORDERING', 'ORDERING_PARTNERS')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of MenuGroupV2 from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in item_tags (list)
        _items = []
        if self.item_tags:
            for _item_item_tags in self.item_tags:
                if _item_item_tags:
                    _items.append(_item_item_tags.to_dict())
            _dict['itemTags'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in menu_groups (list)
        _items = []
        if self.menu_groups:
            for _item_menu_groups in self.menu_groups:
                if _item_menu_groups:
                    _items.append(_item_menu_groups.to_dict())
            _dict['menuGroups'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in menu_items (list)
        _items = []
        if self.menu_items:
            for _item_menu_items in self.menu_items:
                if _item_menu_items:
                    _items.append(_item_menu_items.to_dict())
            _dict['menuItems'] = _items
        # set to None if image (nullable) is None
        # and model_fields_set contains the field
        if self.image is None and "image" in self.model_fields_set:
            _dict['image'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MenuGroupV2 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "guid": obj.get("guid"),
            "multiLocationId": obj.get("multiLocationId"),
            "masterId": obj.get("masterId"),
            "description": obj.get("description"),
            "posName": obj.get("posName"),
            "posButtonColorLight": obj.get("posButtonColorLight"),
            "posButtonColorDark": obj.get("posButtonColorDark"),
            "image": obj.get("image"),
            "visibility": obj.get("visibility"),
            "itemTags": [ItemTagV2.from_dict(_item) for _item in obj["itemTags"]] if obj.get("itemTags") is not None else None,
            "menuGroups": [MenuGroupV2.from_dict(_item) for _item in obj["menuGroups"]] if obj.get("menuGroups") is not None else None,
            "menuItems": [MenuItemV2.from_dict(_item) for _item in obj["menuItems"]] if obj.get("menuItems") is not None else None
        })
        return _obj

# TODO: Rewrite to not use raise_errors
MenuGroupV2.model_rebuild(raise_errors=False)

