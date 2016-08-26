
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
 * <p>Original spec-file type: DecoratedLineage</p>
 * <pre>
 * list starts at parent of this, and goes on up to root
 * </pre>
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "lineage"
})
public class DecoratedLineage {

    @JsonProperty("lineage")
    private List<TaxonInfo> lineage;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("lineage")
    public List<TaxonInfo> getLineage() {
        return lineage;
    }

    @JsonProperty("lineage")
    public void setLineage(List<TaxonInfo> lineage) {
        this.lineage = lineage;
    }

    public DecoratedLineage withLineage(List<TaxonInfo> lineage) {
        this.lineage = lineage;
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
        return ((((("DecoratedLineage"+" [lineage=")+ lineage)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
