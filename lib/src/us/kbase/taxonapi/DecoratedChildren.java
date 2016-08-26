
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
 * <p>Original spec-file type: DecoratedChildren</p>
 * 
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "decorated_children"
})
public class DecoratedChildren {

    @JsonProperty("decorated_children")
    private List<TaxonInfo> decoratedChildren;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("decorated_children")
    public List<TaxonInfo> getDecoratedChildren() {
        return decoratedChildren;
    }

    @JsonProperty("decorated_children")
    public void setDecoratedChildren(List<TaxonInfo> decoratedChildren) {
        this.decoratedChildren = decoratedChildren;
    }

    public DecoratedChildren withDecoratedChildren(List<TaxonInfo> decoratedChildren) {
        this.decoratedChildren = decoratedChildren;
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
        return ((((("DecoratedChildren"+" [decoratedChildren=")+ decoratedChildren)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
