---
blogpost: true
date: 2026-09-12 08:00:00
tags: GitHub, GitHub Actions, Dependabot, Supply Chain Security
category: GitOps
---

# Automate pull-request approval for Dependabot

[Dependabot](https://github.com/dependabot) is a service that automatically updates your project dependencies by creating pull requests. It is a great tool to keep your project up-to-date with the latest security patches and bug fixes. However, managing these pull requests can be time-consuming, especially if you have many dependencies. As a result, many teams end up ignoring Dependabot pull requests, which can lead to security vulnerabilities and other issues.

> [!Warning]
> Auto-merging should be used with caution. Ensure that only trusted dependencies are automatically merged and that your workflow conditions are well-defined to avoid merging changes that could lead to supply chain attacks.

## Setting up Dependabot

The example configuration below, stored in `.github/dependabot.yml`, shows that Dependabot will automatically update the Docker base image and GitHub Actions. It ignores major version updates for Amazon Linux, Fedora, Oracle Linux, and Rocky Linux reducing the noise in the pull requests.

```yaml
---
version: 2
updates:
  - package-ecosystem: docker
    target-branch: master
    directory: /
    schedule:
      interval: daily
    ignore:
      - dependency-name: "amazonlinux"
        update-types: ["version-update:semver-major"]
      - dependency-name: "fedora"
        update-types: ["version-update:semver-major"]
      - dependency-name: "oraclelinux"
        update-types: ["version-update:semver-major"]
      - dependency-name: "rockylinux"
        update-types: ["version-update:semver-major"]

  - package-ecosystem: github-actions
    target-branch: master
    directory: /
    schedule:
      interval: monthly
    groups:
      github-actions:
        patterns:
          - "*"  # Update all GitHub Actions
```

## Setting up auto-merge for Dependabot

To further automate the process, you can use GitHub Actions to automatically approve and merge Dependabot pull requests. The example workflow stored in `.github/workflows/dependabot-auto-merge.yml` shows how to enable auto-merge for Dependabot pull requests that update the Docker base image and are patch version updates.

```yaml
---
name: Dependabot auto-merge

on:
  pull_request:

permissions:
  contents: write
  pull-requests: write

jobs:
  dependabot:
    runs-on: ubuntu-latest
    if: github.actor == 'dependabot[bot]'
    steps:
      - name: Dependabot metadata
        id: metadata
        uses: dependabot/fetch-metadata@v2
        with:
          github-token: "${{ secrets.GITHUB_TOKEN }}"
      - name: Enable auto-merge for Dependabot PRs
        if: contains(steps.metadata.outputs.package-ecosystem, 'docker') && steps.metadata.outputs.update-type == 'version-update:semver-patch'
        run: gh pr merge --auto --merge "$PR_URL"
        env:
          PR_URL: ${{github.event.pull_request.html_url}}
          GH_TOKEN: ${{secrets.GITHUB_TOKEN}}
```

This workflow runs on every pull request and checks if the pull request is from Dependabot and updates the Docker base image with a patch version update. If the conditions are met, it enables auto-merge for the pull request.

## When to use auto-merge for Dependabot

With this setup, you can keep your project dependencies up-to-date without manual intervention, reducing the risk of security vulnerabilities and other issues. An essential consideration is to ensure that the auto-merge conditions are strict enough to prevent merging breaking changes automatically. You can adjust the conditions in the workflow to match your project's requirements.
