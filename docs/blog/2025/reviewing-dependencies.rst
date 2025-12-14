.. post:: 2025-12-14 08:00:00
    :tags: GitHub Actions, dependencies
    :category: Software Development, Security & Compliance

Reviewing dependencies
======================

In modern software development, managing and reviewing dependencies is crucial for maintaining the security, performance, and reliability of your projects. Dependencies are external libraries or packages that your project relies on to function correctly. However, they can also introduce vulnerabilities or compatibility issues if not properly managed.

Why review dependencies?
------------------------

Adding third-party dependencies can save development time and effort, but it also comes with risks. Vulnerabilities in dependencies can be exploited by attackers, leading to security breaches. Additionally, outdated or unmaintained dependencies can cause compatibility issues and hinder the development process.

Regularly reviewing your project's dependencies helps to:

- Identify and mitigate security vulnerabilities.
- Ensure that dependencies are actively maintained and supported.
- Verify licensing compliance.
- Ensure compatibility with your project's codebase.
- Keep your project up-to-date with the latest features and bug fixes.
- Reduce bloat by removing unused or unnecessary dependencies.

This review process should be an integral part of your development workflow as it helps maintain the overall health of your project and protects against potential risks associated with third-party code. While manual reviews are essential, leveraging automated tools can significantly enhance the efficiency and effectiveness of this process. The first step is to identify all dependencies used in your project and start evaluating the used licensing.

Reviewing licenses with GitHub Actions
--------------------------------------

Reviewing licenses of dependencies can be a daunting task, especially for large projects with numerous dependencies. Fortunately, GitHub Actions provides a way to automate this process using the :github:repo:`Dependency Review Action <actions/dependency-review-action>`. This action scans the dependency manifest files that change as part of a Pull Request (PR) and surfaces known-vulnerable versions of the packages declared or updated in the PR. By integrating this action into your CI/CD pipeline, you can ensure that any PR introducing known-vulnerable packages will be blocked from merging.

To set up the Dependency Review Action in your GitHub repository, you can create a workflow file in the `.github/workflows` directory of your repository. Below is an example of a GitHub Actions workflow that utilizes the Dependency Review Action:

.. code-block:: yaml
    :caption: GitHub Actions workflow for dependency review

    # Dependency Review Action
    #
    # This Action will scan dependency manifest files that change as part of a Pull Request,
    # surfacing known-vulnerable versions of the packages declared or updated in the PR.
    # Once installed, if the workflow run is marked as required, PRs introducing known-vulnerable
    # packages will be blocked from merging.
    #
    # Source repository: https://github.com/actions/dependency-review-action
    # Public documentation: https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/about-dependency-review#dependency-review-enforcement
    ---
    name: 'Dependency review'

    on:
      pull_request:
        branches: [ "master" ]

    # If using a dependency submission action in this workflow this permission will need to be set to:
    #
    # permissions:
    #   contents: write
    #
    # https://docs.github.com/en/enterprise-cloud@latest/code-security/supply-chain-security/understanding-your-software-supply-chain/using-the-dependency-submission-api
    permissions:
      contents: read
      # Write permissions for pull-requests are required for using the `comment-summary-in-pr` option, comment out if you aren't using this option
      pull-requests: write

    jobs:
      dependency-review:
        runs-on: ubuntu-latest
        steps:
          - name: 'Checkout repository'
            uses: actions/checkout@v6

          - name: 'Dependency Review'
            uses: actions/dependency-review-action@v4
            # Commonly enabled options, see https://github.com/actions/dependency-review-action#configuration-options for all available options.
            with:
              comment-summary-in-pr: always
              allow-licenses: GPL-2.0-or-later, LGPL-2.1-or-later, GFDL-1.1-or-later, MIT, MPL-2.0, CC-BY-4.0, CC-BY-SA-4.0, Apache-2.0


.. warning::

    The allowed licenses specified in the example above are for demonstration purposes only. It is essential to review and select licenses that align with your project's licensing requirements and policies.

As shown in the example above, the action is triggered on pull requests targeting the `master` branch. It checks out the repository and runs the Dependency Review Action, which scans the changed dependency manifest files for known vulnerabilities. The `allow-licenses` option is used to specify a list of acceptable licenses for the dependencies. The action will block the merging of pull requests that introduce dependencies with licenses not included in this list which is a subset of all licenses defined in the `SPDX License List <//spdx.org/licenses/>`_ as Free/Libre licenses.

.. note::

    The option ``deny-licenses`` can also be used to block specific licenses if your project has strict licensing requirements. For example, you might want to deny licenses that are incompatible with your project's license or those that impose certain restrictions. The option has been marked as deprecated and it is recommended to use ``allow-licenses`` instead to specify only the licenses that are acceptable for your project.

Choosing the right licenses
---------------------------

When selecting licenses for your dependencies, it's essential to consider the compatibility with your project's license and the implications of using certain licenses. Some licenses may have restrictions that could affect how you can use, modify, or distribute your project. Common open-source licenses include MIT, Apache 2.0, GPL, and BSD, each with its own set of terms and conditions. It's advisable to consult with legal experts or use tools that can help analyze license compatibility to ensure that your project remains compliant with all applicable licenses.

For a comprehensive list of licenses and their details, you can refer to the `SPDX License List <//spdx.org/licenses/>`_ for standardized identifiers and information about various free/libre-source and Open Source Initiative approved licenses. It is a good practice to document the licenses of all dependencies used in your project to maintain transparency and facilitate future reviews as it evolves and will be part of :wikipedia:`SBOM (Software Bill of Materials) <SBOM>` for your project.

Conclusion about reviewing dependencies
---------------------------------------

In conclusion, reviewing dependencies is a crucial aspect of maintaining a secure and compliant software project. By leveraging tools like GitHub Actions and the Dependency Review Action, you can automate the process of identifying and addressing potential issues with your dependencies. Additionally, establishing clear guidelines for acceptable licenses and regularly reviewing your dependency tree can help mitigate risks and ensure that your project remains aligned with its licensing requirements.

On a final note, automated tools can only go so far in identifying potential issues with dependencies. The biggest concerns is the quality and trustworthiness of the dependencies themselves and the data sources they rely on. For some projects the dependency review already showed already that not all packages are covered equally well as some scoring objectives weren't implemented. Here also lies a problem with dependencies that lack proper maintenance to implement all the latest security practices due to various reasons.
