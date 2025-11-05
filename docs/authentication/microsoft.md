# Modern Authentication for SharePoint & Graph in Automation

## Introduction

Microsoft is deprecating the use of non-MFA accounts for authenticating against their products; this has been known since 2024 and looks to be happening on the **30th of September, 2025**. Any scripts that do not use an interactive authentication flow (i.e. background scripts, automation tasks, etc.) will stop working, and it looks like if you are using the third-party `Office365-REST-Python-Client` `.with_user_creds()` then your flow may already be breaking. For this we have made some short-term fixes which use the `UsernamePasswordCredential` from `azure-identity` (which uses `msal` under-the-hood); this works but is also deprecated according to the aforementioned notice.

**Our goal**: run automated scripts against SharePoint and Graph without broad, tenant-wide permissions.

## Background

- **Old approach**: Service account with delegated permissions, added to specific sites/folders. Scripts authenticated using username/password.
- **Problems**: Bypasses MFA, weak security posture, and now deprecated.
- **Result**: We need to move from delegated user context to app-only authentication.

_TODO: Break this down further_
### Old Approach

### Problems

## New Authentication Options

- **App-only authentication**: Azure AD (Entra ID) registered applications use _certificates_ or _secrets_.
- **Permissions model**:
  - Static scopes (`Sites.FullControl.All`, `Files.ReadWrite.All`) apply tenant-wide
  - "New" _Selected scopes_ allow **resource-specific consent (RSC)**
- **Key concept**: Apps get no default access with `Sites.Selected`. Access must be explicitly granted to a site, list, folder, or file.

_TODO: Break this down further_

### App-only auth

### Permissions model

### Resource-Specific Consent

## Implementation Patterns

### App Registration

1. Register the application in Entra ID.
2. Add API permissions -> Add a permission -> Microsoft Graph -> Sites.Selected.
3. Admin consent required once.

### Assigning Site-Scoped Permissions

- Grant the app roles (`Read`, `Write`, `Manage`, `FullControl`) on a given site.
- Example (PnP PowerShell):
```powershell
Grant-PnPAzureADAppSitePermission -Site https://contoso.sharepoint.com/sites/TeamX -AppId <AppId> -Permissions Write
```

### Assigning Folder/File-Scoped Permissions

- Use Graph API to grant access directly to a driveItem.
- Example (PowerShell Graph SDK):
```powershell
New-MgDriveItemPermission -DriveId <DriveId> -DriveItemId <FolderId> -BodyParameter @{ roles = @('write'); grantedTo = @{ application = @{ id = '<AppId>' } } }
```

### Using Tokens in Scripts

- Script acquires app-only token using certificate/secret.
- Token includes `Sites.Selected`.
- Access is checked against the site/folder/file permissions assigned.

## Graph vs SharePoint REST

Many operations now exist in Graph, but some properties are only in SharePoint REST. For example, if you are trying to get the HasUniqueRoleAssignment properties from a folder this can still only be done via SharePoint REST, while Graph can still list the permissions on an item this specific property is still missing.

Be sure to check if a property is returned by a given resource before falling back to SharePoint REST since you might just have to use $select/$expand to retrieve it.

Both API methods support RSC. If you add `Sites.Selected` under SharePoint API as well, the app can call REST endpoints with the same scoped access (TBC).

## Security Considerations

- **Least privilege**: Apps gain no access by default. Explicit assignment required.
- **Auditing**: Site owners can review which apps have permissions.
- **Limits**: Folder/file-level assignments break inheritance and count against unique permissions limits in SharePoint.
- **Fallback**: If broader access is unavoidable, restrict to specific apps and monitor carefully. i.e. With regular certificate/secret rotation, and strong app ownership control.

_TODO: Break this down further_

### Principle of Least Privelege

### Admin Consent + Site Owner Assignment

### Limits

## Migration Strategy

1. Identify existing service accounts and their folder/site memberships.
2. Register replacement apps in Entra ID.
3. Request `Sites.Selected` (Graph and optionally SharePoint API).
4. Admin consent the permissions.
5. Grant site/folder permissions matching old access.
6. Update scripts to authenticate using app-only token.
7. Decommission old service accounts.

### Mapping Old Service Accounts to New App Registrations

### Step-by-Step Migration Checklist

## References & Further Reading

- [Microsoft: Resource-specific consent in Graph](https://learn.microsoft.com/en-us/graph/permissions-reference#resource-specific-consent)
- [PnP PowerShell: Grant-PnPAzureADAppSitePermission](https://pnp.github.io/powershell/cmdlets/Grant-PnPAzureADAppSitePermission.html)
- [Graph API: DriveItem permissions](https://learn.microsoft.com/en-us/graph/api/driveitem-post-permissions)
- [Microsoft: SharePoint Add-in retirement](https://learn.microsoft.com/en-us/sharepoint/dev/sp-add-ins/retirement-announcement-for-add-ins)
