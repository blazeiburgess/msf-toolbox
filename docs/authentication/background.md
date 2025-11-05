# Background

## Why change?
- Microsoft is deprecating non-MFA accounts and the Resource Owner Password Credential (ROPC) flow.
- Automation scripts previously authenticated with service accounts using `UsernamePasswordCredential`.
- This approach bypassed MFA, introduced security risks, and is no longer supported.

## Old model
- A service account (dedicated user) was added to specific SharePoint sites or folders.
- Scripts ran headlessly with the user’s delegated permissions.
- This achieved fine-grained access control but relied on insecure authentication.

## New requirements
- Unattended, headless authentication.
- No reliance on password-based logins.
- Least-privilege access to specific sites, folders, or files.
- Alignment with Microsoft’s supported models.
