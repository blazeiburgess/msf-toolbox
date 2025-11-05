# Assigning Folder and File Permissions

## Why use folder-level permissions?
When an automation script should only operate on a specific library or folder without touching the rest of the site.

## Graph API (PowerShell SDK)
```powershell
$DriveId  = "<drive-id-of-the-library>"
$FolderId = "<driveItem-id-of-the-folder>"
$AppId    = "<AppId>"

$params = @{
  roles     = @("write")
  grantedTo = @{ application = @{ id = $AppId } }
}

New-MgDriveItemPermission -DriveId $DriveId -DriveItemId $FolderId -BodyParameter $params
```

## REST API Equivalent

```http
POST /drives/{driveId}/items/{itemId}/permissions
Content-Type: application/json

{
  "roles": ["read"],
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

## Notes

- File and folder assignments create **unique permissions**.
- Unique permissions may count towards SharePoint limits.
- Use with caution for large-scale scenarios
