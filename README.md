# CRM banking

CRM banking is a CRM system for financial companies, which helps to hold clients' databases and fixes the history of all actions with clients. 

Description:

CRM banking is a CRM system helps to:
- manage users
- hold contact's databases,
- propose financial products,
- create contacts,
- import & export contact's data from/in the CSV-file
- check contacts via external API
- create contracts, when the interest grown to agreeing of client to make a deal.

## Installation

Install [sqlite3](https://www.sqlite.org/download.html/) database.

Install the requirement using the package manager [pip](https://pip.pypa.io/en/stable/).

    pip install --requirement requirements.txt

## Usage

Run 'Main'.
In Python console:
1. Enter username and password. For the first login use test/test. Only logged users can create new users.
2. Follow the recommendations in Console:
   1) Choose section! 
   1 - Contacts, 2 - Contracts, 3 - Leads, 4 - Users, 5 - Products, 0 - Exit
   2) Choose operation in section: 
      1) Contacts.
      1 - Create, 2 - Get info, 3 - Import from file, 4 - Export to file, 9 - Go to Section, 0 - Exit
      2) Contracts.
      1 - Create, 2 - Get info, 9 - Go to Section, 0 - Exit
      3) Leads.
      9 - Go to Section, 0 - Exit
      4) Users.
      1 - Create, 2 - Get info, 9 - Go to Section, 0 - Exit
      5) Products.
      9 - Go to Section, 0 - Exit

3. There is possible to check the age and gender by the name of the contact. 
It automatically works when creating a contract. Or manually need to run functions: 
checks/public_data/get_age_by_name
checks/public_data/get_gender_by_name
4. Show log: Log file is located in the root folder of the application with name: my_log_{currentdate}.log.
5. Run Pytest: TBD

## Support

Feel free to contact me by e-mail at dnytsyk@gmail.com if you have any questions related to my project.

## Roadmap

In future releases, I will plan to add features:
- graphic user interface,
- extended financial product,
- add new functional roles (system administrator, etc),
- support databases MySQL and PostgreSQL.

## Authors and acknowledgment

I appreciate my teachers in ReDI school teaching me and support while creating the project.
