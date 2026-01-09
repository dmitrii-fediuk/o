#
`A` ≔
```toml
URL = 'https://www.upwork.com/jobs/~021998936685512149772'
Title = 'Azure CLI SSL Certificate Verification Expert Needed for Python 3.13 Proxy Issue'
'Publication Date' = 'today'
```

#
`PD` ≔
~~~markdown
#
I need an experienced freelancer to troubleshoot and resolve an SSL certificate verification error I'm encountering when using Azure CLI on my Windows machine (likely running in Git Bash or similar).
#
The setup involves a custom Python 3.13 environment with Azure CLI installed via pip, and I'm behind a corporate proxy that performs SSL/TLS inspection.
#
Despite following standard fixes, the issue persists, and I suspect it's related to strict certificate validation in Python 3.13.
# Problem Details:
## Command failing
`az login` (aliased to `python -m azure.cli`).
## Error message
"[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: CA cert does not include key usage extension (_ssl.c:1028)".
## Environment
Windows, Python 3.13, custom `.bashrc` with exports like:
```bash
export PATH=/c/Users/[username]/bin:$PATH
export SSL_CERT_FILE=/path/to/cacert.pem
export REQUESTS_CA_BUNDLE=$SSL_CERT_FILE (and similar for GIT, CURL, NODE).
```

# Attempts made:
- Appended the proxy's root CA certificate (exported from a working machine) to a custom `cacert.pem`.
- Set proxy vars (`HTTP_PROXY`, `HTTPS_PROXY`).

#
The CA cert is from our internal network/proxy (e.g., Zscaler or similar), but it lacks required extensions like keyCertSign in Key Usage.
#
Works on another machine (possibly older Python or different config), but not here.

# Goal
##
Get `az login` working without disabling verification (insecure workaround).
##
Prefer secure fixes like using system cert store, proper CA config, or Python tweaks.
~~~

#
Сделай `PD` частью `A`.