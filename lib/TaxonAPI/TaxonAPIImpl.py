# -*- coding: utf-8 -*-
#BEGIN_HEADER
from biokbase.workspace.client import Workspace as workspaceService
import doekbase.data_api.taxonomy.taxon.api
from doekbase.data_api import cache
import traceback
import logging
#END_HEADER


class TaxonAPI:
    '''
    Module Name:
    TaxonAPI

    Module Description:
    A KBase module: TaxonAPI
    '''

    ######## WARNING FOR GEVENT USERS #######
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    #########################################
    VERSION = "0.0.2"
    GIT_URL = "git@github.com:kbase/taxon_api"
    GIT_COMMIT_HASH = "30e969aff0bd259f710e14b4468a2a73367f07cf"
    
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
        """
        Retrieve parent Taxon.
        @return Reference to parent Taxon.
        :param ref: instance of type "ObjectReference"
        :returns: instance of type "ObjectReference"
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN get_parent
        taxon_api = doekbase.data_api.taxonomy.taxon.api.TaxonAPI(self.services, ctx['token'], ref)
        try:
            returnVal=taxon_api.get_parent(ref_only=True)
        except:
            returnVal=''
        #END get_parent

        # At some point might do deeper type checking...
        if not isinstance(returnVal, basestring):
            raise ValueError('Method get_parent return value ' +
                             'returnVal is not type basestring as required.')
        # return the results
        return [returnVal]

    def get_children(self, ctx, ref):
        """
        Retrieve children Taxon.
        @return List of references to child Taxons.
        :param ref: instance of type "ObjectReference"
        :returns: instance of list of type "ObjectReference"
        """
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
        """
        funcdef GenomeAnnotation(s) that refer to this Taxon.
         If this is accessing a KBaseGenomes.Genome object, it will
         return an empty list (this information is not available).
         @return List of references to GenomeAnnotation objects.
        :param ref: instance of type "ObjectReference"
        :returns: instance of list of type "ObjectReference"
        """
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
        """
        Retrieve the scientific lineage.
        @return Strings for each 'unit' of the lineage, ordered in
          the usual way from Domain to Kingdom to Phylum, etc.
        :param ref: instance of type "ObjectReference"
        :returns: instance of list of String
        """
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
        """
        Retrieve the scientific name.
        @return The scientific name, e.g., "Escherichia Coli K12 str. MG1655"
        :param ref: instance of type "ObjectReference"
        :returns: instance of String
        """
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
        """
        Retrieve the NCBI taxonomic ID of this Taxon.
        For type KBaseGenomes.Genome, the ``source_id`` will be returned.
        @return Integer taxonomic ID.
        :param ref: instance of type "ObjectReference"
        :returns: instance of Long
        """
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
        """
        Retrieve the kingdom.
        :param ref: instance of type "ObjectReference"
        :returns: instance of String
        """
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
        """
        Retrieve the domain.
        :param ref: instance of type "ObjectReference"
        :returns: instance of String
        """
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
        """
        Retrieve the genetic code.
        :param ref: instance of type "ObjectReference"
        :returns: instance of Long
        """
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
        """
        Retrieve the aliases.
        :param ref: instance of type "ObjectReference"
        :returns: instance of list of String
        """
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
        """
        Retrieve object info.
        @skip documentation
        :param ref: instance of type "ObjectReference"
        :returns: instance of type "ObjectInfo" (* @skip documentation) ->
           structure: parameter "object_id" of Long, parameter "object_name"
           of String, parameter "object_reference" of String, parameter
           "object_reference_versioned" of String, parameter "type_string" of
           String, parameter "save_date" of String, parameter "version" of
           Long, parameter "saved_by" of String, parameter "workspace_id" of
           Long, parameter "workspace_name" of String, parameter
           "object_checksum" of String, parameter "object_size" of Long,
           parameter "object_metadata" of mapping from String to String
        """
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
        """
        Retrieve object history.
        @skip documentation
        :param ref: instance of type "ObjectReference"
        :returns: instance of type "ObjectHistory" (* @skip documentation) ->
           list of type "ObjectInfo" (* @skip documentation) -> structure:
           parameter "object_id" of Long, parameter "object_name" of String,
           parameter "object_reference" of String, parameter
           "object_reference_versioned" of String, parameter "type_string" of
           String, parameter "save_date" of String, parameter "version" of
           Long, parameter "saved_by" of String, parameter "workspace_id" of
           Long, parameter "workspace_name" of String, parameter
           "object_checksum" of String, parameter "object_size" of Long,
           parameter "object_metadata" of mapping from String to String
        """
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
        """
        Retrieve object provenance.
        @skip documentation
        :param ref: instance of type "ObjectReference"
        :returns: instance of type "ObjectProvenance" (* @skip documentation)
           -> list of type "ObjectProvenanceAction" (* @skip documentation)
           -> structure: parameter "time" of String, parameter "service_name"
           of String, parameter "service_version" of String, parameter
           "service_method" of String, parameter "method_parameters" of list
           of String, parameter "script_name" of String, parameter
           "script_version" of String, parameter "script_command_line" of
           String, parameter "input_object_references" of list of String,
           parameter "validated_object_references" of list of String,
           parameter "intermediate_input_ids" of list of String, parameter
           "intermediate_output_ids" of list of String, parameter
           "external_data" of list of type "ExternalDataUnit" (* @skip
           documentation) -> structure: parameter "resource_name" of String,
           parameter "resource_url" of String, parameter "resource_version"
           of String, parameter "resource_release_date" of String, parameter
           "data_url" of String, parameter "data_id" of String, parameter
           "description" of String, parameter "description" of String
        """
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
        """
        Retrieve object identifier.
        @skip documentation
        :param ref: instance of type "ObjectReference"
        :returns: instance of Long
        """
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
        """
        Retrieve object name.
        @skip documentation
        :param ref: instance of type "ObjectReference"
        :returns: instance of String
        """
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
        """
        Retrieve object version.
        @skip documentation
        :param ref: instance of type "ObjectReference"
        :returns: instance of String
        """
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

    def get_all_data(self, ctx, params):
        """
        :param params: instance of type "GetAllDataParams" -> structure:
           parameter "ref" of type "ObjectReference", parameter
           "include_decorated_scientific_lineage" of type "boolean" (A
           boolean. 0 = false, other = true.), parameter
           "include_decorated_children" of type "boolean" (A boolean. 0 =
           false, other = true.)
        :returns: instance of type "TaxonData" -> structure: parameter
           "parent" of type "ObjectReference", parameter "children" of list
           of type "ObjectReference", parameter "decorated_children" of list
           of type "TaxonInfo" -> structure: parameter "ref" of type
           "ObjectReference", parameter "scientific_name" of String,
           parameter "scientific_lineage" of list of String, parameter
           "decorated_scientific_lineage" of list of type "TaxonInfo" ->
           structure: parameter "ref" of type "ObjectReference", parameter
           "scientific_name" of String, parameter "scientific_name" of
           String, parameter "taxonomic_id" of Long, parameter "kingdom" of
           String, parameter "domain" of String, parameter "genetic_code" of
           Long, parameter "aliases" of list of String, parameter "obj_info"
           of type "ObjectInfo" (* @skip documentation) -> structure:
           parameter "object_id" of Long, parameter "object_name" of String,
           parameter "object_reference" of String, parameter
           "object_reference_versioned" of String, parameter "type_string" of
           String, parameter "save_date" of String, parameter "version" of
           Long, parameter "saved_by" of String, parameter "workspace_id" of
           Long, parameter "workspace_name" of String, parameter
           "object_checksum" of String, parameter "object_size" of Long,
           parameter "object_metadata" of mapping from String to String
        """
        # ctx is the context object
        # return variables are: d
        #BEGIN get_all_data
        d = {}

        taxon_api = doekbase.data_api.taxonomy.taxon.api.TaxonAPI(self.services, ctx['token'], params['ref'])

        try:
            d['parent']=taxon_api.get_parent(ref_only=True)
        except AttributeError:
            print('Error getting parent for '+params['ref']+':\n'+ str(traceback.format_exc()))
            d['parent']=None

        d['children']=taxon_api.get_children(ref_only=True)
        d['scientific_lineage']=taxon_api.get_scientific_lineage()
        d['scientific_name']=taxon_api.get_scientific_name()
        d['taxonomic_id']=taxon_api.get_taxonomic_id()
        try:
            d['kingdom']=taxon_api.get_kingdom()
            # throws error if not found, so catch and log it
        except AttributeError as e:
            print('Error getting kingdom for '+params['ref']+':\n'+ str(traceback.format_exc()))
            d['kingdom']=None

        d['domain']=taxon_api.get_domain()
        d['genetic_code']=taxon_api.get_genetic_code()
        d['aliases']=taxon_api.get_aliases()
        d['info']=taxon_api.get_info()

        if 'include_decorated_scientific_lineage' in params and params['include_decorated_scientific_lineage']==1:
            l = self.get_decorated_scientific_lineage(ctx, {'ref':params['ref']})[0]
            d['decorated_scientific_lineage'] = l['decorated_scientific_lineage']

        if 'include_decorated_children' in params and params['include_decorated_children']==1:
            l = self.get_decorated_children(ctx, {'ref':params['ref']})[0]
            d['decorated_children'] = l['decorated_children']

        #END get_all_data

        # At some point might do deeper type checking...
        if not isinstance(d, dict):
            raise ValueError('Method get_all_data return value ' +
                             'd is not type dict as required.')
        # return the results
        return [d]

    def get_decorated_scientific_lineage(self, ctx, params):
        """
        :param params: instance of type "GetDecoratedScientificLineageParams"
           -> structure: parameter "ref" of type "ObjectReference"
        :returns: instance of type "DecoratedScientificLineage" (list starts
           at the root, and goes on down to this) -> structure: parameter
           "decorated_scientific_lineage" of list of type "TaxonInfo" ->
           structure: parameter "ref" of type "ObjectReference", parameter
           "scientific_name" of String
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN get_decorated_scientific_lineage

        lineageList = [];

        thisTaxon = doekbase.data_api.taxonomy.taxon.api.TaxonAPI(self.services, ctx['token'], params['ref'])

        while True:
            parent_data = None
            try:
                # note: doesn't look like there is a way to get a reference of a Taxon directly (without
                # constructing it from object_info), so first get reference, then instantiate another API object 
                parent_ref=thisTaxon.get_parent(ref_only=True)
                if parent_ref is not None:
                    parent = doekbase.data_api.taxonomy.taxon.api.TaxonAPI(self.services, ctx['token'], parent_ref)
                    scientific_name = parent.get_scientific_name()
                    if scientific_name != 'root':
                        parent_data = {
                            'ref': parent_ref,
                            'scientific_name':scientific_name
                        }
                        thisTaxon = parent
            
            except AttributeError:
                # case where parent is not found
                pass

            if parent_data is not None:
                lineageList.append(parent_data)
            else:
                break

        lineageList.reverse() # reverse list to match scientific_lineage style
        returnVal = { 'decorated_scientific_lineage': lineageList }

        #END get_decorated_scientific_lineage

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method get_decorated_scientific_lineage return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]

    def get_decorated_children(self, ctx, params):
        """
        :param params: instance of type "GetDecoratedChildrenParams" ->
           structure: parameter "ref" of type "ObjectReference"
        :returns: instance of type "DecoratedChildren" -> structure:
           parameter "decorated_children" of list of type "TaxonInfo" ->
           structure: parameter "ref" of type "ObjectReference", parameter
           "scientific_name" of String
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN get_decorated_children

        taxon_api = doekbase.data_api.taxonomy.taxon.api.TaxonAPI(self.services, ctx['token'], params['ref'])

        children_refs=taxon_api.get_children(ref_only=True)

        decorated_children = []
        for child_ref in children_refs:
            child = doekbase.data_api.taxonomy.taxon.api.TaxonAPI(self.services, ctx['token'], child_ref)
            decorated_children.append({
                    'ref':child_ref,
                    'scientific_name':child.get_scientific_name()
                })

        returnVal = { 'decorated_children': decorated_children }
        #END get_decorated_children

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method get_decorated_children return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]

    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK", 'message': "", 'version': self.VERSION, 
                     'git_url': self.GIT_URL, 'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
