#!/usr/bin/env python3
"""
Validate that setuptools_scm version matches the Git tag.

This script is used in the GitHub Actions publish workflow to ensure
the package version matches the release tag.

Usage:
    python scripts/validate_version.py <scm_version> <git_tag>
    
Exit codes:
    0: Version validation passed
    1: Version mismatch or error
"""

import sys
from packaging.version import parse, Version


def main():
    if len(sys.argv) != 3:
        print("Usage: python scripts/validate_version.py <scm_version> <git_tag>")
        sys.exit(1)
    
    scm_version = sys.argv[1]
    tag_version = sys.argv[2]
    
    print(f"SCM Version: {scm_version}")
    print(f"Git Tag: {tag_version}")
    
    try:
        # Parse the versions
        scm_parsed = parse(scm_version)
        tag_parsed = parse(tag_version)
        
        # Extract base version (without local/dev/post parts)
        scm_base = scm_parsed.base_version
        tag_base = tag_parsed.base_version
        
        print(f"SCM base version: {scm_base}")
        print(f"Tag base version: {tag_base}")
        
        # For releases, we expect the base versions to match
        if scm_base != tag_base:
            print(f"ERROR: Base version mismatch: setuptools_scm={scm_base}, tag={tag_base}")
            sys.exit(1)
        
        # Additional check: for a release tag, setuptools_scm should give us a clean version
        # (no dev, post, or local parts) when on the exact tag commit
        if scm_parsed.is_devrelease or scm_parsed.post is not None or scm_parsed.local is not None:
            print(f"WARNING: setuptools_scm returned a non-release version: {scm_version}")
            print("This may indicate the tag is not on the current commit.")
            # We'll allow this to proceed but log the warning
        
        print("Version validation passed!")
        return 0
        
    except Exception as e:
        print(f"ERROR: Failed to parse versions: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())