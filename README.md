# Website Signup Company

This module ensures that portal users created during website signup or checkout are assigned the correct `company_id` and `company_ids` based on the active website's company.

## Features

- Works for both "account created" and "no account created" checkout flows.
- Sets `company_id` and `company_ids` on the user and partner.
- Compatible with Odoo 14.

## Installation

Clone into your custom addons path:

```bash
git clone https://github.com/l-arnold/website_signup_company.git