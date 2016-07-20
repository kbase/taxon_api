#BEGIN_HEADER
from biokbase.workspace.client import Workspace as workspaceService
import doekbase.data_api.taxonomy.taxon.api
from doekbase.data_api import cache
import logging
#END_HEADER


class TaxonAPI:
    '''
    Module Name:
    TaxonAPI

    Module Description:
    A KBase module: test_taxon_api
    '''

    ######## WARNING FOR GEVENT USERS #######
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    #########################################
    VERSION = "0.0.1"
    GIT_URL = "https://github.com/scanon/testtaxonapi"
    GIT_COMMIT_HASH = "a76b28a7e461132eb5227a7465dc8c37fb01b839"
    
    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.workspaceURL = config['workspace-url']
        self.shockURL = config['shock-url']
        self.logger = logging.getLogger()
        log_handler = logging.StreamHandler()
        log_handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s"))
        self.logger.addHandler(log_handler)


        self.services = {
                "workspace_service_url": self.workspaceURL,
                "shock_service_url": self.shockURL,
            }
        try:
            cache_dir = config['cache_dir']
        except:
            cache_dir = None
        try:
            redis_host = config['redis_host']
            redis_port = config['redis_port']
        except:
            redis_host = None
            redis_port = None
        if redis_host is not None and redis_port is not None:
            self.logger.info("Activating REDIS at host:{} port:{}".format(redis_host, redis_port))
            cache.ObjectCache.cache_class = cache.RedisCache
            cache.ObjectCache.cache_params = {'redis_host': redis_host, 'redis_port': redis_port}
        elif cache_dir is not None:
            self.logger.info("Activating File")
            cache.ObjectCache.cache_class = cache.DBMCache
            cache.ObjectCache.cache_params = {'path':cache_dir,'name':'data_api'}
        else:
            self.logger.info("Not activating REDIS")

        #END_CONSTRUCTOR
        pass
    

    def get_parent(self, ctx, ref):
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN get_parent
        taxon_api = doekbase.data_api.taxonomy.taxon.api.TaxonAPI(self.services, ctx['token'], ref)
        returnVal=taxon_api.get_parent(ref_only=True)
        #END get_parent

        # At some point might do deeper type checking...
        if not isinstance(returnVal, basestring):
            raise ValueError('Method get_parent return value ' +
                             'returnVal is not type basestring as required.')
        # return the results
        return [returnVal]

    def get_children(self, ctx, ref):
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN get_children
        taxon_api = doekbase.data_api.taxonomy.taxon.api.TaxonAPI(self.services, ctx['token'], ref)
        returnVal=taxon_api.get_children(ref_only=True)
        #END get_children

        # At some point might do deeper type checking...
        if not isinstance(returnVal, list):
            raise ValueError('Method get_children return value ' +
                             'returnVal is not type list as required.')
        # return the results
        return [returnVal]

    def get_genome_annotations(self, ctx, ref):
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN get_genome_annotations
        taxon_api = doekbase.data_api.taxonomy.taxon.api.TaxonAPI(self.services, ctx['token'], ref)
        returnVal=taxon_api.get_genome_annotations(ref_only=True)
        #END get_genome_annotations

        # At some point might do deeper type checking...
        if not isinstance(returnVal, list):
            raise ValueError('Method get_genome_annotations return value ' +
                             'returnVal is not type list as required.')
        # return the results
        return [returnVal]

    def get_scientific_lineage(self, ctx, ref):
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN get_scientific_lineage
        taxon_api = doekbase.data_api.taxonomy.taxon.api.TaxonAPI(self.services, ctx['token'], ref)
        returnVal=taxon_api.get_scientific_lineage()
        #END get_scientific_lineage

        # At some point might do deeper type checking...
        if not isinstance(returnVal, list):
            raise ValueError('Method get_scientific_lineage return value ' +
                             'returnVal is not type list as required.')
        # return the results
        return [returnVal]

    def get_scientific_name(self, ctx, ref):
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN get_scientific_name
        taxon_api = doekbase.data_api.taxonomy.taxon.api.TaxonAPI(self.services, ctx['token'], ref)
        returnVal=taxon_api.get_scientific_name()
        #END get_scientific_name

        # At some point might do deeper type checking...
        if not isinstance(returnVal, basestring):
            raise ValueError('Method get_scientific_name return value ' +
                             'returnVal is not type basestring as required.')
        # return the results
        return [returnVal]

    def get_taxonomic_id(self, ctx, ref):
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN get_taxonomic_id
        taxon_api = doekbase.data_api.taxonomy.taxon.api.TaxonAPI(self.services, ctx['token'], ref)
        returnVal=taxon_api.get_taxonomic_id()
        #END get_taxonomic_id

        # At some point might do deeper type checking...
        if not isinstance(returnVal, int):
            raise ValueError('Method get_taxonomic_id return value ' +
                             'returnVal is not type int as required.')
        # return the results
        return [returnVal]

    def get_kingdom(self, ctx, ref):
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN get_kingdom
        taxon_api = doekbase.data_api.taxonomy.taxon.api.TaxonAPI(self.services, ctx['token'], ref)
        returnVal=taxon_api.get_kingdom()
        #END get_kingdom

        # At some point might do deeper type checking...
        if not isinstance(returnVal, basestring):
            raise ValueError('Method get_kingdom return value ' +
                             'returnVal is not type basestring as required.')
        # return the results
        return [returnVal]

    def get_domain(self, ctx, ref):
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN get_domain
        taxon_api = doekbase.data_api.taxonomy.taxon.api.TaxonAPI(self.services, ctx['token'], ref)
        returnVal=taxon_api.get_domain()
        #END get_domain

        # At some point might do deeper type checking...
        if not isinstance(returnVal, basestring):
            raise ValueError('Method get_domain return value ' +
                             'returnVal is not type basestring as required.')
        # return the results
        return [returnVal]

    def get_genetic_code(self, ctx, ref):
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN get_genetic_code
        taxon_api = doekbase.data_api.taxonomy.taxon.api.TaxonAPI(self.services, ctx['token'], ref)
        returnVal=taxon_api.get_genetic_code()
        #END get_genetic_code

        # At some point might do deeper type checking...
        if not isinstance(returnVal, int):
            raise ValueError('Method get_genetic_code return value ' +
                             'returnVal is not type int as required.')
        # return the results
        return [returnVal]

    def get_aliases(self, ctx, ref):
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN get_aliases
        taxon_api = doekbase.data_api.taxonomy.taxon.api.TaxonAPI(self.services, ctx['token'], ref)
        returnVal=taxon_api.get_aliases()
        #END get_aliases

        # At some point might do deeper type checking...
        if not isinstance(returnVal, list):
            raise ValueError('Method get_aliases return value ' +
                             'returnVal is not type list as required.')
        # return the results
        return [returnVal]

    def get_info(self, ctx, ref):
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN get_info
        taxon_api = doekbase.data_api.taxonomy.taxon.api.TaxonAPI(self.services, ctx['token'], ref)
        returnVal=taxon_api.get_info()
        #END get_info

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method get_info return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]

    def get_history(self, ctx, ref):
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN get_history
        taxon_api = doekbase.data_api.taxonomy.taxon.api.TaxonAPI(self.services, ctx['token'], ref)
        returnVal=taxon_api.get_history()
        #END get_history

        # At some point might do deeper type checking...
        if not isinstance(returnVal, list):
            raise ValueError('Method get_history return value ' +
                             'returnVal is not type list as required.')
        # return the results
        return [returnVal]

    def get_provenance(self, ctx, ref):
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN get_provenance
        taxon_api = doekbase.data_api.taxonomy.taxon.api.TaxonAPI(self.services, ctx['token'], ref)
        returnVal=taxon_api.get_provenance()
        #END get_provenance

        # At some point might do deeper type checking...
        if not isinstance(returnVal, list):
            raise ValueError('Method get_provenance return value ' +
                             'returnVal is not type list as required.')
        # return the results
        return [returnVal]

    def get_id(self, ctx, ref):
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN get_id
        taxon_api = doekbase.data_api.taxonomy.taxon.api.TaxonAPI(self.services, ctx['token'], ref)
        returnVal=taxon_api.get_id()
        #END get_id

        # At some point might do deeper type checking...
        if not isinstance(returnVal, int):
            raise ValueError('Method get_id return value ' +
                             'returnVal is not type int as required.')
        # return the results
        return [returnVal]

    def get_name(self, ctx, ref):
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN get_name
        taxon_api = doekbase.data_api.taxonomy.taxon.api.TaxonAPI(self.services, ctx['token'], ref)
        returnVal=taxon_api.get_name()
        #END get_name

        # At some point might do deeper type checking...
        if not isinstance(returnVal, basestring):
            raise ValueError('Method get_name return value ' +
                             'returnVal is not type basestring as required.')
        # return the results
        return [returnVal]

    def get_version(self, ctx, ref):
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN get_version
        taxon_api = doekbase.data_api.taxonomy.taxon.api.TaxonAPI(self.services, ctx['token'], ref)
        returnVal=taxon_api.get_version()
        #END get_version

        # At some point might do deeper type checking...
        if not isinstance(returnVal, basestring):
            raise ValueError('Method get_version return value ' +
                             'returnVal is not type basestring as required.')
        # return the results
        return [returnVal]

    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK", 'message': "", 'version': self.VERSION, 
                     'git_url': self.GIT_URL, 'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
