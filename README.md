## Record Details In List View - Base

This module provides a base module to show the record details in list view.
For example, you can show a table with order lines of the sale order in the sale
list view, by quickly inheriting the sale module and add a method fetching the
sale order data.

## Usage

1. Install this module.
2. Create a module which inehrits the model where you want to show the record details
3. Add a method `fetch_record_details` in the model which return a string with HTML data

## Known Issues

1. If any model has a separate implementation for list view, then they might require model specific
   changes like the ones did for purchase order. (Check `record_details_list_purchase` module)




https://github.com/user-attachments/assets/b0bbc4c5-c3af-4dbd-b272-f7965c09e710




## Disclaimer

1. There maybe some css issues, you have been warned.
