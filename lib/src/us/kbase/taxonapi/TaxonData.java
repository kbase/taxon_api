
package us.kbase.taxonapi;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import javax.annotation.Generated;
import com.fasterxml.jackson.annotation.JsonAnyGetter;
import com.fasterxml.jackson.annotation.JsonAnySetter;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


/**
 * <p>Original spec-file type: TaxonData</p>
 * 
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "parent",
    "children",
    "scientific_lineage",
    "scientific_name",
    "taxonomic_id",
    "kingdom",
    "domain",
    "genetic_code",
    "aliases",
    "obj_info"
})
public class TaxonData {

    @JsonProperty("parent")
    private java.lang.String parent;
    @JsonProperty("children")
    private List<String> children;
    @JsonProperty("scientific_lineage")
    private List<String> scientificLineage;
    @JsonProperty("scientific_name")
    private java.lang.String scientificName;
    @JsonProperty("taxonomic_id")
    private Long taxonomicId;
    @JsonProperty("kingdom")
    private java.lang.String kingdom;
    @JsonProperty("domain")
    private java.lang.String domain;
    @JsonProperty("genetic_code")
    private Long geneticCode;
    @JsonProperty("aliases")
    private List<String> aliases;
    /**
     * <p>Original spec-file type: ObjectInfo</p>
     * <pre>
     * * @skip documentation
     * </pre>
     * 
     */
    @JsonProperty("obj_info")
    private ObjectInfo objInfo;
    private Map<java.lang.String, Object> additionalProperties = new HashMap<java.lang.String, Object>();

    @JsonProperty("parent")
    public java.lang.String getParent() {
        return parent;
    }

    @JsonProperty("parent")
    public void setParent(java.lang.String parent) {
        this.parent = parent;
    }

    public TaxonData withParent(java.lang.String parent) {
        this.parent = parent;
        return this;
    }

    @JsonProperty("children")
    public List<String> getChildren() {
        return children;
    }

    @JsonProperty("children")
    public void setChildren(List<String> children) {
        this.children = children;
    }

    public TaxonData withChildren(List<String> children) {
        this.children = children;
        return this;
    }

    @JsonProperty("scientific_lineage")
    public List<String> getScientificLineage() {
        return scientificLineage;
    }

    @JsonProperty("scientific_lineage")
    public void setScientificLineage(List<String> scientificLineage) {
        this.scientificLineage = scientificLineage;
    }

    public TaxonData withScientificLineage(List<String> scientificLineage) {
        this.scientificLineage = scientificLineage;
        return this;
    }

    @JsonProperty("scientific_name")
    public java.lang.String getScientificName() {
        return scientificName;
    }

    @JsonProperty("scientific_name")
    public void setScientificName(java.lang.String scientificName) {
        this.scientificName = scientificName;
    }

    public TaxonData withScientificName(java.lang.String scientificName) {
        this.scientificName = scientificName;
        return this;
    }

    @JsonProperty("taxonomic_id")
    public Long getTaxonomicId() {
        return taxonomicId;
    }

    @JsonProperty("taxonomic_id")
    public void setTaxonomicId(Long taxonomicId) {
        this.taxonomicId = taxonomicId;
    }

    public TaxonData withTaxonomicId(Long taxonomicId) {
        this.taxonomicId = taxonomicId;
        return this;
    }

    @JsonProperty("kingdom")
    public java.lang.String getKingdom() {
        return kingdom;
    }

    @JsonProperty("kingdom")
    public void setKingdom(java.lang.String kingdom) {
        this.kingdom = kingdom;
    }

    public TaxonData withKingdom(java.lang.String kingdom) {
        this.kingdom = kingdom;
        return this;
    }

    @JsonProperty("domain")
    public java.lang.String getDomain() {
        return domain;
    }

    @JsonProperty("domain")
    public void setDomain(java.lang.String domain) {
        this.domain = domain;
    }

    public TaxonData withDomain(java.lang.String domain) {
        this.domain = domain;
        return this;
    }

    @JsonProperty("genetic_code")
    public Long getGeneticCode() {
        return geneticCode;
    }

    @JsonProperty("genetic_code")
    public void setGeneticCode(Long geneticCode) {
        this.geneticCode = geneticCode;
    }

    public TaxonData withGeneticCode(Long geneticCode) {
        this.geneticCode = geneticCode;
        return this;
    }

    @JsonProperty("aliases")
    public List<String> getAliases() {
        return aliases;
    }

    @JsonProperty("aliases")
    public void setAliases(List<String> aliases) {
        this.aliases = aliases;
    }

    public TaxonData withAliases(List<String> aliases) {
        this.aliases = aliases;
        return this;
    }

    /**
     * <p>Original spec-file type: ObjectInfo</p>
     * <pre>
     * * @skip documentation
     * </pre>
     * 
     */
    @JsonProperty("obj_info")
    public ObjectInfo getObjInfo() {
        return objInfo;
    }

    /**
     * <p>Original spec-file type: ObjectInfo</p>
     * <pre>
     * * @skip documentation
     * </pre>
     * 
     */
    @JsonProperty("obj_info")
    public void setObjInfo(ObjectInfo objInfo) {
        this.objInfo = objInfo;
    }

    public TaxonData withObjInfo(ObjectInfo objInfo) {
        this.objInfo = objInfo;
        return this;
    }

    @JsonAnyGetter
    public Map<java.lang.String, Object> getAdditionalProperties() {
        return this.additionalProperties;
    }

    @JsonAnySetter
    public void setAdditionalProperties(java.lang.String name, Object value) {
        this.additionalProperties.put(name, value);
    }

    @Override
    public java.lang.String toString() {
        return ((((((((((((((((((((((("TaxonData"+" [parent=")+ parent)+", children=")+ children)+", scientificLineage=")+ scientificLineage)+", scientificName=")+ scientificName)+", taxonomicId=")+ taxonomicId)+", kingdom=")+ kingdom)+", domain=")+ domain)+", geneticCode=")+ geneticCode)+", aliases=")+ aliases)+", objInfo=")+ objInfo)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
