# App Registration

To enable app-only authentication, you must register an application in Microsoft Entra ID (Azure AD).

## Steps

1. **Register application**
   - Go to Entra admin portal → App registrations -> New registration.
   - Give it a descriptive name (e.g., `Automation-SharePoint-Scripts`).
   - Choose *Accounts in this organisation only*.

2. **Configure secrets or certificates**
   - Preferred: upload an X.509 certificate for authentication.
   - Alternative: create a client secret (expires, less secure).

3. **Add API permissions**
   - Microsoft Graph -> Application -> `Sites.Selected`.
   - Optionally: SharePoint -> Application -> `Sites.Selected` (for REST API access).
   - Click *Grant admin consent*.

4. **Expose App ID**
   - Note the **Client ID**, **Tenant ID**, and the certificate/secret.  
   - Scripts will use these values to acquire tokens.

## Result
The app has no access by default. Access must be explicitly granted per site, list, or folder.
