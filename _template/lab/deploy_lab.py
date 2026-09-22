#!/usr/bin/env python3
"""
SEC-XXX Lab: <what this deploys>

Subcommands:
  deploy     Create all infrastructure (resumable)
  status     Show what currently exists
  test       Assert the detection and response behave as documented
  teardown   Delete everything deploy created

State lives in resources.json (gitignored) so deploy is resumable and teardown knows what to
remove. Every resource is tagged so orphans can be found by tag.
"""

import argparse
import json
import sys
from pathlib import Path

import boto3
from botocore.exceptions import ClientError

SCENARIO = "SEC-XXX"
PREFIX = "sec-xxx"
DEFAULT_REGION = "us-east-1"
STATE_FILE = Path(__file__).with_name("resources.json")

TAGS = [
    {"Key": "Project", "Value": "aws-security-engineering"},
    {"Key": "Scenario", "Value": SCENARIO},
    {"Key": "Ephemeral", "Value": "true"},
]


# --- state -------------------------------------------------------------------

def load_state():
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text())
    return {}


def save_state(state):
    STATE_FILE.write_text(json.dumps(state, indent=2, default=str))


# --- session -----------------------------------------------------------------

def make_session(args):
    session = boto3.Session(profile_name=args.profile, region_name=args.region)
    account_id = session.client("sts").get_caller_identity()["Account"]
    print(f"account {account_id} · region {args.region} · scenario {SCENARIO}")
    return session, account_id


# --- lifecycle ---------------------------------------------------------------

def deploy(session, account_id, state):
    """Create infrastructure. Each step must be idempotent and recorded in state."""
    # Example shape — replace with the scenario's resources.
    #
    # if "role_arn" not in state:
    #     iam = session.client("iam")
    #     resp = iam.create_role(RoleName=f"{PREFIX}-target", AssumeRolePolicyDocument=..., Tags=TAGS)
    #     state["role_arn"] = resp["Role"]["Arn"]
    #     save_state(state)
    #     print(f"  created role {state['role_arn']}")
    # else:
    #     print(f"  role already exists: {state['role_arn']}")
    raise NotImplementedError("implement deploy for this scenario")


def status(session, account_id, state):
    """Print what exists according to state, verified against the API."""
    if not state:
        print("nothing deployed (no resources.json)")
        return
    for key, value in state.items():
        print(f"  {key}: {value}")
    # Verify each recorded resource still exists so status does not lie after a partial teardown.


def test(session, account_id, state):
    """Assert documented behavior. Prints PASS/FAIL per assertion, exits non-zero on failure."""
    failures = []

    def check(name, condition, detail=""):
        print(f"  [{'PASS' if condition else 'FAIL'}] {name}{' — ' + detail if detail else ''}")
        if not condition:
            failures.append(name)

    # check("detection fired within 15 minutes", finding is not None, f"finding id {finding_id}")
    # check("containment revoked the session", access_denied, "second call returned AccessDenied")
    raise NotImplementedError("implement tests for this scenario")

    if failures:
        print(f"\n{len(failures)} assertion(s) failed")
        sys.exit(1)
    print("\nall assertions passed")


def teardown(session, account_id, state):
    """Delete everything deploy created, in dependency order. Idempotent."""
    if not state:
        print("nothing to tear down")
        return
    # Delete in reverse dependency order, tolerating already-deleted resources:
    #
    # if "role_arn" in state:
    #     try:
    #         session.client("iam").delete_role(RoleName=f"{PREFIX}-target")
    #         print("  deleted role")
    #     except ClientError as e:
    #         if e.response["Error"]["Code"] != "NoSuchEntity":
    #             raise
    #     state.pop("role_arn")
    #     save_state(state)
    raise NotImplementedError("implement teardown for this scenario")


# --- entrypoint --------------------------------------------------------------

COMMANDS = {"deploy": deploy, "status": status, "test": test, "teardown": teardown}


def main():
    parser = argparse.ArgumentParser(description=f"{SCENARIO} lab")
    parser.add_argument("command", choices=COMMANDS)
    parser.add_argument("--profile", default=None, help="AWS profile for a dedicated lab account")
    parser.add_argument("--region", default=DEFAULT_REGION)
    args = parser.parse_args()

    session, account_id = make_session(args)
    state = load_state()
    COMMANDS[args.command](session, account_id, state)


if __name__ == "__main__":
    main()
