# -*- coding: utf-8 -*-
#BEGIN_HEADER
from Workspace.WorkspaceClient import Workspace
import logging
import functools
# from datetime import datetime
#END_HEADER


class TaxonAPI:
    '''
    Module Name:
    TaxonAPI

    Module Description:
    A KBase module: TaxonAPI
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "1.0.4"
    GIT_URL = "https://github.com/kbase/taxon_api"
    GIT_COMMIT_HASH = "13d69191b532f486dbedec09a6ef8ce43f74210b"

    #BEGIN_CLASS_HEADER
    _GENOME_TYPES = ['KBaseGenomes.Genome',
                     'KBaseGenomeAnnotations.GenomeAnnotation']
    _TAXON_TYPES = ['KBaseGenomeAnnotations.Taxon']

    @functools.lru_cache(maxsize=1024)
    def get_object(self, ref, no_data=False):
        res = self.ws.get_objects2({
            'objects': [{'ref': ref}],
            'no_data': 1 if no_data else 0
        })['data'][0]
        return res

    def get_data(self, ref):
        obj = self.get_object(ref)
        return obj['data']

    @functools.lru_cache(maxsize=1024)
    def translate_to_MD5_types(self, ktype):
        return self.ws.translate_to_MD5_types([ktype]).values()[0]

    def get_referrers(self, ref):
        referrers = self.ws.list_referencing_objects(
            [{"ref": ref}])[0]
        object_refs_by_type = dict()
        tlist = []
        for x in referrers:
            tlist.append(x[2])
        typemap = self.ws.translate_to_MD5_types(tlist)
        for x in referrers:
            typestring = typemap[x[2]]
            if typestring not in object_refs_by_type:
                object_refs_by_type[typestring] = list()
            upa = '%d/%d/%d' % (x[6], x[0], x[4])
            object_refs_by_type[typestring].append(upa)
        return object_refs_by_type

    def get_reffers_type(self, ref, types):
        referrers = self.get_referrers(ref)
        children = list()
        for object_type in referrers:
            if object_type.split('-')[0] in types:
                children.extend(referrers[object_type])

        return children

    def make_hash(self, i):
        omd = i[10]
        if i[10] == {}:
            omd = None

        return {
            'type_string': i[2],
            'workspace_id': i[6],
            'object_checksum': i[8],
            'object_reference': '%d/%d' % (i[6], i[0]),
            'object_size': i[9],
            'saved_by': i[5],
            'object_id': i[0],
            'save_date': i[3],
            'object_metadata': omd,
            'object_name': i[1],
            'version': i[4],
            'workspace_name': i[7],
            'object_reference_versioned': '%d/%d/%d' % (i[6], i[0], i[4])
        }
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.workspaceURL = config['workspace-url']
        self.ws = Workspace(self.workspaceURL)
        self.shockURL = config['shock-url']
        self.logger = logging.getLogger()
        log_handler = logging.StreamHandler()
        log_handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s"))
        self.logger.addHandler(log_handler)

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
        data = self.get_data(ref)
        returnVal = data.get('parent_taxon_ref', '')
        #END get_parent

        # At some point might do deeper type checking...
        if not isinstance(returnVal, str):
            raise ValueError('Method get_parent return value ' +
                             'returnVal is not type str as required.')
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
        returnVal = self.get_reffers_type(ref, self._TAXON_TYPES)
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
        returnVal = self.get_reffers_type(ref, self._GENOME_TYPES)
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
        o = self.get_data(ref)
        returnVal = [x.strip() for x in o['scientific_lineage'].split(";")]
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
        obj = self.get_data(ref)
        returnVal = obj['scientific_name']
        #END get_scientific_name

        # At some point might do deeper type checking...
        if not isinstance(returnVal, str):
            raise ValueError('Method get_scientific_name return value ' +
                             'returnVal is not type str as required.')
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
        obj = self.get_data(ref)
        returnVal = obj['taxonomy_id']
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
        obj = self.get_data(ref)
        returnVal = obj['kingdom']
        #END get_kingdom

        # At some point might do deeper type checking...
        if not isinstance(returnVal, str):
            raise ValueError('Method get_kingdom return value ' +
                             'returnVal is not type str as required.')
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
        obj = self.get_data(ref)
        returnVal = obj['domain']
        #END get_domain

        # At some point might do deeper type checking...
        if not isinstance(returnVal, str):
            raise ValueError('Method get_domain return value ' +
                             'returnVal is not type str as required.')
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
        obj = self.get_data(ref)
        returnVal = obj['genetic_code']
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
        obj = self.get_data(ref)
        returnVal = obj.get('aliases', [])
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
        i = self.get_object(ref, no_data=True)['info']
        returnVal = self.make_hash(i)
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
        # returnVal = self.ws.get_object_history({'ref': ref})
        returnVal = []
        for i in self.ws.get_object_history({'ref': ref}):
            returnVal.append(self.make_hash(i))
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
        prov = self.ws.get_object_provenance([{"ref": ref}])[0]['provenance']
        returnVal = []
        copy_keys = {"time": "time",
                     "service": "service_name",
                     "service_ver": "service_version",
                     "method": "service_method",
                     "method_params": "method_parameters",
                     "script": "script_name",
                     "script_ver": "script_version",
                     "script_command_line": "script_command_line",
                     "input_ws_objects": "input_object_references",
                     "resolved_ws_objects": "validated_object_references",
                     "intermediate_incoming": "intermediate_input_ids",
                     "intermediate_outgoing": "intermediate_output_ids",
                     "external_data": "external_data",
                     "description": "description"
                     }

        for object_provenance in prov:
            action = dict()

            for k in copy_keys:
                if k in object_provenance:
                    if isinstance(object_provenance[k], list) and len(object_provenance[k]) == 0:
                        continue

                    action[copy_keys[k]] = object_provenance[k]

            returnVal.append(action)
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
        pieces = ref.split('/')
        if len(pieces) != 2 and len(pieces) != 3:
            raise ValueError(f'Invalid workspace reference: {ref}')
        returnVal = int(pieces[1])
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
        returnVal = self.get_object(ref, no_data=True)['info'][1]
        #END get_name

        # At some point might do deeper type checking...
        if not isinstance(returnVal, str):
            raise ValueError('Method get_name return value ' +
                             'returnVal is not type str as required.')
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
        pieces = ref.split('/')
        if len(pieces) == 2:
            returnVal = str(self.get_object(ref)['info'][4], no_data=True)
        elif len(pieces) == 3:
            returnVal = pieces[2]
        else:
            raise ValueError(f'Invalid workspace reference: {ref}')
        #END get_version

        # At some point might do deeper type checking...
        if not isinstance(returnVal, str):
            raise ValueError('Method get_version return value ' +
                             'returnVal is not type str as required.')
        # return the results
        return [returnVal]

    def get_all_data(self, ctx, params):
        """
        :param params: instance of type "GetAllDataParams" -> structure:
           parameter "ref" of type "ObjectReference", parameter
           "include_decorated_scientific_lineage" of type "boolean" (A
           boolean. 0 = false, other = true.), parameter
           "include_decorated_children" of type "boolean" (A boolean. 0 =
           false, other = true.), parameter "exclude_children" of type
           "boolean" (A boolean. 0 = false, other = true.)
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
        ref = params['ref']

        obj = self.get_object(ref)
        data = obj['data']

        try:
            d['parent'] = data['parent_taxon_ref']
        except KeyError:
            print('Error getting parent for ' + ref)
            # +':\n'+ str(traceback.format_exc()))
            d['parent'] = None

        if 'exclude_children' in params and params['exclude_children'] == 1:
            pass
        else:
            d['children'] = self.get_reffers_type(ref, self._TAXON_TYPES)

        d['scientific_lineage'] = data['scientific_lineage']
        d['scientific_name'] = data['scientific_name']
        d['taxonomic_id'] = data['taxonomy_id']
        try:
            d['kingdom'] = data['kingdom']
            # throws error if not found, so catch and log it
        except KeyError:
            print('Error getting kingdom for ' + ref)
            # +':\n'+ str(traceback.format_exc()))
            d['kingdom'] = None

        d['domain'] = data['domain']
        d['genetic_code'] = data['genetic_code']
        d['aliases'] = None
        if 'aliases' in data:
            d['aliases'] = data['aliases']
        d['info'] = self.make_hash(obj['info'])

        key = 'include_decorated_scientific_lineage'
        if key in params and params[key] == 1:
            l = self.get_decorated_scientific_lineage(ctx, {'ref': ref})[0]
            d['decorated_scientific_lineage'] = l['decorated_scientific_lineage']

        key = 'include_decorated_children'
        if key in params and params[key] == 1:
            l = self.get_decorated_children(ctx, {'ref': ref})[0]
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

        lineageList = []
        ref = params['ref']

        while True:
            parent_data = None
            try:
                # note: doesn't look like there is a way to get a reference
                # of a Taxon directly (without constructing it from
                # object_info), so first get reference, then instantiate
                # another API object
                parent_ref = self.get_data(ref)['parent_taxon_ref']
                if parent_ref is not None:
                    data = self.get_data(ref)
                    scientific_name = data['scientific_name']
                    if scientific_name != 'root':
                        parent_data = {
                            'ref': parent_ref,
                            'scientific_name': scientific_name
                        }
                        ref = parent_ref

            except KeyError:
                # case where parent is not found
                pass

            if parent_data is not None:
                lineageList.append(parent_data)
            else:
                break

        lineageList.reverse()  # reverse list to match scientific_lineage style
        returnVal = {'decorated_scientific_lineage': lineageList[:-1]}

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
        ref = params['ref']
        children_refs = self.get_reffers_type(ref, self._TAXON_TYPES)

        decorated_children = []
        for child_ref in children_refs:
            decorated_children.append({
                'ref': child_ref,
                'scientific_name': self.get_data(child_ref)['scientific_name']
            })

        returnVal = {'decorated_children': decorated_children}
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
