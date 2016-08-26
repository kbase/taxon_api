/*
A KBase module: TaxonAPI
*/

module TaxonAPI {

/* A boolean. 0 = false, other = true. */
typedef int boolean;

typedef string ObjectReference;

/** @skip documentation */
typedef structure {
     int object_id;
     string object_name;
     string object_reference;
     string object_reference_versioned;
     string type_string;
     string save_date;
     int version;
     string saved_by;
     int workspace_id;
     string workspace_name;
     string object_checksum;
     int object_size;
     mapping<string,string> object_metadata;
}  ObjectInfo;

/** @skip documentation */
typedef list<ObjectInfo> ObjectHistory;

/** @skip documentation */
typedef structure {
     string resource_name;
     string resource_url;
     string resource_version;
     string resource_release_date;
     string data_url;
     string data_id;
     string description;
}  ExternalDataUnit;

/** @skip documentation */
typedef structure {
     string time;
     string service_name;
     string service_version;
     string service_method;
     list<string> method_parameters;
     string script_name;
     string script_version;
     string script_command_line;
     list<string> input_object_references;
     list<string> validated_object_references;
     list<string> intermediate_input_ids;
     list<string> intermediate_output_ids;
     list<ExternalDataUnit> external_data;
     string description;
}  ObjectProvenanceAction;

/** @skip documentation */
typedef list<ObjectProvenanceAction> ObjectProvenance;

    /**
     * Retrieve parent Taxon.
     *
     * @return Reference to parent Taxon.
     */
     funcdef get_parent( ObjectReference ref)  returns (ObjectReference) authentication required;

    /**
     * Retrieve children Taxon.
     *
     * @return List of references to child Taxons.
     */
     funcdef get_children( ObjectReference ref)  returns (list<ObjectReference>) authentication required;

    /**
     funcdef GenomeAnnotation(s) that refer to this Taxon.
     * If this is accessing a KBaseGenomes.Genome object, it will
     * return an empty list (this information is not available).
     *
     * @return List of references to GenomeAnnotation objects.
     */
     funcdef get_genome_annotations( ObjectReference ref)  returns (list<ObjectReference>) authentication required;

    /**
     * Retrieve the scientific lineage.
     *
     * @return Strings for each 'unit' of the lineage, ordered in
     *   the usual way from Domain to Kingdom to Phylum, etc.
     *
     */
     funcdef get_scientific_lineage( ObjectReference ref)  returns (list<string>) authentication required;

    /**
     * Retrieve the scientific name.
     *
     * @return The scientific name, e.g., "Escherichia Coli K12 str. MG1655"
     */
     funcdef get_scientific_name( ObjectReference ref)  returns (string) authentication required;

    /**
     * Retrieve the NCBI taxonomic ID of this Taxon.
     * For type KBaseGenomes.Genome, the ``source_id`` will be returned.
     *
     * @return Integer taxonomic ID.
     */
     funcdef get_taxonomic_id( ObjectReference ref)  returns (int) authentication required;

    /**
     * Retrieve the kingdom.
     *
     */
     funcdef get_kingdom( ObjectReference ref)  returns (string) authentication required;

    /**
     * Retrieve the domain.
     *
     */
     funcdef get_domain( ObjectReference ref)  returns (string) authentication required;

    /**
     * Retrieve the genetic code.
     *
     */
     funcdef get_genetic_code( ObjectReference ref)  returns (int) authentication required;

    /**
     * Retrieve the aliases.
     *
     */
     funcdef get_aliases( ObjectReference ref)  returns (list<string>) authentication required;

    /**
     * Retrieve object info.
     * @skip documentation
     */
     funcdef get_info( ObjectReference ref)  returns (ObjectInfo) authentication required;

    /**
     * Retrieve object history.
     * @skip documentation
     */
     funcdef get_history( ObjectReference ref)  returns (ObjectHistory) authentication required;

    /**
     * Retrieve object provenance.
     * @skip documentation
     */
     funcdef get_provenance( ObjectReference ref)  returns (ObjectProvenance) authentication required;

    /**
     * Retrieve object identifier.
     * @skip documentation
     */
     funcdef get_id( ObjectReference ref)  returns (int) authentication required;

    /**
     * Retrieve object name.
     * @skip documentation
     */
     funcdef get_name( ObjectReference ref)  returns (string) authentication required;

    /**
     * Retrieve object version.
     * @skip documentation
     */
     funcdef get_version( ObjectReference ref)  returns (string) authentication required;


     typedef structure {
        ObjectReference ref;
        boolean include_decorated_scientific_lineage;
        boolean include_decorated_children;
     } GetAllDataParams;


     typedef structure {
        ObjectReference ref;
        string scientific_name;
     } TaxonInfo;

     typedef structure {
        ObjectReference parent;

        list<ObjectReference> children;
        list<TaxonInfo> decorated_children;

        list<string> scientific_lineage;
        list<TaxonInfo> decorated_scientific_lineage;

        string scientific_name;
        int taxonomic_id;
        string kingdom;
        string domain;
        int genetic_code;

        list <string> aliases;

        ObjectInfo obj_info;
     } TaxonData;

     funcdef get_all_data( GetAllDataParams params )
                    returns (TaxonData d) authentication required;

    typedef structure {
        ObjectReference ref;
     } GetDecoratedScientificLineageParams;

     /* list starts at the root, and goes on down to this */
     typedef structure {
        list <TaxonInfo> decorated_scientific_lineage;
     } DecoratedScientificLineage;

     funcdef get_decorated_scientific_lineage(GetDecoratedScientificLineageParams params)
                    returns (DecoratedScientificLineage) authentication required;

    typedef structure {
        ObjectReference ref;
     } GetDecoratedChildrenParams;

     typedef structure {
        list <TaxonInfo> decorated_children;
     } DecoratedChildren;

     funcdef get_decorated_children(GetDecoratedChildrenParams params)
                    returns (DecoratedChildren) authentication required;

};
