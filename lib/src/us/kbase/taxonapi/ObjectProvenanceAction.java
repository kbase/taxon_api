
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
 * <p>Original spec-file type: ObjectProvenanceAction</p>
 * <pre>
 * * @skip documentation
 * </pre>
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "time",
    "service_name",
    "service_version",
    "service_method",
    "method_parameters",
    "script_name",
    "script_version",
    "script_command_line",
    "input_object_references",
    "validated_object_references",
    "intermediate_input_ids",
    "intermediate_output_ids",
    "external_data",
    "description"
})
public class ObjectProvenanceAction {

    @JsonProperty("time")
    private java.lang.String time;
    @JsonProperty("service_name")
    private java.lang.String serviceName;
    @JsonProperty("service_version")
    private java.lang.String serviceVersion;
    @JsonProperty("service_method")
    private java.lang.String serviceMethod;
    @JsonProperty("method_parameters")
    private List<String> methodParameters;
    @JsonProperty("script_name")
    private java.lang.String scriptName;
    @JsonProperty("script_version")
    private java.lang.String scriptVersion;
    @JsonProperty("script_command_line")
    private java.lang.String scriptCommandLine;
    @JsonProperty("input_object_references")
    private List<String> inputObjectReferences;
    @JsonProperty("validated_object_references")
    private List<String> validatedObjectReferences;
    @JsonProperty("intermediate_input_ids")
    private List<String> intermediateInputIds;
    @JsonProperty("intermediate_output_ids")
    private List<String> intermediateOutputIds;
    @JsonProperty("external_data")
    private List<ExternalDataUnit> externalData;
    @JsonProperty("description")
    private java.lang.String description;
    private Map<java.lang.String, Object> additionalProperties = new HashMap<java.lang.String, Object>();

    @JsonProperty("time")
    public java.lang.String getTime() {
        return time;
    }

    @JsonProperty("time")
    public void setTime(java.lang.String time) {
        this.time = time;
    }

    public ObjectProvenanceAction withTime(java.lang.String time) {
        this.time = time;
        return this;
    }

    @JsonProperty("service_name")
    public java.lang.String getServiceName() {
        return serviceName;
    }

    @JsonProperty("service_name")
    public void setServiceName(java.lang.String serviceName) {
        this.serviceName = serviceName;
    }

    public ObjectProvenanceAction withServiceName(java.lang.String serviceName) {
        this.serviceName = serviceName;
        return this;
    }

    @JsonProperty("service_version")
    public java.lang.String getServiceVersion() {
        return serviceVersion;
    }

    @JsonProperty("service_version")
    public void setServiceVersion(java.lang.String serviceVersion) {
        this.serviceVersion = serviceVersion;
    }

    public ObjectProvenanceAction withServiceVersion(java.lang.String serviceVersion) {
        this.serviceVersion = serviceVersion;
        return this;
    }

    @JsonProperty("service_method")
    public java.lang.String getServiceMethod() {
        return serviceMethod;
    }

    @JsonProperty("service_method")
    public void setServiceMethod(java.lang.String serviceMethod) {
        this.serviceMethod = serviceMethod;
    }

    public ObjectProvenanceAction withServiceMethod(java.lang.String serviceMethod) {
        this.serviceMethod = serviceMethod;
        return this;
    }

    @JsonProperty("method_parameters")
    public List<String> getMethodParameters() {
        return methodParameters;
    }

    @JsonProperty("method_parameters")
    public void setMethodParameters(List<String> methodParameters) {
        this.methodParameters = methodParameters;
    }

    public ObjectProvenanceAction withMethodParameters(List<String> methodParameters) {
        this.methodParameters = methodParameters;
        return this;
    }

    @JsonProperty("script_name")
    public java.lang.String getScriptName() {
        return scriptName;
    }

    @JsonProperty("script_name")
    public void setScriptName(java.lang.String scriptName) {
        this.scriptName = scriptName;
    }

    public ObjectProvenanceAction withScriptName(java.lang.String scriptName) {
        this.scriptName = scriptName;
        return this;
    }

    @JsonProperty("script_version")
    public java.lang.String getScriptVersion() {
        return scriptVersion;
    }

    @JsonProperty("script_version")
    public void setScriptVersion(java.lang.String scriptVersion) {
        this.scriptVersion = scriptVersion;
    }

    public ObjectProvenanceAction withScriptVersion(java.lang.String scriptVersion) {
        this.scriptVersion = scriptVersion;
        return this;
    }

    @JsonProperty("script_command_line")
    public java.lang.String getScriptCommandLine() {
        return scriptCommandLine;
    }

    @JsonProperty("script_command_line")
    public void setScriptCommandLine(java.lang.String scriptCommandLine) {
        this.scriptCommandLine = scriptCommandLine;
    }

    public ObjectProvenanceAction withScriptCommandLine(java.lang.String scriptCommandLine) {
        this.scriptCommandLine = scriptCommandLine;
        return this;
    }

    @JsonProperty("input_object_references")
    public List<String> getInputObjectReferences() {
        return inputObjectReferences;
    }

    @JsonProperty("input_object_references")
    public void setInputObjectReferences(List<String> inputObjectReferences) {
        this.inputObjectReferences = inputObjectReferences;
    }

    public ObjectProvenanceAction withInputObjectReferences(List<String> inputObjectReferences) {
        this.inputObjectReferences = inputObjectReferences;
        return this;
    }

    @JsonProperty("validated_object_references")
    public List<String> getValidatedObjectReferences() {
        return validatedObjectReferences;
    }

    @JsonProperty("validated_object_references")
    public void setValidatedObjectReferences(List<String> validatedObjectReferences) {
        this.validatedObjectReferences = validatedObjectReferences;
    }

    public ObjectProvenanceAction withValidatedObjectReferences(List<String> validatedObjectReferences) {
        this.validatedObjectReferences = validatedObjectReferences;
        return this;
    }

    @JsonProperty("intermediate_input_ids")
    public List<String> getIntermediateInputIds() {
        return intermediateInputIds;
    }

    @JsonProperty("intermediate_input_ids")
    public void setIntermediateInputIds(List<String> intermediateInputIds) {
        this.intermediateInputIds = intermediateInputIds;
    }

    public ObjectProvenanceAction withIntermediateInputIds(List<String> intermediateInputIds) {
        this.intermediateInputIds = intermediateInputIds;
        return this;
    }

    @JsonProperty("intermediate_output_ids")
    public List<String> getIntermediateOutputIds() {
        return intermediateOutputIds;
    }

    @JsonProperty("intermediate_output_ids")
    public void setIntermediateOutputIds(List<String> intermediateOutputIds) {
        this.intermediateOutputIds = intermediateOutputIds;
    }

    public ObjectProvenanceAction withIntermediateOutputIds(List<String> intermediateOutputIds) {
        this.intermediateOutputIds = intermediateOutputIds;
        return this;
    }

    @JsonProperty("external_data")
    public List<ExternalDataUnit> getExternalData() {
        return externalData;
    }

    @JsonProperty("external_data")
    public void setExternalData(List<ExternalDataUnit> externalData) {
        this.externalData = externalData;
    }

    public ObjectProvenanceAction withExternalData(List<ExternalDataUnit> externalData) {
        this.externalData = externalData;
        return this;
    }

    @JsonProperty("description")
    public java.lang.String getDescription() {
        return description;
    }

    @JsonProperty("description")
    public void setDescription(java.lang.String description) {
        this.description = description;
    }

    public ObjectProvenanceAction withDescription(java.lang.String description) {
        this.description = description;
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
        return ((((((((((((((((((((((((((((((("ObjectProvenanceAction"+" [time=")+ time)+", serviceName=")+ serviceName)+", serviceVersion=")+ serviceVersion)+", serviceMethod=")+ serviceMethod)+", methodParameters=")+ methodParameters)+", scriptName=")+ scriptName)+", scriptVersion=")+ scriptVersion)+", scriptCommandLine=")+ scriptCommandLine)+", inputObjectReferences=")+ inputObjectReferences)+", validatedObjectReferences=")+ validatedObjectReferences)+", intermediateInputIds=")+ intermediateInputIds)+", intermediateOutputIds=")+ intermediateOutputIds)+", externalData=")+ externalData)+", description=")+ description)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
