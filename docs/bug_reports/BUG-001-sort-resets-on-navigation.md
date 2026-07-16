# BUG-001: Sort order resets after navigating to product detail page and back

**Status:** Confirmed
**Severity:** Low
**Found via:** TC-011 (automated), confirmed manually
**Environment:** Chromium (Playwright automation) and manual verification, macOS

## Summary

Selecting a non-default sort option on the inventory page does not persist when the
user navigates into a product detail page and then returns to the inventory page.
The sort silently resets to the default ("Name, A to Z").

## Steps to Reproduce

1. Log in to https://www.saucedemo.com with `standard_user`.
2. On the inventory page, select "Price (low to high)" from the sort dropdown.
3. Confirm the product list reorders correctly by ascending price.
4. Click into any product to open its detail page.
5. Click "Back to Products."

## Expected Result

The sort dropdown should still show "Price (low to high)," and the product list
should remain ordered by ascending price.

## Actual Result

The sort dropdown resets to its default state ("Name, A to Z"), and the product
list reorders back to the default alphabetical order. The user's sort selection
is lost.

## Impact

Low. This does not block any core functionality (login, cart, checkout), and the
user can simply reapply their preferred sort. However, it is a usability
inconsistency: most users would expect a chosen view preference to persist during
a single browsing session, at least until they navigate away from the app
entirely or refresh manually.

## Notes

This was originally written as TC-011 under the assumption that sort selection
would persist across navigation (a reasonable default expectation for this kind
of control). Automated testing caught the mismatch between expected and actual
behavior, confirmed manually, and the test case was subsequently updated to
assert and document the actual (buggy) behavior, so the automated suite tracks
this as a known issue rather than silently failing or asserting an incorrect
assumption.
