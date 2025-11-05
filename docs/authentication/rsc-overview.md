# Resource-Specific Consent (RSC)

## Concept
- Traditional Graph application permissions (`Sites.ReadWrite.All`) apply tenant-wide.
- RSC introduces **Selected scopes** (`Sites.Selected`) which enable per-resource assignments.
- Apps start with **zero access** until explicitly granted permissions.

## Supported resources
- **Site collections**
- **Lists and document libraries**
- **Folders**
- **Files**

## Roles available
- `read`
- `write`
- `manage`
- `fullcontrol`

## Benefits
- True least-privilege model.
- Mirrors how a service account used to be added only to certain sites or folders.
- Prevents apps from accessing data outside their scope.

## Limitations
- Assignments break inheritance at list/folder/file level.
- SharePoint limits on unique permissions still apply.
