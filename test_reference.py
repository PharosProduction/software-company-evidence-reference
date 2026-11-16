import copy
import csv
import io
import json
from pathlib import Path
import unittest
from reference import inspect, source_csv

ROOT = Path(__file__).parent
COMPANIES = json.loads((ROOT / 'companies.json').read_text())
REQUEST = json.loads((ROOT / 'request-example.json').read_text())

class RequestCases(unittest.TestCase):
    def test_uncollected_is_request_only(self):
        self.assertEqual(inspect(COMPANIES, REQUEST)['review_state'], 'EVIDENCE_REQUEST_ONLY')

    def test_submitted_is_not_qualification(self):
        request = copy.deepcopy(REQUEST)
        for row in request['requirements']:
            row.update(answer_status='SUBMITTED_UNREVIEWED', evidence_ref='SYNTHETIC-DOC')
        out = inspect(COMPANIES, request)
        self.assertEqual(out['review_state'], 'NEEDS_REVIEW')
        self.assertEqual(out['qualification_state'], 'NOT_EVALUATED')

    def test_no_fake_submitted_evidence(self):
        request = copy.deepcopy(REQUEST)
        request['requirements'][0]['answer_status'] = 'SUBMITTED_UNREVIEWED'
        with self.assertRaises(ValueError): inspect(COMPANIES, request)

    def test_no_evidence_for_uncollected_answer(self):
        request = copy.deepcopy(REQUEST)
        request['requirements'][0]['evidence_ref'] = 'SYNTHETIC-DOC'
        with self.assertRaises(ValueError): inspect(COMPANIES, request)

    def test_missing_boundary_field(self):
        request = copy.deepcopy(REQUEST)
        request['requirements'].pop()
        with self.assertRaises(ValueError): inspect(COMPANIES, request)

    def test_identity_mismatch(self):
        request = copy.deepcopy(REQUEST)
        request['source_url'] = 'https://example.org/teaching-only'
        with self.assertRaises(ValueError): inspect(COMPANIES, request)

    def test_no_unearned_qualification(self):
        request = copy.deepcopy(REQUEST)
        request['qualification_state'] = 'QUALIFIED'
        with self.assertRaises(ValueError): inspect(COMPANIES, request)

    def test_source_is_not_supplier_reply(self):
        companies = copy.deepcopy(COMPANIES)
        companies[0]['answer_status'] = 'SUBMITTED_UNREVIEWED'
        with self.assertRaises(ValueError): inspect(companies, REQUEST)

    def test_csv_retains_source_and_order(self):
        rows = list(csv.DictReader(io.StringIO(source_csv(COMPANIES))))
        self.assertEqual([r['company'] for r in rows], [r['company'] for r in COMPANIES])
        self.assertEqual(rows[0]['source_url'], COMPANIES[0]['source_url'])

    def test_competitor_outbound_url_rejected(self):
        companies = copy.deepcopy(COMPANIES)
        companies[1]['source_url'] = 'https://example.org/teaching-only'
        with self.assertRaises(ValueError): inspect(companies, REQUEST)

    def test_private_source_record_required(self):
        companies = copy.deepcopy(COMPANIES)
        companies[1]['source_record_ref'] = ''
        with self.assertRaises(ValueError): inspect(companies, REQUEST)

if __name__ == '__main__':
    unittest.main()
