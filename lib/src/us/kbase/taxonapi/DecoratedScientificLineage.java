
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
 * <p>Original spec-file type: DecoratedScientificLineage</p>
 * <pre>
 * list starts at the root, and goes on down to this
 * </pre>
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "decorated_scientific_lineage"
})
public class DecoratedScientificLineage {

    @JsonProperty("decorated_scientific_lineage")
    private List<TaxonInfo> decoratedScientificLineage;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("decorated_scientific_lineage")
    public List<TaxonInfo> getDecoratedScientificLineage() {
        return decoratedScientificLineage;
    }

    @JsonProperty("decorated_scientific_lineage")
    public void setDecoratedScientificLineage(List<TaxonInfo> decoratedScientificLineage) {
        this.decoratedScientificLineage = decoratedScientificLineage;
    }

    public DecoratedScientificLineage withDecoratedScientificLineage(List<TaxonInfo> decoratedScientificLineage) {
        this.decoratedScientificLineage = decoratedScientificLineage;
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
        return ((((("DecoratedScientificLineage"+" [decoratedScientificLineage=")+ decoratedScientificLineage)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
