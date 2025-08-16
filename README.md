# Website Signup Company

## Overview

`website_signup_company` is an Odoo 14 module that ensures portal users created via website signup are correctly assigned to the appropriate company context. It supports multi-company setups and synchronizes company access between users and their related partners.

## Multi-Company Signup Behavior

This module ensures that new users created via the website signup flow are correctly assigned to the company context of the website they signed up on. It also synchronizes the user's allowed companies with their related partner record to prevent company mismatch errors during checkout or portal access.

### Key Features

- Sets `res.users.company_id` to the website's company during signup
- Mirrors `res.users.company_ids` to `res.partner.company_ids`
- Ensures `res.partner.company_id` matches the website company
- Keeps partner company access in sync when user access is updated

### Technical Notes

- Signup logic is handled via model overrides in:
  - `models/signup_partner_company_sync.py` (signup-time sync)
  - `models/user_partner_company_sync.py` (post-signup sync)
- Debug logging is included to trace sync behavior in Odoo logs
- No changes are made to guest checkout flows or public user behavior

#### Example Log Output

```text
INFO signup_partner_company_sync: Signup sync: partner.company_ids set to [1, 2, 3] for user 14567
INFO user_partner_company_sync: Update sync: partner.company_ids updated to [1, 2] for user 14567  
```

#### Compatibility
Tested on Odoo 14.0

Compatible with multi-company setups using multiple websites

Designed to work alongside modules like website_sale_suggest_create_account

#### Legacy Notes from Version 1
The following section reflects the original README from the first iteration of this module, before model-based sync logic was introduced.

# Features
Works for both "account created" and "no account created" checkout flows

Sets company_id and company_ids on the user and partner based upon the Portal Template USER

Compatible with Odoo 14

# Installation
Clone into your custom addons path:

git clone git@github.com:l-arnold/website_signup_company.git --branch 14.0

