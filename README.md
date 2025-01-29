# Public Demo

This is a repository to demonstrate the scanning and correlation capabilities of the Wiz platform.

**_This repo is for demo purposes only. All secret keys and sensitive data are fake._**

## Repository Configuration

### Secrets

| Name                      | Description                                                           |
| ------------------------- | --------------------------------------------------------------------- |
| `IMAGE_REGISTRY_USERNAME` | The username to utilize when authenticating to the container registry |
| `IMAGE_REGISTRY_PASSWORD` | The password to utilize when authenticating to the container registry |
| `WIZ_CLIENT_ID`           | The Client ID for the required Wiz Service Account                    |
| `WIZ_CLIENT_SECRET`       | The Client Secret for the required Wiz Service Account                |

### Variables

| Name             | Description                                                          |
| ---------------- | -------------------------------------------------------------------- |
| `IMAGE_REGISTRY` | The domain name of the container image registry to utilize           |
| `WIZ_ENV`        | The Wiz Environment to utilize for Wiz CLI scanning (Default: 'app') |
