# Security Policy

## Reporting Security Vulnerabilities

🔒 **Please do not report security vulnerabilities through public GitHub issues.**

If you discover a security vulnerability in this project, please report it privately to help protect our users:

1. **GitHub Security:** Use GitHub's [private vulnerability reporting](https://github.com/AbyssWild/moon-dev-ai-agentswwgre/security/advisories/new) (preferred)
2. **Response Time:** We aim to respond within 48 hours
3. **Disclosure:** We follow responsible disclosure practices

## Supported Versions

Currently maintained versions:

| Version | Supported          |
| ------- | ------------------ |
| Latest  | :white_check_mark: |
| Older   | :x:                |

## Security Features

### 🔐 API Key Management

- All API keys and secrets are stored in `.env` file (excluded from version control)
- `.env_example` provides template without actual credentials
- No hardcoded secrets in source code
- API keys loaded via `python-dotenv`

### 🛡️ Command Injection Prevention

- All subprocess calls use list arguments (not shell=True)
- Custom `secure_utils` module for safe system operations
- Path validation and sanitization for file operations

### ✅ Secure Practices Implemented

1. **Environment Variable Security**
   - Sensitive data loaded from `.env`
   - Never committed to version control
   - Example template provided separately

2. **Safe Subprocess Usage**
   - All `subprocess` calls use list arguments
   - No `shell=True` to prevent injection
   - Proper error handling and timeouts

3. **No Dangerous Operations**
   - No `eval()` or `exec()` with external input
   - No unsafe pickle deserialization
   - No SQL injection risks (no database usage)

4. **Audio Playback Security**
   - Replaced `os.system()` with secure subprocess calls
   - Cross-platform support (macOS, Windows, Linux)
   - Path validation before execution

## Security Checklist for Contributors

When contributing code, ensure:

- [ ] No hardcoded API keys, passwords, or secrets
- [ ] Use `subprocess.run()` with list arguments, not `os.system()`
- [ ] Validate and sanitize all user inputs
- [ ] Use environment variables for configuration
- [ ] No `eval()` or `exec()` with untrusted input
- [ ] Proper error handling that doesn't expose sensitive info
- [ ] Add `.env` entries to `.env_example` (without values)

## Known Security Considerations

### 🔑 Private Key Security

This is a trading bot that requires:
- Solana private keys
- Ethereum private keys (for HyperLiquid)
- Multiple API keys

**⚠️ Critical Security Practices:**

1. **Never commit private keys** to version control
2. **Never share your `.env` file**
3. **Rotate keys immediately** if accidentally exposed
4. **Use separate wallets** for testing with small amounts
5. **Enable 2FA** on all accounts where possible
6. **Monitor wallet activity** regularly

### 🔐 API Key Best Practices

1. **Least Privilege:** Use API keys with minimum required permissions
2. **Rotation:** Regularly rotate API keys (monthly recommended)
3. **Monitoring:** Monitor API usage for anomalies
4. **Backup:** Keep secure backups of keys in password manager
5. **Revocation:** Have a plan to revoke compromised keys quickly

### 💻 Execution Environment

1. **VPS Security:** If running on VPS, secure your server
2. **Firewall:** Use firewall to restrict access
3. **Updates:** Keep system and dependencies updated
4. **Monitoring:** Log and monitor for suspicious activity
5. **Backups:** Regular backups of configuration (without secrets)

## Dependency Security

### Regular Updates

```bash
# Check for dependency vulnerabilities
pip install safety
safety check -r requirements.txt

# Or use pip-audit
pip install pip-audit
pip-audit
```

### Pinned Versions

All dependencies in `requirements.txt` are pinned to specific versions to prevent supply chain attacks.

## Security Audit History

| Date | Type | Findings | Status |
|------|------|----------|--------|
| 2025-10-25 | Code Review | Fixed exec() and os.system() vulnerabilities | ✅ Resolved |

## Security Resources

- [SECURITY_ANALYSIS.md](SECURITY_ANALYSIS.md) - Detailed security analysis
- [Python Security Best Practices](https://python.readthedocs.io/en/stable/library/security_warnings.html)
- [OWASP Top Ten](https://owasp.org/www-project-top-ten/)

## Automated Security

Consider integrating:

1. **Dependabot:** Automated dependency updates (GitHub native)
2. **CodeQL:** Static analysis security scanning (GitHub native)
3. **pip-audit:** Python dependency vulnerability scanner
4. **bandit:** Python security linter

## Emergency Response

If you suspect a security breach:

1. **Immediate Actions:**
   - Revoke all API keys immediately
   - Change all passwords
   - Move funds from affected wallets to secure addresses
   - Document what happened

2. **Investigation:**
   - Review logs for suspicious activity
   - Check transaction history
   - Identify attack vector
   - Assess damage

3. **Recovery:**
   - Generate new keys and credentials
   - Update all affected systems
   - Implement additional security measures
   - Monitor for continued threats

4. **Notification:**
   - Report to relevant parties
   - Update security documentation
   - Share lessons learned (without sensitive details)

## Compliance & Legal

### Financial Regulations

This software is provided as-is for educational purposes. Users are responsible for:

- Complying with local trading regulations
- Tax reporting requirements
- KYC/AML obligations
- License requirements for automated trading

### Disclaimer

🚨 **Trading cryptocurrency carries substantial risk of loss.** This software:

- Is experimental and educational
- Provides no guarantees of profitability
- Should not be used with funds you cannot afford to lose
- Is not financial advice

## Contact

For security concerns: Contact repository owner  
For general issues: Use GitHub Issues  
For discussions: Join Discord community

---

**Remember:** Security is everyone's responsibility. When in doubt, ask before committing!

🌙 Built with security in mind by Moon Dev
