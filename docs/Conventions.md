# Conventions

## Scenario identifiers

- `SEC-XXX_snake_case_name`, numbered sequentially across the whole repository, never per track,
  so an id is unique on its own and can be cited in a conversation or a CV.
- Never reuse an id. If a scenario is retired, the number retires with it.

## Scenario anatomy

Copy [`_template/`](../_template/) and keep the section order. The order is the argument: what
the attacker does, how it is seen, how it is stopped, and the proof of each step.

- **Status line** — resolution state, date, and whether the lab has actually been run.
- **MITRE ATT&CK** — technique IDs, listed explicitly so they are searchable.
- **Threat scenario** — the business context and why the technique matters for that industry.
  Industry descriptor only, never a customer name.
- **Attack simulation** — the exact commands or code that produce the malicious activity.
- **Detection** — the signal, the rule, the expected latency, and the false-positive profile.
  A detection without a stated false-positive profile is not finished.
- **Response** — the containment action, whether it is automated, and what it deliberately does
  not do (blast radius).
- **Evidence** — captured log excerpts and findings that prove detection and response fired.
- **Hardening** — the preventive control that would have made the attack impossible, and its cost.
- **Reusable takeaways** — numbered, transferable lessons.
- **References** — public sources only.

## Evidence

- Store captured output under `lab/evidence/` as text or markdown, with the timestamp and the
  region kept, and every identifier sanitized.
- Prefer an excerpt that shows the decisive field over a full log dump.
- Redact but do not fabricate. If a value cannot be published, replace it with a placeholder and
  say what it was, for example `<attacker-source-ip, non-corporate ASN>`.

## Labs

- One `deploy_lab.py` per scenario, with the subcommands `deploy`, `status`, `test` and `teardown`.
- Resumable: persist created resource ids to `resources.json` (gitignored) and re-read them.
- Derive the account id with `sts get_caller_identity`. Never hardcode it.
- Tag everything with `Project=aws-security-engineering` and `Scenario=SEC-XXX` so orphaned
  resources can be found by tag.
- `teardown` must delete everything `deploy` created, in dependency order, and be idempotent.
- `test` prints an explicit PASS or FAIL per assertion and exits non-zero on any failure.
- State the estimated hourly and daily cost in the README. Choose the cheapest sizing that still
  demonstrates the behavior.

## Sanitization — this repository is public

Never commit:

- Customer or company names. Use an industry descriptor: "regulated financial services",
  "enterprise SaaS (accounting)", "airlines / travel technology".
- Support case identifiers. Use sequential `CASE-NN` tokens and keep the real mapping in
  `case_mapping.md`, which is gitignored.
- AWS account ids. Use `<LAB_ACCOUNT_ID>`, `<CUSTOMER_ACCOUNT_ID>`, `<WORKLOAD_ACCOUNT_ID>`.
- Customer resource ids: `vpc-`, `subnet-`, `nat-`, `tgw-`, `dx-`, ARNs, hosted zone ids, Web ACL
  names, distribution ids, domain names. Use `<customer-vpc-id>`-style placeholders.
- Employee names, aliases or emails. Refer to roles instead.
- Internal tooling, hostnames or URLs of any kind. Use the public equivalent.
- Internal service architecture: component names, polling intervals, internal SLAs, unreleased
  features. Describe only externally observable behavior and cite public documentation for it.

Lab-owned identifiers may stay when the resources are already destroyed and the value is inert,
but the lab account id is always replaced with `<LAB_ACCOUNT_ID>`.

## Writing style

- Bullets with bold labels, not markdown tables.
- Titles name the counterintuitive finding, not the service. "Catch-all drop kills the TCP SYN"
  beats "Network Firewall rule issue".
- State mechanisms and evidence. Cut anything that would survive unchanged if the finding were
  the opposite.
- English throughout, including diagrams.
