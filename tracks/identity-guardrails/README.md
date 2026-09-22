# Identity & Guardrails

Preventive controls: what a principal can do at all, enforced at the organization boundary and in
the pipeline rather than reviewed after the fact.

## Scope

- **Least privilege** — IAM Access Analyzer policy generation from CloudTrail activity, then
  narrowing by condition keys instead of by action lists.
- **Organization controls** — service control policies, resource control policies, delegated
  administration, and the failure modes of an SCP that is correct but unenforceable.
- **Boundaries** — permission boundaries for delegated administration, role trust policy design,
  and confused-deputy protection with `aws:SourceArn` and `aws:SourceAccount`.
- **Policy as code** — Checkov and cfn-guard in CI, IAM policy simulation in tests, and a build
  that fails on a policy regression.

## Published scenarios

None yet.

## Planned

- **PassRole escalation** (T1548.005) — a principal with narrow permissions plus `iam:PassRole`
  reaching administrator through a service it is allowed to invoke; the boundary that stops it.
- **SCPs with proof** — each guardrail paired with a test that attempts the forbidden action and
  asserts the deny, including the cases where an SCP silently does not apply.
- **Least privilege from real traffic** — generating a policy from Access Analyzer, measuring what
  it over-grants, and closing the gap with condition keys.
- **Cross-account trust review** — enumerating every principal outside the organization that can
  assume a role or read a bucket, and the conditions that should be required.

## Guardrail bar

A control claim needs a test that fails when the control is removed. Every scenario ships the
negative test, not only the happy path.
