# Using Tokens in Scripts

## Python example
```python
from azure.identity import ClientSecretCredential
from msgraph.core import GraphClient

tenant_id = "<tenant-id>"
client_id = "<client-id>"
client_secret = "<client-secret>"

credential = ClientSecretCredential(tenant_id, client_id, client_secret)
client = GraphClient(credential=credential)

site_id = "<site-id>"
response = client.get(f"/sites/{site_id}/drive/root/children")
print(response.json())
```

## PowerShell Example

```powershell
Connect-MgGraph -ClientId <clientId> -TenantId <tenantId> -CertificateThumbprint <thumbprint>
Get-MgSite -SiteId <siteId>
```

## REST call with bearer token

1. Aquire token:
```bash
az account get-access-token --resource https://graph.microsoft.com
```
2. Call Graph API
```bash
curl -H "Authorization: Bearer <token>" https://graph.microsoft.com/v1.0/sites/root
```
