# Security Considerations

## Principle of least privilege
- Always prefer `Sites.Selected` over tenant-wide scopes.
- Grant the minimum role necessary (e.g., `read` if write is not required).

## Consent model
- Admins consent once to `Sites.Selected`.
- Site owners or admins must assign the app per site/folder.

## Auditing
- Site owners can review app permissions in SharePoint Admin Center.
- Monitor app-only token usage with Microsoft 365 audit logs.

## Limits
- Folder/file assignments create unique permissions.
- Excessive unique permissions can affect performance and manageability.

## Retirement note
- Legacy SharePoint Add-Ins (`appinv.aspx`) are deprecated and will be shut down by April 2026.
- RSC is the long-term supported model.
