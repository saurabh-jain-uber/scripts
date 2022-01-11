#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Saurabh Jain (jain.saurabh@uber.com)
# Created Date: 10/01/2021 
# version ='0.1'
# ---------------------------------------------------------------------------

import os
import json
from argparse import ArgumentParser

def check_price_limit(args):
    file, data = get_dict_from_file(args.file_name)
    #gets the items array from the data dictionary
    menu_items = data['items']
    
    for i in menu_items:
        #picks the value of the price variable. Might need changes if the json structure changes in future
        price = i["price_info"]["price"]
        #check if the price of an item is greater than or equal to price limit given by user
        if price >= args.price_limit:
            print(f'ID: {i["id"]}, PRICE: {price}')
    
    close_file(file)

def get_dict_from_file(file_name):
    #reads the json menu file
    file = open(file_name)
    
    #loads the json file as a dict
    data = json.load(file)
    return file, data

def close_file(file):
    file.close()

if __name__=="__main__":
    parser = ArgumentParser()

    #Command line argument for price limit of an item 
    parser.add_argument("-p", "--price-limit",
                        dest="price_limit",
                        help="Price limit per item",
                        default=20000, type=int)

    #Command line argument for json of the menu
    parser.add_argument("-n", "--file-name",
                        dest="file_name",
                        help="Name of the menu JSON file",
                        default="sample_menu.json", type=str)
    
    args = parser.parse_args()

    check_price_limit(args)