
# Student Management Module – Odoo 19

A custom Student Management module developed using Odoo 19, Python and XML. This module manages student records, departments and courses, with features for student status tracking, age validation, fee calculation and PDF report generation.

## Features

- **Student Management:** Create and manage student records.
- **Department Management:** Organise students by department.
- **Course Management:** Create and manage courses.
- **Student Status Workflow:** New, Active and Graduated.
- **Age Validation:** Validate student age using Python constraints.
- **Age Warning:** Display warnings using `@api.onchange`.
- **Fee Calculation:** Automatically calculate total fees using computed fields.
- **PDF Reports:** Generate student reports using QWeb.

## Technologies Used

- Odoo 19
- Python
- XML
- PostgreSQL

## Odoo Concepts Implemented

- Odoo ORM and custom models
- Model inheritance
- Many2one, One2many and Many2many relationships
- List, Form and Search views
- Computed fields
- `@api.onchange` and `@api.constrains`
- Status workflows and business logic
- XML actions and menus
- Access rights and security
- QWeb PDF reports

## Installation

1. Clone the repository:

   ```bash
   git clone -b 19.0 https://github.com/safa-noora/student-management-odoo.git
   ```

2. Copy the student_management folder into your Odoo custom addons directory.
3. Add the custom addons directory to your Odoo configuration file's addons_path.
4. Restart the Odoo server.
5. Enable Developer Mode in Odoo.
6. Update the Apps List, search for Student Management, and install the module.

## Author

**Safa Noora K K**

B.Tech – Computer Science and Engineering (2026)

GitHub: https://github.com/safa-noora
