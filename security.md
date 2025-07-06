# Security Policy

## Supported Versions

We currently support the following versions of AutoCAD MCP Server:

| Version | Supported          |
| ------- | ------------------ |
| 0.1.x   | :white_check_mark: |

## Reporting a Vulnerability

We take security seriously and appreciate your efforts to responsibly disclose security vulnerabilities.

### How to Report

**DO NOT** create a public GitHub issue for security vulnerabilities.

Instead, please report security issues by email to: [vigneshpbmenon1@outlook.com]

Please include:
- A detailed description of the vulnerability
- Steps to reproduce the issue
- Potential impact assessment
- Any suggested fixes or mitigations

### What to Expect

- **Acknowledgment**: We will acknowledge receipt of your report within 48 hours
- **Initial Assessment**: We will provide an initial assessment within 5 business days
- **Regular Updates**: We will keep you informed of our progress
- **Resolution**: We aim to resolve critical issues within 90 days

### Responsible Disclosure

We kindly ask that you:
- Allow us reasonable time to investigate and fix the issue
- Do not publicly disclose the vulnerability until we have released a fix
- Do not perform testing on systems you don't own or without permission

## Security Considerations

### AutoCAD Integration

- This software requires AutoCAD to be running and uses COM interfaces
- The server should only be used in trusted environments
- Network exposure should be carefully considered

### Python Dependencies

- We regularly update dependencies to address security vulnerabilities
- Use `pip-audit` or similar tools to scan for known vulnerabilities
- Consider using virtual environments to isolate dependencies

### Best Practices

When using this software:
- Keep AutoCAD and Python updated
- Use the latest version of the MCP server
- Implement proper access controls
- Monitor for suspicious activity
- Backup important CAD files before automation

## Security Features

- Input validation on all tool parameters
- Error handling to prevent information leakage
- Type checking to prevent injection attacks
- Minimal required permissions

## Vulnerability History

No vulnerabilities have been reported or discovered at this time.

## Security Resources

- [OWASP Python Security](https://owasp.org/www-project-python-security/)
- [Python Security Best Practices](https://python.org/dev/security/)
- [AutoCAD Security Guidelines](https://www.autodesk.com/trust/security)

---

Thank you for helping keep AutoCAD MCP Server secure!
