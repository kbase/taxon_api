import unittest
import time

from os import environ
from configparser import ConfigParser

from biokbase.workspace.client import Workspace as workspaceService
from TaxonAPI.TaxonAPIImpl import TaxonAPI
from TaxonAPI.TaxonAPIServer import MethodContext


class taxon_apiTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        token = environ.get('KB_AUTH_TOKEN', None)
        # WARNING: don't call any logging methods on the context object,
        # it'll result in a NoneType error
        cls.ctx = MethodContext(None)
        cls.ctx.update({'token': token,
                        'provenance': [
                            {'service': 'taxon_api',
                             'method': 'please_never_use_it_in_production',
                             'method_params': []
                             }],
                        'authenticated': 1})
        config_file = environ.get('KB_DEPLOYMENT_CONFIG', None)
        cls.cfg = {}
        config = ConfigParser()
        config.read(config_file)
        for nameval in config.items('TaxonAPI'):
            cls.cfg[nameval[0]] = nameval[1]
        cls.wsURL = cls.cfg['workspace-url']
        cls.wsClient = workspaceService(cls.wsURL, token=token)
        cls.serviceImpl = TaxonAPI(cls.cfg)
        cls.taxon = 'ReferenceTaxons/280699_taxon/1'
        cls.parent = u'ReferenceTaxons/45157_taxon/1'
        cls.root_taxon = 'ReferenceTaxons/1_taxon/1'

    @classmethod
    def tearDownClass(cls):
        if hasattr(cls, 'wsName'):
            cls.wsClient.delete_workspace({'workspace': cls.wsName})
            print('Test workspace was deleted')

    def getWsClient(self):
        return self.__class__.wsClient

    def getWsName(self):
        if hasattr(self.__class__, 'wsName'):
            return self.__class__.wsName
        suffix = int(time.time() * 1000)
        wsName = "TaxonAPI_" + str(suffix)
        self.getWsClient().create_workspace({'workspace': wsName})
        self.__class__.wsName = wsName
        return wsName

    def getImpl(self):
        return self.__class__.serviceImpl

    def getContext(self):
        return self.__class__.ctx

    def test_get_parent(self):
        ret = self.getImpl().get_parent(self.getContext(), self.taxon)
        parent_ref_id = self.wsClient.get_objects2({'objects': [{'ref': self.parent}]})['data'][0]['path'][0]
        self.assertEqual(ret[0], parent_ref_id)

        ret = self.getImpl().get_parent(self.getContext(), self.root_taxon)
        self.assertEqual(ret[0], '')

    def test_get_all_data(self):
        ret = self.getImpl().get_all_data(self.getContext(),
                                          {'ref': self.taxon})
        parent_ref_name = ret[0]['parent']
        parent_ref_id = self.wsClient.get_objects2({'objects': [{'ref': parent_ref_name}]})['data'][0]['path'][0]
        self.assertEqual(ret[0]['parent'], parent_ref_id)
        self.assertTrue('decorated_scientific_lineage' not in ret[0])
        self.assertTrue('decorated_children' not in ret[0])
        self.assertEqual(ret[0]['children'], [])
        self.assertEqual(ret[0]['domain'], 'Eukaryota')
        self.assertEqual(ret[0]['genetic_code'], 1)
        self.assertEqual(ret[0]['scientific_name'],
                         'Cyanidioschyzon merolae strain 10D')
        self.assertEqual(ret[0]['taxonomic_id'], 280699)
        item = {
            'ref': self.taxon,
            'include_decorated_scientific_lineage': 1
        }

        ret = self.getImpl().get_all_data(self.getContext(), item)
        parent_ref_name = ret[0]['parent']
        parent_ref_id = self.wsClient.get_objects2({'objects': [{'ref': parent_ref_name}]})['data'][0]['path'][0]
        self.assertEqual(ret[0]['parent'], parent_ref_id)
        self.assertTrue('decorated_scientific_lineage' in ret[0])
        self.assertTrue('decorated_children' not in ret[0])

        ret = self.getImpl().get_all_data(self.getContext(),
                                          {'ref': self.parent,
                                          'exclude_children': 1})
        self.assertTrue('children' not in ret[0])
        self.assertTrue('decorated_scientific_lineage' not in ret[0])
        self.assertTrue('decorated_children' not in ret[0])
        p = {'ref': self.parent, 'include_decorated_children': 1}
        ret = self.getImpl().get_all_data(self.getContext(), p)
        self.assertTrue('decorated_children' in ret[0])
        self.assertTrue('decorated_scientific_lineage' not in ret[0])

        ret = self.getImpl().get_all_data(self.getContext(), {'ref': self.root_taxon})
        self.assertEqual(ret[0]['parent'], None)

    def test_get_decorated_lineage(self):
        p = {'ref': self.taxon}
        ret = self.getImpl().get_decorated_scientific_lineage(self.getContext(), p)
        lineage = ret[0]['decorated_scientific_lineage']
        self.assertEqual(len(lineage), 8)

        self.assertEqual(lineage[0]['scientific_name'], 'cellular organisms')

    def test_get_children(self):
        ret = self.getImpl().get_children(self.getContext(), self.taxon)
        self.assertEqual(ret[0], [])

    def test_get_decorated_children(self):
        ret = self.getImpl().get_decorated_children(self.getContext(), {'ref': self.root_taxon})
        # tricky to test without loading specific test data- the number
        # of children can change (usually
        # increase, but objects could be deleted too)
        self.assertTrue(len(ret[0]['decorated_children']) >= 5)

    def test_get_genome_annotations(self):
        ret = self.getImpl().get_genome_annotations(self.getContext(), self.taxon)
        self.assertTrue(len(ret[0]) > 0)
        # this fails as the test taxon is referenced- so we can't do this.
        #    self.assertEqual(ret[0], ['7364/20/13', '7364/10/1', '6838/147/1',
        #    '5810/70/1', '6831/12/1','7695/21/1', '5729/70/1', '7990/93/1',
        #    '8020/81/1', '8020/39/1', '7824/35/1',
        #	'1837/570/3', '1374/676/1', '5441/70/1', '4758/9/1', '4435/71/1',
        #    '4237/79/1'])

    def test_get_scientific_lineage(self):
        ret = self.getImpl().get_scientific_lineage(self.getContext(), self.taxon)
        self.assertEqual(ret[0], [u'cellular organisms', u'Eukaryota',
                                  u'Rhodophyta', u'Bangiophyceae',
                                  u'Cyanidiales', u'Cyanidiaceae',
                                  u'Cyanidioschyzon',
                                  u'Cyanidioschyzon merolae'])

    def test_get_scientific_name(self):
        ret = self.getImpl().get_scientific_name(self.getContext(), self.taxon)
        self.assertEqual(ret[0], u'Cyanidioschyzon merolae strain 10D')

    def test_get_taxonomic_id(self):
        ret = self.getImpl().get_taxonomic_id(self.getContext(), self.taxon)
        self.assertEqual(ret[0], 280699)

    def xtest_get_kingdom(self):
        ret = self.getImpl().get_kingdom(self.getContext(), self.taxon)
        self.assertEqual(ret[0], u'cellular organisms')

    def test_get_domain(self):
        ret = self.getImpl().get_domain(self.getContext(), self.taxon)
        self.assertEqual(ret[0], u'Eukaryota')

    def test_get_genetic_code(self):
        ret = self.getImpl().get_genetic_code(self.getContext(), self.taxon)
        self.assertEqual(ret[0], 1)

    def test_get_aliases(self):
        ret = self.getImpl().get_aliases(self.getContext(), self.taxon)
        self.assertEqual(ret[0], [])

    def test_get_info(self):
        ret = self.getImpl().get_info(self.getContext(), self.taxon)
        ws_id, obj_id, version = self.wsClient.get_objects2({'objects': [{'ref': self.taxon}]})['data'][0]['path'][0].split('/')
        # data saved on ci and appdev have different save date
        del ret[0]['save_date']
        # 'object_checksum' includes the date the object is saved, this info on ci and appdev are different
        # needs to be compared particularly
        if 'ci' in self.wsURL:
            self.assertEqual(ret[0]['object_checksum'],  u'5f1b24082f447daccca0c8d2f1073fe4')
        elif 'appdev' in self.wsURL:
            self.assertEqual(ret[0]['object_checksum'], u'be965af99c26eb1d8af025f6cd58476b')
        del ret[0]['object_checksum']
        exp = {
            'type_string': u'KBaseGenomeAnnotations.Taxon-1.0',
            'workspace_id': int(ws_id),
            'object_reference': '/'.join([ws_id, obj_id]),
            'object_size': 455,
            'saved_by': u'kbasetest',
            'object_id': int(obj_id),
            'object_metadata': None,
            'object_name': u'280699_taxon',
            'version': 1,
            'workspace_name': u'ReferenceTaxons',
            'object_reference_versioned': '/'.join([ws_id, obj_id, version])
        }
        self.assertDictEqual(ret[0], exp)

    def test_get_history(self):
        ret = self.getImpl().get_history(self.getContext(), self.taxon)
        # kt = ret[0][0].pop('type_string')
        # print kt
        ws_id, obj_id, version = self.wsClient.get_objects2({'objects': [{'ref': self.taxon}]})['data'][0]['path'][0].split('/')
        # data saved on ci and appdev have different save date
        del ret[0][0]['save_date']
        # 'object_checksum' includes the date the object is saved, this info on ci and appdev are different
        # needs to be compared particularly
        if 'ci' in self.wsURL:
            self.assertEqual(ret[0][0]['object_checksum'],  u'5f1b24082f447daccca0c8d2f1073fe4')
        elif 'appdev' in self.wsURL:
            self.assertEqual(ret[0][0]['object_checksum'], u'be965af99c26eb1d8af025f6cd58476b')
        del ret[0][0]['object_checksum']
        expected = {'object_id': int(obj_id),
                    'object_metadata': None,
                    'object_name': u'280699_taxon',
                    'object_reference': '/'.join([ws_id, obj_id]),
                    'object_reference_versioned': '/'.join([ws_id, obj_id, version]),
                    'object_size': 455,
                    'saved_by': u'kbasetest',
                    'type_string': u'KBaseGenomeAnnotations.Taxon-1.0',
                    'version': 1,
                    'workspace_id': int(ws_id),
                    'workspace_name': u'ReferenceTaxons'}
        self.assertEqual(ret[0][0], expected)

    def test_get_provenance(self):
        ret = self.getImpl().get_provenance(self.getContext(), self.taxon)
        exp = {
            'description': u'taxon generated from NCBI taxonomy names and nodes files downloaded on 7/20/2015.',
            'script_name': u'make_taxons.py',
            'script_version': u'0.1'
        }
        self.assertEqual(ret[0], [exp])

    def test_get_id(self):
        ret = self.getImpl().get_id(self.getContext(), self.taxon)
        ret_ref_id = self.wsClient.get_objects2({'objects': [{'ref': self.taxon}]})['data'][0]['path'][0].split('/')[1]
        self.assertEqual(ret[0], int(ret_ref_id))

    def test_get_name(self):
        ret = self.getImpl().get_name(self.getContext(), self.taxon)
        self.assertEqual(ret[0], u'280699_taxon')

    def test_get_version(self):
        ret = self.getImpl().get_version(self.getContext(), self.taxon)
        self.assertEqual(ret[0], '1')
