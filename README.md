## Item price limit exceeded detection script

This script can be used to detect if any item in the items arrays has price over the accepted limit. The price limit can be passed as an argument to the script. Following menu structure is needed to use this script.

> items -> price_info -> price is used to check the price limit

```
{
    "menus": [
        {
            "id": "Specials",
            "title": {
                "translations": {
                    "en": "Specials"
                }
            },
            "service_availability": [
                
            ],
            "category_ids": [

            ]
        }
    ],
    "categories": [
        {
            "id": "Specials_98385",
            "title": {
                "translations": {
                    "en": "Specials"
                }
            },
            "entities": [
                {
                    "id": "Best_Burger"
                }
            ]
        }
    ],
    "items": [
        {
            "id": "Best_Burger",
            "title": {
                "translations": {
                    "en": "Best Burger"
                }
            },
            "description": {
                "translations": {
                    "en": "auce, habenero hot sauce, pickles and white bread"
                }
            },
            "image_url": "https://duyt4h9nfnj50.cloudfront.net/sku/f2a668b94427c1a9b849ec50941cdbc0",
            "price_info": {
                "price": 100,
                "overrides": []
            },
            "tax_info": {},
            "dish_info": {
                "classifications": {}
            },
            "tax_label_info": {
                "default_value": {
                    "labels": [
                        "TEMP_HEATED",
                        "CAT_PREPARED_FOOD"
                    ],
                    "source": "DEFAULT"
                }
            },
            "bundled_items": null
        }
    ],
    "modifier_groups": null,
    "display_options": {
        "disable_item_instructions": true
    }
}
```
### How to run the script
`python3 menu_price_checker.py -n sample_menu.json -p 20000`
or
`python3 menu_price_checker.py --file-name sample_menu.json --price-limit 20000`

### Available arguments
- --file-name or -n : Name of the sample menu in json format. 
- --price-limit or -p : Price limit of the items.