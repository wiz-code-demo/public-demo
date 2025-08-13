# Fix for CVE-2024-0519: Replace vulnerable elgalu/selenium image
# with official, maintained selenium/standalone-chrome image
#
# SECURITY ISSUE FIXED:
# - CVE-2024-0519: Out of bounds memory access in V8 JavaScript engine
# - Chrome version updated to 120.0.6099.224+ (patched)
# - Migrated from archived elgalu/selenium to official SeleniumHQ image
#
# Original vulnerable image: elgalu/selenium:3.141.59-p59
# New secure image: selenium/standalone-chrome:4.34.0-20250707

FROM selenium/standalone-chrome:4.34.0-20250707

# Switch to root for configuration
USER root

# Install any additional tools if needed for demo purposes
# (keeping minimal for security)
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Create demo directory structure if needed
RUN mkdir -p /opt/demo

# Copy any demo-specific configurations
# COPY demo-config/ /opt/demo/

# Set proper ownership
RUN chown -R seluser:seluser /opt/demo

# Switch back to selenium user for security
USER seluser

# Expose Selenium Grid port
EXPOSE 4444

# Expose VNC port for debugging (optional)
EXPOSE 5900

# Expose noVNC port for web-based debugging (optional)
EXPOSE 7900

# Use the default entrypoint from selenium image
# This starts the Selenium Grid in standalone mode