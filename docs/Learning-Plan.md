# Learning Plan

A twelve-week plan to close the gap between an AWS networking background and a cloud security
engineering role that spans **cloud posture, detection and response, secure code and CI/CD, and the
security of AI systems in production**. Derived from the requirements that repeat across 2026
security engineering postings at large cloud providers, frontier AI labs and regulated fintechs.

Started 2026-09-22. Assumes ~9 hours per week: two weekday evenings of study, one weekend block to
build, one hour to write up. Every phase ends in a committed artifact — there is no phase whose
output is only notes.

## How this plan is built

- **60 / 30 / 10.** Sixty percent hands-on in a deployed lab, thirty percent reading primary
  sources, ten percent writing the result down. Video courses are not the primary channel.
- **Primary sources only for the reference layer.** RFCs, AWS and GCP service documentation, vendor
  docs, the MITRE matrices, OWASP project pages. Blogs are for technique ideas, never for how a
  control actually behaves.
- **The artifact is the assessment.** A phase is complete when its scenario deploys, detects,
  responds and tears down, with a `test` that fails when the control is removed. Not when the
  reading list is finished.
- **Explain it to a non-engineer.** Each scenario README must make the mechanism understandable to
  someone outside security. Communication is a graded requirement in these roles, not a soft skill.
- **Memorize only vocabulary.** Spaced repetition is worth it for finding types, SPL commands, IAM
  condition keys and OAuth claims — roughly twenty cards per phase. Nothing conceptual goes in a
  deck; concepts get built instead.
- **Keep a verification log.** For every answer taken from an AI assistant during this plan, record
  the claim, the primary source that confirmed or contradicted it, and the verdict. The running
  tally of how often the model was wrong, and about what, is itself a portfolio artifact — and it
  is the exact instinct these roles screen for.

### Sequencing rationale

- **Query-language fluency goes first.** It is the most frequently cited requirement, the cheapest
  to acquire, and every later phase produces logs that need querying.
- **A second cloud goes late.** Postings ask for working knowledge of *one* provider plus the
  appetite to go deeper. One well-built GCP scenario removes the objection; eight weeks of GCP study
  displaces higher-value work.
- **AI security goes last but is not optional.** It depends on having real telemetry and real IAM
  boundaries to attack, both of which earlier phases produce. It is also the strongest
  differentiator, so it gets a full phase rather than a footnote.
- **Deliberately out of scope:** EDR console operation, phishing sandbox triage and incident
  management platforms. They cannot be practiced honestly without the licensed product, and
  simulating them produces a fake artifact. Prepare to discuss them conceptually and say plainly
  that the hands-on part is missing.

## Phase 0 — Lab account hygiene (week 0, one evening)

- **Learn:** consolidated billing alarms, AWS Budgets actions, `Ephemeral` tagging, tag-based
  orphan sweeps, and what an SCP can protect in a lab account.
- **Read:** AWS Budgets documentation; the service-quota and free-tier pages for the services used
  in Phase 1.
- **Build:** a dedicated lab account with a hard budget alarm, an SCP denying regions outside the
  one in use, and a tag-based sweep script that lists anything tagged `Ephemeral=true` older than
  24 hours.
- **Artifact:** `docs/Lab-Account-Setup.md`, plus the sweep script under `tools/`.
- **Done when:** a forgotten NAT gateway would page you within an hour instead of showing up on an
  invoice.

## Phase 1 — Query languages and SIEM fluency (weeks 1–2)

The single most-cited gap. The goal is not "I have seen Splunk"; it is writing a detection whose
threshold is justified by a measured baseline.

- **Learn:** SPL as a language — `search`, `stats`, `tstats`, `eval`, `where`, `rex`, `transaction`,
  `lookup`, subsearches; the index / sourcetype / field-extraction model; why `tstats` exists.
  Then the same query expressed three ways: SPL, CloudWatch Logs Insights, and SQL over Athena.
- **Read:** the Splunk Search Manual and Search Reference; the Sigma specification and the
  `sigma-cli` backend list; the CloudWatch Logs Insights query syntax reference.
- **Practice:** Splunk Free in Docker (`splunk/splunk`), loaded first with the public BOTS datasets
  to learn the language against data someone else has labeled, then with CloudTrail, VPC Flow Logs
  and Route 53 Resolver query logs exported from the lab account.
- **Artifact:** **SEC-001 — DNS exfiltration through Resolver query logs** (T1048). The detection
  ships three times: as a Sigma rule, as the generated SPL, and as the CloudWatch Logs Insights
  equivalent, with the DNS Firewall rule that stops it as the preventive control.
- **Done when:** the README states the query-length and entropy thresholds with the baseline
  measurement that justifies them, and a false-positive profile derived from seven days of the
  lab's own traffic — not an assumed number.

## Phase 2 — Detection engineering as an engineering discipline (weeks 3–4)

The postings do not ask for alerts. They ask for rule lifecycle management, coverage, precision,
latency and safe rollout.

- **Learn:** GuardDuty finding types and what telemetry each one is derived from; CloudTrail
  management versus data events; Security Hub as an aggregator; EventBridge as the response trigger;
  detection-as-code — rules in version control, tested in CI, promoted through environments.
- **Read:** the GuardDuty finding-types reference; the CloudTrail event reference; the MITRE ATT&CK
  Cloud matrix entries for the techniques in [MITRE-Coverage.md](MITRE-Coverage.md).
- **Practice:** Stratus Red Team to emit techniques on demand; measure end-to-end latency from
  action to alert and record p50 and p95 per rule; then tune a deliberately noisy rule and document
  what the tuning gave up.
- **Artifacts:**
  - **SEC-002 — EC2 role credentials used from outside the VPC** (T1078.004): credentials taken
    from the instance metadata service and replayed from elsewhere, detected on the mismatch
    between the role session and its expected network origin.
  - **SEC-003 — Detection quality as a measured property**: precision, coverage and latency for the
    rule set built so far, with the rules themselves under test in CI.
- **Done when:** removing a rule makes CI fail, and every published rule carries a latency number
  and a false-positive profile measured rather than estimated.

## Phase 3 — Identity, OAuth/OIDC and CI/CD trust (weeks 5–6)

The conceptual gap that is closed fastest by building, and the one that pays off in every
interview: almost every cloud compromise is an identity problem wearing a different hat.

- **Learn:** the OAuth 2.0 authorization code and client credentials flows; what an OIDC ID token
  actually asserts, claim by claim; SAML versus OIDC for SSO; MFA and its bypasses; machine identity
  and service-to-service auth; `AssumeRoleWithWebIdentity`; trust-policy conditions on `sub` and
  `aud`; permission boundaries versus SCPs versus identity policies.
- **Read:** RFC 6749, then RFC 6819 (the threat model — the more useful half); OpenID Connect Core
  section 2 on claims; the AWS documentation on federating GitHub Actions with OIDC; an identity
  provider's own machine-to-machine token documentation on a free tenant.
- **Practice:** a free IdP tenant to issue and inspect tokens by hand; then remove every long-lived
  key from a deployment pipeline.
- **Artifacts:**
  - **SEC-004 — Keyless CI deployment, and the detection for the key that should not exist**:
    GitHub Actions authenticating to AWS through OIDC, an SCP denying access-key creation, and a
    detection for `iam:CreateAccessKey` on a principal that no longer needs one (T1098.001).
  - **SEC-005 — A wildcard in the `sub` claim is the vulnerability**: an over-broad OIDC trust
    policy assumed from a repository that was never meant to have it, with the tightened condition
    proven by a test that shows the second repository denied.
- **Done when:** you can explain, without notes, which claim binds a token to one repository and
  what an attacker gets when that binding is loose.

## Phase 4 — Secure code, SAST and dependency triage (weeks 7–8)

The review work these roles actually do daily is unglamorous: internal tools, scripts and pull
requests with hardcoded credentials, unsafe input handling, over-broad permissions and secrets in
pipelines.

- **Learn:** the OWASP Top 10 narrowed to what appears in internal automation rather than in web
  applications; the OWASP Top 10 CI/CD Security Risks; CVE triage by reachability and exploit
  likelihood instead of raw severity; quality gates that block a merge versus ones that only report.
- **Read:** OWASP Top 10 and the CI/CD Security Risks project; the EPSS documentation; SonarQube
  quality-gate documentation; the Semgrep rule-writing guide.
- **Practice:** SonarQube Community in Docker over this repository and the AI labs repository; a
  custom Semgrep rule for a real boto3 anti-pattern (an over-broad policy document built from an
  f-string, for instance); secret scanning against a branch with a planted credential.
- **Artifact:** **SEC-006 — The critical CVE I did not fix first.** The pipeline gate built out with
  SAST, dependency and secret scanning, plus the triage record: what was found, what was fixed, and
  the reasoning for the unreachable critical that was deferred while a reachable medium was fixed.
- **Done when:** you can defend the deferral with reachability evidence, and the custom rule catches
  a pattern that the off-the-shelf ruleset misses.

## Phase 5 — The second provider, by translation (weeks 9–10)

Study GCP as a mapping exercise from what already exists in this repository, not from zero.

- **Learn:** GCP IAM — members, roles, bindings, service accounts, service account keys, workload
  identity federation, impersonation; organization policy constraints as the SCP analogue; VPC
  firewall rules against security groups and NACLs; Cloud Audit Logs admin activity versus data
  access; Security Command Center finding classes; Cloud Asset Inventory for project inventory.
- **Read:** the GCP IAM overview; "Best practices for using service accounts"; the Cloud Audit Logs
  overview; the Security Command Center finding-types reference.
- **Practice:** a free-tier project; create the misconfiguration, watch which log records it, and
  note where the GCP signal is better or worse than the AWS equivalent.
- **Artifact:** **SEC-007 — Service account key exfiltration, and the org policy that makes it
  impossible**: detected in Cloud Audit Logs and Security Command Center, prevented with
  `constraints/iam.disableServiceAccountKeyCreation`, and mapped side by side against the AWS
  access-key equivalent from SEC-004.
- **Done when:** you can translate any control in this repository into its GCP counterpart in one
  paragraph, including where the analogy breaks.

## Phase 6 — Securing AI systems, and trusting their output (weeks 11–12)

Lands in the [ai-labs](https://github.com/rreyescloud/ai-labs) repository. Two artifacts: one on
attacking an AI system, one on measuring whether an AI system's own conclusions can be believed.
The second is the differentiator — operating an LLM investigation agent and catching its
hallucinated attributions is the job description of a growing number of these roles, and almost
nobody has published evidence of doing it.

- **Learn:** the OWASP Top 10 for LLM Applications; MITRE ATLAS; Bedrock Guardrails and what
  they measure; tool-use permissioning for agents and the confused-deputy problem; indirect prompt
  injection through retrieved content; evaluation design — ground truth, N runs, and the failure
  mode where the correct answer is "the evidence does not support a conclusion".
- **Read:** the OWASP LLM Top 10 entries for prompt injection, excessive agency and sensitive
  information disclosure; ATLAS techniques for the same; the provider documentation on tool use and
  on guardrail evaluation; published critiques of LLM-as-judge evaluation.
- **Artifacts:**
  - **AIS-003 — Indirect prompt injection through RAG**: a poisoned document makes the agent invoke
    a tool the user never asked for. Report what guardrails caught, what they missed, and why the
    IAM boundary on the agent's role is the only deterministic control.
  - **AIS-006 — Grading the investigation agent**: log bundles with known ground truth, including
    bundles engineered so the only correct answer is "insufficient evidence", fed to an agent that
    must produce an attribution. Measure the hallucinated-attribution rate across N runs, publish
    the eval harness, and show the instruction change that moved the rate.
- **Done when:** the agent's error rate is stated as a range over repeated runs rather than a single
  number, and the write-up names the class of question on which it is reliably wrong.

## Running throughout

- **One offensive exercise a week.** flaws.cloud, CloudGoat and IAM Vulnerable for AWS, plus the
  free tier of a cloud pentest lab platform. Hands-on offensive work — including CTF participation
  — is a stated minimum qualification in some of these postings, not a bonus.
- **One write-up per artifact, published the same week it is built.** The backlog of unwritten labs
  is the failure mode of every portfolio.
- **One detection engineering or cloud incident post-mortem read per week**, with the technique
  added to the backlog in [MITRE-Coverage.md](MITRE-Coverage.md) if it is not already there.
- **Tear down the same day.** Every lab is tagged and swept per Phase 0. Cost discipline is part of
  the skill, not overhead around it.

## Readiness check

At the end of the twelve weeks, each of the following should point at a published artifact rather
than at a claim:

- **A log query language** → SEC-001, in three dialects.
- **Cloud posture triage** → SEC-002 and SEC-003 on AWS, SEC-007 on GCP.
- **Detection maintenance and false-positive hunting** → SEC-003's measured precision and coverage.
- **Timeline reconstruction with evidence** → the evidence directories, which show the decisive
  field rather than a log dump.
- **Identity and authentication** → SEC-004 and SEC-005, including a token inspected claim by claim.
- **Secure code review and CI/CD security** → SEC-006, with a triage decision that had to be
  defended.
- **Two clouds** → the AWS-to-GCP mapping in SEC-007.
- **Generative AI in a technical context, with skepticism about its output** → AIS-003, AIS-006, and
  the verification log.
- **Explaining findings to non-specialists** → every README, which is why the plan spends ten
  percent of its time on writing.

Gaps that will remain, to be stated plainly rather than papered over: EDR console operation,
phishing triage with commercial sandbox and threat-intel tooling, and incident management platform
experience.
