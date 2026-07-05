# Test Plan: SauceDemo E-Commerce Application

## 1. Overview

This document outlines the test strategy for a QA automation portfolio project targeting
[SauceDemo](https://www.saucedemo.com), a publicly available e-commerce demo application
built specifically for QA/automation practice.

This project is intended to demonstrate practical QA engineering skills: test planning,
test case design, risk-based prioritization, and automation implementation using
Playwright (Python) and pytest.

## 2. Scope

### In Scope
- **Authentication**: login with valid, invalid, and edge-case credentials
- **Product Sorting/Filtering**: verifying sort behavior (name, price, ascending or descending)
- **Shopping Cart**: adding/removing items, cart state persistence
- **Checkout Flow**: full purchase path, form validation, order confirmation

### Out of Scope
- Performance/load testing
- Security/penetration testing
- Cross-browser compatibility testing (this suite runs against Chromium only)
- API-level testing (SauceDemo does not expose a public API for this purpose)
- Mobile/responsive layout testing

> Scoping decisions reflect what can be meaningfully and safely tested against a public
> demo site, while still demonstrating end-to-end functional coverage of the application's
> core purchase flow, the highest-risk path in any e-commerce application.

## 3. Test Approach

This suite uses a mix of:
- **Positive testing**: confirming expected behavior under normal conditions
- **Negative testing**: confirming the system fails gracefully under invalid conditions
  (e.g., locked accounts, empty required fields)
- **Boundary/edge case testing**: e.g., empty cart checkout, special characters in form
  fields

Automated tests are implemented using **Playwright (Python)** with **pytest** as the test
runner, following the **Page Object Model (POM)** pattern to separate page structure from
test logic, improving maintainability and readability as the suite grows.

## 4. Test Environment

| Item | Detail |
|---|---|
| Application Under Test | https://www.saucedemo.com |
| Browser | Chromium (via Playwright) |
| Test Framework | pytest |
| Automation Tool | Playwright (Python) |
| Test Accounts | Provided by SauceDemo (see Section 5) |

## 5. Test Data Strategy

SauceDemo provides a fixed set of test accounts, each simulating a different real-world
scenario. This suite intentionally uses each account for its designed purpose rather than
defaulting to `standard_user` everywhere, since account-specific behavior is itself part of
what needs coverage:

| Account | Purpose | Used In |
|---|---|---|
| `standard_user` | Baseline "everything works" scenario | Positive test cases across all flows |
| `locked_out_user` | Simulates a disabled/blocked account | Negative login test cases |
| `problem_user` | Simulates UI rendering issues (e.g., broken images) | UI-integrity checks |
| `performance_glitch_user` | Simulates slow-loading pages | Noted as a candidate for future performance-aware test design (out of scope for functional suite) |

All passwords for these accounts are `secret_sauce`, per SauceDemo's public documentation.
No real or sensitive credentials are used anywhere in this project.

## 6. Risk-Based Prioritization

| Area | Priority | Rationale |
|---|---|---|
| Checkout flow | **High** | Directly maps to revenue-critical path; failures here have the highest business impact |
| Login/authentication | **High** | Gatekeeper for all downstream functionality; must fail securely and predictably |
| Cart management | **Medium** | Affects usability and trust, but failures are typically recoverable by the user |
| Sorting/filtering | **Low–Medium** | Affects usability/discoverability, not transaction completion |

## 7. Entry & Exit Criteria

**Entry criteria:**
- Application is publicly accessible at the URL above
- Test accounts are available and functioning as documented

**Exit criteria:**
- All High-priority test cases pass, or failures are documented as known issues with
  supporting bug reports
- Test coverage summary is up to date in the project README

## 8. Deliverables

- `docs/test_cases.md`: full test case design (manual-style documentation, independent of
  automation implementation)
- `tests/`: automated Playwright/pytest implementation
- `docs/bug_reports/`: any defects identified during testing, documented in standard
  bug-report format
- `docs/exploratory_session_log.md`: notes from time-boxed manual exploratory testing

## 9. Known Limitations

This suite intentionally focuses on UI-level functional testing of the core purchase
journey. It does not attempt to validate backend logic, performance under load, or
accessibility compliance, each of which would be a reasonable next phase for a production
application, but falls outside the scope of a UI automation portfolio piece.
