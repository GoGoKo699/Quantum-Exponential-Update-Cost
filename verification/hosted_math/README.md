# Hosted mathematics verification

These generic utilities inventory exact Git objects, compile reference MathML, and compare every mathematical expression with the real commit-pinned GitHub page at wide and narrow widths. Screenshots support a separate visual review. A structural pass does not establish scientific correctness or arbitrary mathematical equivalence.

The read-only workflow in `.github/workflows/hosted-math.yml` checks out the proposed source without persisted credentials. It first probes the README, then captures the complete tracked Markdown scope using Playwright and MathJax. The runtime uses pinned dependencies in temporary storage. The scripts never write to a remote repository, authenticate a browser or change access settings.

To run the complete capture in a compatible local runtime:

```bash
npm install --prefix /absolute/temporary/dependencies playwright@1.56.1 mathjax-full@3.2.1
node /absolute/temporary/dependencies/node_modules/playwright/cli.js install chromium
NODE_PATH=/absolute/temporary/dependencies/node_modules node verification/hosted_math/capture_hosted_math.cjs \
  --root /absolute/repository --repository GoGoKo699/Quantum-Exponential-Update-Cost \
  --revision FULL_COMMIT_SHA --output /absolute/new-empty-evidence-directory
```

Use an actually observed full commit SHA and a new output directory. The representative-page probe takes the same arguments plus `--page README.md`. Its result is diagnostic only. Preserve failed attempts, inspect actual screenshots and repeat affected capture after a source repair. Expiring workflow artifacts are reproducible verification caches, rather than permanent scientific data.
