# BUG-002: Login error banner text is clipped and unreadable

**Status:** Confirmed
**Severity:** Low
**Found via:** Manual exploratory testing
**Environment:** Chrome, macOS, desktop viewport

## Summary

The error banner shown on the login page does not resize to fit its message. When
the message wraps to three lines, the third line is cut off at the bottom edge of
the banner, leaving the text partially rendered and unreadable.

## Steps to Reproduce

1. Navigate to https://www.saucedemo.com/inventory.html directly, without logging
   in first.
2. Observe the red error banner that appears on the login page.

## Expected Result

The banner expands to fit its full message, and all text is legible.

## Actual Result

The banner keeps a fixed height. The message wraps to three lines, but only the
first two and a fraction of the third are visible. The final line ("in") is cut
off mid-character at the bottom edge.

The full message appears to be: "Epic sadface: You can only access
'/inventory.html' when you are logged in"

## Impact

Low. The user can still infer the meaning from the visible portion, and the
underlying access control is working correctly. However, a clipped error message
undermines trust in the interface and could be more confusing with a longer or
less predictable message.

## Notes on Detection

This defect is not detectable by the current automated suite, and that gap is
worth stating plainly. A functional assertion such as
`expect(page.get_by_text("Epic sadface")).to_be_visible()` passes here: the
element is present and rendered, so the assertion has nothing to object to.
Functional automation verifies behavior, not presentation.

Visual regression testing (for example, Playwright's `to_have_screenshot()`)
would catch a future change to this banner, but would not have caught this
instance. Baseline screenshots capture whatever state exists when they are taken,
so a pre-existing defect gets locked in as the expected result. Visual regression
catches regressions, not defects that were already there.

Catching this required a person looking at the screen and noticing something was
wrong. It is a useful example of why exploratory testing retains value alongside
a passing automated suite.
