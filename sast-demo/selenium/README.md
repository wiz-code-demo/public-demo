# Selenium Security Fix - CVE-2024-0519

## Overview

This directory contains the security fix for **CVE-2024-0519**, a critical vulnerability in the V8 JavaScript engine that affected the previously used Selenium container image.

## Vulnerability Details

- **CVE ID**: CVE-2024-0519
- **Severity**: Critical
- **CVSS Score**: High
- **Description**: Out of bounds memory access in V8 JavaScript engine in Google Chrome prior to version 120.0.6099.224
- **Impact**: Remote code execution via crafted HTML page
- **Affected Image**: `elgalu/selenium:3.141.59-p59` (archived/unmaintained)

## Security Fix

### Previous Vulnerable Configuration
```yaml
image:
  repository: wizsensordemos.azurecr.io/sast-demo
  tag: "main"
```
- Based on archived `elgalu/selenium:3.141.59-p59`
- Chrome version vulnerable to CVE-2024-0519
- No longer maintained or receiving security updates

### New Secure Configuration
```yaml
image:
  repository: selenium/standalone-chrome
  tag: "4.34.0-20250707"
```
- Official SeleniumHQ maintained image
- Chrome 120.0.6099.224+ (patched for CVE-2024-0519)
- Regular security updates and maintenance
- Selenium Grid 4.34.0 with latest features

## Security Improvements

### 1. Updated Base Image
- **From**: `elgalu/selenium:3.141.59-p59` (archived June 30, 2021)
- **To**: `selenium/standalone-chrome:4.34.0-20250707` (actively maintained)

### 2. Container Security Hardening
```yaml
securityContext:
  allowPrivilegeEscalation: false
  readOnlyRootFilesystem: false
  capabilities:
    drop: [ALL]
    add: [SYS_ADMIN]  # Required for Chrome sandbox
  runAsNonRoot: true
  runAsUser: 1200
```

### 3. Resource Limits
```yaml
resources:
  limits:
    cpu: 2000m
    memory: 4Gi
  requests:
    cpu: 1000m
    memory: 2Gi
```

### 4. Shared Memory Configuration
```yaml
volumes:
  - name: dshm
    emptyDir:
      medium: Memory
      sizeLimit: 2Gi
```

## Deployment Instructions

### Using Helm
```bash
# Deploy with updated secure image
helm upgrade --install selenium-demo ./sast-demo/sb-showtime \
  --set image.repository=selenium/standalone-chrome \
  --set image.tag=4.34.0-20250707
```

### Using Docker
```bash
# Build the secure image
docker build -t secure-selenium-demo ./sast-demo/selenium/

# Run with security best practices
docker run -d \
  --name selenium-demo \
  --shm-size=2g \
  --security-opt no-new-privileges \
  --user 1200:1201 \
  -p 4444:4444 \
  secure-selenium-demo
```

## Verification

### 1. Check Chrome Version
```bash
kubectl exec -it <pod-name> -- google-chrome --version
# Should show version 120.0.6099.224 or higher
```

### 2. Verify Selenium Grid
```bash
curl http://localhost:4444/wd/hub/status
# Should return grid status with ready: true
```

### 3. Security Scan
```bash
# Run vulnerability scan on new image
trivy image selenium/standalone-chrome:4.34.0-20250707
```

## Maintenance

### Regular Updates
- Monitor [SeleniumHQ/docker-selenium releases](https://github.com/SeleniumHQ/docker-selenium/releases)
- Update image tags regularly for security patches
- Subscribe to security advisories

### Automated Scanning
```yaml
# Example GitHub Actions workflow
name: Security Scan
on:
  schedule:
    - cron: '0 2 * * *'  # Daily at 2 AM
jobs:
  scan:
    runs-on: ubuntu-latest
    steps:
    - name: Scan Selenium Image
      uses: aquasecurity/trivy-action@master
      with:
        image-ref: 'selenium/standalone-chrome:4.34.0-20250707'
```

## References

- [CVE-2024-0519 Details](https://nvd.nist.gov/vuln/detail/cve-2024-0519)
- [Chrome Security Update](https://chromereleases.googleblog.com/2024/01/stable-channel-update-for-desktop_16.html)
- [SeleniumHQ Docker Images](https://github.com/SeleniumHQ/docker-selenium)
- [Kubernetes Security Best Practices](https://kubernetes.io/docs/concepts/security/)

## Support

For questions about this security fix or Selenium deployment:
- Review the [SeleniumHQ documentation](https://selenium.dev/documentation/)
- Check [Docker Selenium wiki](https://github.com/SeleniumHQ/docker-selenium/wiki)
- Report security issues through proper channels