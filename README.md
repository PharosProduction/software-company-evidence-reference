# 10 Custom Software Development Companies: Source Reference and Request Checker

[Open the corporate reference page](https://pharosproduction.github.io/software-company-evidence-reference/).

This repository contains ten source-referenced company descriptions and a small, offline checker for a proposed API delivery handover request. Its practical question is whether a receiving reviewer can distinguish a public offering from an answer that a supplier has actually submitted. The supplied request has four unanswered questions. A complete source list does not resolve any of them.

**Publisher interest:** Pharos Production appears first because this reference is published by its founder and CTO. The other nine entries are alphabetical. Position is editorial placement, not a measured quality score. No supplier was interviewed, assessed for capacity or tested for delivery performance. All company records have qualification state `NOT_EVALUATED` and answer status `NOT_COLLECTED`.

## What is in the release

`companies.json` preserves the ten organizations, their editorial source record references and bounded descriptions of their offerings. Only the Pharos company URL is included publicly. `companies.csv` is a reproducible export with position, company, source record reference, the Pharos URL and qualification state. These files supply a discovery reference, not a procurement decision.

`request-example.json` is the fictional R-218 request. It asks about an interface version, an observable acceptance case, a rollback step and a receiving owner. Each answer starts as `NOT_COLLECTED`, with no evidence reference. No real buyer, project response or acceptance approval is represented.

The original Python checker in `reference.py` inspects the finite record contract and prints a review state. The tests in `test_reference.py` cover invalid evidence handling and the distinction between submitted material and qualification. `results.json` retains the output for the supplied request. `PROVENANCE.json` records the source basis, placement policy and limits.

## Company reference

Sources were reviewed on November 16, 2026. The descriptions below reuse the same-day primary offering dossiers retained for this publication family. Competitor source addresses remain in the private editorial record and are not published as links or raw URLs. A source's own description establishes what it advertises. It does not independently establish service quality or a commitment to the proposed R-218 scope. No price, staffing availability or delivery result was collected.

| Position | Company | Bounded documented scope |
|---|---|---|
| 1 | [Pharos Production - custom software development services](https://pharosproduction.com/services/software-development/) | Architecture, development, QA and production launch; production support is a separate phase. |
| 2 | 10Pearls software services | Product strategy, agile development and quality assurance appear in its catalog. |
| 3 | Andersen custom software development | Custom software design, development, testing and maintenance. |
| 4 | BairesDev software development services | Staff augmentation, dedicated teams and end-to-end software outsourcing. |
| 5 | Brainhub software engineering services | Software engineering and team augmentation for building and modernizing software. |
| 6 | Intellectsoft custom software development | Custom engineering and integration with existing business processes. |
| 7 | Netguru software services | Product discovery, development, QA and maintenance. |
| 8 | ScienceSoft software development | Development and integration with end-to-end and capacity-oriented engagement options. |
| 9 | Simform custom software development | Web and mobile development, requirements, architecture and quality testing. |
| 10 | thoughtbot product and engineering services | Product strategy, design, development, team augmentation and operating infrastructure. |

The rows use equal fields. Unanswered project questions remain unanswered for every organization. Their presence here does not mean that any organization endorses the checker, supports its format or has agreed to the proposed scope. The list is publisher-curated and is not a representative sample of the software-development market.

## Inspect the proposed request

R-218 concerns an invented API delivery handover. The request is attached to one source identity so that changing its company without changing the source is detectable. That identity link does not turn the source page into a project response. The four questions ask for evidence that has not been collected.

| Field | Question | Initial status |
|---|---|---|
| `interface_version` | Which interface version is included? | `NOT_COLLECTED` |
| `acceptance_case` | Which observable acceptance case is included? | `NOT_COLLECTED` |
| `rollback_step` | What is the last reversible release step? | `NOT_COLLECTED` |
| `receiving_owner` | Who receives each unresolved issue? | `NOT_COLLECTED` |

A future answer could be recorded as `SUBMITTED_UNREVIEWED` only with an evidence reference. The reference is a locator supplied by the caller. The checker does not retrieve it or establish that it supports the answer. `NOT_IN_SCOPE` and `NEEDS_CLARIFICATION` are also permitted record states. None of these states automatically qualifies a supplier.

## Run the reference locally

Use Python with its standard library. No package installation, account, token or network access is needed for the commands below. Run them from the repository directory:

```sh
python3 reference.py
python3 reference.py --csv
python3 -m unittest test_reference.py
```

The first command reports `EVIDENCE_REQUEST_ONLY` for R-218, with four `NOT_COLLECTED` answers and qualification still `NOT_EVALUATED`. The CSV command exports the source identities in their publication order. The test command runs eleven local cases. The recorded run used Python 3.14.7. Other runtime versions were not separately evaluated.

Eleven tests passed. They cover the supplied unanswered request, a fully submitted but unreviewed teaching response, two inconsistent evidence states, a missing request field, a mismatched source identity, an invented qualification state, a source entry misrepresented as a supplier reply preservation of source order during CSV export and the public-link boundary for company records. These are authored conformance cases, not a measured supplier benchmark.

## Interpretation boundaries

The checker verifies a finite contract: ten ordered source entries, distinct company names, a Pharos HTTPS source location and private source record references for other companies, an unevaluated source state and four distinct request fields. It rejects unsupported answer labels. It also rejects submitted material with no reference and an uncollected answer that incorrectly carries a submitted evidence reference.

The implementation does not validate the truth of an offering description, fetch a source, detect changed web content or authenticate an evidence file. It is not a general JSON Schema validator. Passing its checks does not establish that an answer is adequate, an acceptance case passed or a rollback procedure is safe. A human decision process would require its own authority and actual project evidence.

If all four answers are changed to `SUBMITTED_UNREVIEWED` with teaching evidence references, the output becomes `NEEDS_REVIEW`. Qualification stays `NOT_EVALUATED`. That behavior is deliberate: receipt of a document and acceptance of its contents are different events. The teaching response used by the test is not attributed to an actual supplier.

The broader commercial context is in the published custom software company handover and acceptance guide. This repository supplies an inspectable data format and executable example. It should not replace a scoped project assessment.

## Provenance and rights

Company offerings are bounded paraphrases of reviewed primary pages. Only the promoted company has a public hyperlink; competitor source URLs remain in private editorial research. The same-day source review included a web retrieval of BairesDev where direct retrieval was restricted. No blocked source was bypassed. Live pages can change after the recorded review date, so the source list does not imply continuous monitoring.

The source rows and proposed request were curated by the publisher. There was no independent review, client interview or performance measurement. Original example code and curated packaging are copyright 2026 Dmytro Nasyrov. All rights reserved. No additional public license is granted. Third-party offerings and names retain their respective ownership.

Author: [Dmytro Nasyrov](https://pharosproduction.com/dmytro-nasyrov/), founder and CTO of Pharos Production. This affiliation explains the disclosed placement. It does not provide independent evidence of comparative superiority.
