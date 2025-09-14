# HTTPS Deployment Guide

## Django Settings
- SECURE_SSL_REDIRECT = True
- SECURE_HSTS_SECONDS = 31536000
- SECURE_HSTS_INCLUDE_SUBDOMAINS = True
- SECURE_HSTS_PRELOAD = True
- SESSION_COOKIE_SECURE = True
- CSRF_COOKIE_SECURE = True
- X_FRAME_OPTIONS = "DENY"
- SECURE_CONTENT_TYPE_NOSNIFF = True
- SECURE_BROWSER_XSS_FILTER = True

## Web Server Configuration
- SSL certificate installed via Let's Encrypt
- Nginx configured to redirect HTTP to HTTPS
- Certbot used for auto-renewal

## Security Review
- All cookies restricted to HTTPS
- Headers implemented to prevent XSS, clickjacking, and MIME sniffing
- HSTS ensures long-term HTTPS enforcement
