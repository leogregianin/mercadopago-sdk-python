# coding: UTF-8

"""
MercadoPago SDK
Search approved credit card payments from 21/10/2011 to 25/10/2011
@date 2012/03/29
@author hcasatti
"""

# Import Mercadopago library
import os, sys
sys.path.append(os.path.dirname(__file__)+"/../../lib")
import mercadopago

import json

def index(req, **kwargs):
    # Create an instance with your MercadoPago credentials (CLIENT_ID and CLIENT_SECRET): 
    # Argentina: https://www.mercadopago.com/mla/herramientas/aplicaciones 
    # Brasil: https://www.mercadopago.com/mlb/ferramentas/aplicacoes
    mp = mercadopago.MP("CLIENT_ID", "CLIENT_SECRET")
    
    filters = {
        "begin_date": "2011-10-21T00:00:00Z",
        "end_date": "2011-10-25T24:00:00Z",
        "payment_type": "credit_card",
        "operation_type": "regular_payment"
    }

    # Search payment data according to filters
    searchResult = mp.search_payment(filters)
    
    # Show payment information
    output = """
    <!doctype html>
    <html>
        <head>
            <title>Search approved credit card payments from 21/10/2011 to 25/10/2011</title>
        </head>
        <body>
            <table border='1'>
                <tr><th>id</th><th>external_reference</th><th>status</th></tr>"""
    for payment in searchResult["response"]["results"]:
        output += "<tr>"
        output += "<td>"+payment["collection"]["id"]+"</td>\n"
        output += "<td>"+payment["collection"]["external_reference"]+"</td>\n"
        output += "<td>"+payment["collection"]["status"]+"</td>\n"
        output += "</tr>"
    output += """
            </table>
        </body>
    </html>
    """
    
    return output
