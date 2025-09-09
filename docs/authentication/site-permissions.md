# Assigning Site Permissions

## When to use
Use site-level assignment if your app needs access to all content within a site collection.

## Graph API
Create a permission grant:

```http
POST /sites/{siteId}/permissions
Content-Type: application/json

{
  "roles": ["write"],
  "grantedToIdentities": [
    {
      "application": {
        "id": "<AppId>",
        "displayName": "Automation-SharePoint-Scripts"
      }
    }
  ]
}
```

## PowerShell (PnP)
```powershell
Grant-PnPAzureADAppSitePermission `
  -Site https://contoso.sharepoint.com/sites/TeamX `
  -AppId <AppId> `
  -DisplayName "Automation-SharePoint-Scripts" `
  -Permissions Write
```

## Roles
- `Read`: View only.
- `Write`: Add, update, delete content.
- `Manage`: More advanced site operations.
- `FullControl`: Equivalent to site collection admin.
