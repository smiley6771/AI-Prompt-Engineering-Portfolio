# Structured classification prompt

Use the same model and ticket for both prompt conditions.

```text
You classify fictional IT helpdesk tickets into exactly one of four categories.

Definitions:
- security: suspicious access, phishing, malware, compromised accounts, or unsafe authentication.
- networking: connectivity, Wi-Fi, DNS, VPN reachability, or network performance.
- hardware: physical device, battery, peripheral, screen, or component failure.
- software: application functionality, installation, updates, or configuration errors.

Decision rules:
1. Classify the primary problem described, not incidental details.
2. An explicit compromise, phishing or malicious activity takes priority over a connectivity or app symptom.
3. Select exactly one category from: security, networking, hardware, software.
4. Output only the lowercase category. No punctuation or explanation.

Ticket:
[TICKET]
```

**Note:** Rules should be specified before running the final evaluation. Don't adjust them to fit the known answers without recording the change.
