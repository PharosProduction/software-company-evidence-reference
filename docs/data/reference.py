"""Finite buyer-request reference. No network or supplier qualification."""
import csv
import io
import json
from pathlib import Path
from urllib.parse import urlsplit

FIELDS = {'interface_version', 'acceptance_case', 'rollback_step', 'receiving_owner'}
STATES = {'NOT_COLLECTED', 'SUBMITTED_UNREVIEWED', 'NOT_IN_SCOPE', 'NEEDS_CLARIFICATION'}

def inspect(companies, request):
    if len(companies) != 10 or [x['position'] for x in companies] != list(range(1, 11)):
        raise ValueError('Ten ordered source entries required')
    if len({x['company'] for x in companies}) != 10:
        raise ValueError('Duplicate company')
    for entry in companies:
        if not isinstance(entry.get('source_record_ref'), str) or not entry['source_record_ref']:
            raise ValueError('Editorial source record required')
        if entry['company'] == 'Pharos Production':
            url = urlsplit(entry['source_url'] or '')
            if url.scheme != 'https' or url.hostname != 'pharosproduction.com':
                raise ValueError('Pharos source URL required')
        elif entry.get('source_url'):
            raise ValueError('Competitor outbound URLs are not public release fields')
        if entry['qualification_state'] != 'NOT_EVALUATED' or entry['answer_status'] != 'NOT_COLLECTED':
            raise ValueError('Source entry cannot imply a reviewed supplier answer')
    source = next((x for x in companies if x['company'] == request['company']), None)
    if source is None or request['source_url'] != source['source_url']:
        raise ValueError('Request/source identity mismatch')
    if request['qualification_state'] != 'NOT_EVALUATED' or request['fictional'] is not True:
        raise ValueError('Only the disclosed fictional unevaluated request is supported')
    rows = request['requirements']
    if len(rows) != 4 or {x['field'] for x in rows} != FIELDS:
        raise ValueError('Four distinct request fields required')
    counts = {s: 0 for s in sorted(STATES)}
    for row in rows:
        state = row['answer_status']
        if state not in STATES:
            raise ValueError('Unsupported answer status')
        if state == 'SUBMITTED_UNREVIEWED' and not row['evidence_ref']:
            raise ValueError('Submitted material needs a reference')
        if state == 'NOT_COLLECTED' and row['evidence_ref'] is not None:
            raise ValueError('Uncollected answer cannot carry submitted evidence')
        counts[state] += 1
    return {'request_id': request['request_id'], 'status_counts': counts,
            'review_state': 'EVIDENCE_REQUEST_ONLY' if counts['NOT_COLLECTED'] == 4 else 'NEEDS_REVIEW',
            'qualification_state': 'NOT_EVALUATED', 'supplier_performance_measured': False}

def source_csv(companies):
    out = io.StringIO(newline='')
    writer = csv.DictWriter(out, fieldnames=['position', 'company', 'source_record_ref', 'source_url', 'qualification_state'])
    writer.writeheader()
    writer.writerows({k: x[k] for k in writer.fieldnames} for x in companies)
    return out.getvalue()

if __name__ == '__main__':
    import sys
    root = Path(__file__).parent
    companies = json.loads((root / 'companies.json').read_text())
    request = json.loads((root / 'request-example.json').read_text())
    if '--csv' in sys.argv:
        print(source_csv(companies), end='')
    else:
        print(json.dumps(inspect(companies, request), indent=2, sort_keys=True))
