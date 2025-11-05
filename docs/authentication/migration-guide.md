# Migration Guide

## Step 1: Inventory
- Identify existing automation scripts using `UsernamePasswordCredential`.
- Map the service accounts they rely on and their current site/folder memberships.

## Step 2: Register new apps
- Create app registrations in Entra ID.
- Add `Sites.Selected` permissions.
- Configure authentication (certificates preferred).

## Step 3: Consent
- Tenant admin grants admin consent to `Sites.Selected`.

## Step 4: Assign permissions
- Grant app site/folder/file access equivalent to old service accounts.
- Use Graph API, PnP PowerShell, or SharePoint Admin Center.

## Step 5: Update scripts
- Replace UsernamePasswordCredential with ClientSecretCredential or CertificateCredential.
- Update API calls to use app-only tokens.

## Step 6: Test
- Verify that scripts can only access the intended sites/folders.
- Confirm that access to other sites is denied.

## Step 7: Decommission
- Disable or delete old service accounts.
- Remove stored user passwords from automation.

## Step 8: Monitor
- Audit app permissions regularly.
- Review token usage and access logs.
