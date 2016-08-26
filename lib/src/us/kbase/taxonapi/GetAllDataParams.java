
package us.kbase.taxonapi;

import java.util.HashMap;
import java.util.Map;
import javax.annotation.Generated;
import com.fasterxml.jackson.annotation.JsonAnyGetter;
import com.fasterxml.jackson.annotation.JsonAnySetter;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


/**
 * <p>Original spec-file type: GetAllDataParams</p>
 * 
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "ref",
    "include_decorated_scientific_lineage",
    "include_decorated_children"
})
public class GetAllDataParams {

    @JsonProperty("ref")
    private String ref;
    @JsonProperty("include_decorated_scientific_lineage")
    private Long includeDecoratedScientificLineage;
    @JsonProperty("include_decorated_children")
    private Long includeDecoratedChildren;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("ref")
    public String getRef() {
        return ref;
    }

    @JsonProperty("ref")
    public void setRef(String ref) {
        this.ref = ref;
    }

    public GetAllDataParams withRef(String ref) {
        this.ref = ref;
        return this;
    }

    @JsonProperty("include_decorated_scientific_lineage")
    public Long getIncludeDecoratedScientificLineage() {
        return includeDecoratedScientificLineage;
    }

    @JsonProperty("include_decorated_scientific_lineage")
    public void setIncludeDecoratedScientificLineage(Long includeDecoratedScientificLineage) {
        this.includeDecoratedScientificLineage = includeDecoratedScientificLineage;
    }

    public GetAllDataParams withIncludeDecoratedScientificLineage(Long includeDecoratedScientificLineage) {
        this.includeDecoratedScientificLineage = includeDecoratedScientificLineage;
        return this;
    }

    @JsonProperty("include_decorated_children")
    public Long getIncludeDecoratedChildren() {
        return includeDecoratedChildren;
    }

    @JsonProperty("include_decorated_children")
    public void setIncludeDecoratedChildren(Long includeDecoratedChildren) {
        this.includeDecoratedChildren = includeDecoratedChildren;
    }

    public GetAllDataParams withIncludeDecoratedChildren(Long includeDecoratedChildren) {
        this.includeDecoratedChildren = includeDecoratedChildren;
        return this;
    }

    @JsonAnyGetter
    public Map<String, Object> getAdditionalProperties() {
        return this.additionalProperties;
    }

    @JsonAnySetter
    public void setAdditionalProperties(String name, Object value) {
        this.additionalProperties.put(name, value);
    }

    @Override
    public String toString() {
        return ((((((((("GetAllDataParams"+" [ref=")+ ref)+", includeDecoratedScientificLineage=")+ includeDecoratedScientificLineage)+", includeDecoratedChildren=")+ includeDecoratedChildren)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
