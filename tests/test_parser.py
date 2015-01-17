# -*- coding: utf-8 -*-
import os
import types
from RISparser import readris

pj = os.path.join


class TestRISparser():

    def test_parse_example_basic_ris(self):
        filepath = os.getcwd() + '/example_basic.ris'
        ristags = [
            {'TY': 'JOUR'},
            {'AU': 'Shannon,Claude E.'},
            {'PY': '1948/07//'},
            {'TI': 'A Mathematical Theory of Communication'},
            {'JO': 'Bell System Technical Journal'},
            {'SP': '379'},
            {'EP': '423'},
            {'VL': '27'},
        ]
        entries = list(readris(filepath))
        assert len(entries)
        for ristag in ristags:
            k, v = ristag.popitem()
            assert k in entries[0]
            assert v == entries[0][k].strip()

    def test_parse_example_full_ris(self):
        filepath = os.getcwd() + '/example_full.ris'
        ristags = [
            {'TY': 'JOUR'},
            {'ID': '12345'},
            {'T1': 'Title of reference'},
            {'A1': ['Marx, Karl', 'Lindgren, Astrid', 'Glattauer, Daniel']},
            {'Y1': '2014//'},
            {'N2': 'BACKGROUND: Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.  RESULTS: Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. CONCLUSIONS: Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium.'},
            {'KW': ['Pippi', 'Nordwind', 'Piraten']},
            {'JF': 'Lorem'},
            {'JA': 'lorem'},
            {'VL': '9'},
            {'IS': '3'},
            {'SP': 'e0815'},
            {'CY': 'United States'},
            {'PB': ['Fun Factory', 'Fun Factory USA']},
            {'SN': '1932-6208'},
            {'M1': '1008150341'},
            {'L2': 'http://example.com'},
        ]
        entries = list(readris(filepath))
        assert len(entries) == 2
        for ristag in ristags:
            k, v = ristag.popitem()
            assert k in entries[0]
            if isinstance(v, types.ListType):
                assert ''.join(v) == ''.join(entries[0][k])
            else:
                assert v == entries[0][k].strip()
