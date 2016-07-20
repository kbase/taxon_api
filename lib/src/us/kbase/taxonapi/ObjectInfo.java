
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
 * <p>Original spec-file type: ObjectInfo</p>
 * <pre>
 * * @skip documentation
 * </pre>
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "object_id",
    "object_name",
    "object_reference",
    "object_reference_versioned",
    "type_string",
    "save_date",
    "version",
    "saved_by",
    "workspace_id",
    "workspace_name",
    "object_checksum",
    "object_size",
    "object_metadata"
})
public class ObjectInfo {

    @JsonProperty("object_id")
    private Long objectId;
    @JsonProperty("object_name")
    private java.lang.String objectName;
    @JsonProperty("object_reference")
    private java.lang.String objectReference;
    @JsonProperty("object_reference_versioned")
    private java.lang.String objectReferenceVersioned;
    @JsonProperty("type_string")
    private java.lang.String typeString;
    @JsonProperty("save_date")
    private java.lang.String saveDate;
    @JsonProperty("version")
    private Long version;
    @JsonProperty("saved_by")
    private java.lang.String savedBy;
    @JsonProperty("workspace_id")
    private Long workspaceId;
    @JsonProperty("workspace_name")
    private java.lang.String workspaceName;
    @JsonProperty("object_checksum")
    private java.lang.String objectChecksum;
    @JsonProperty("object_size")
    private Long objectSize;
    @JsonProperty("object_metadata")
    private Map<String, String> objectMetadata;
    private Map<java.lang.String, Object> additionalProperties = new HashMap<java.lang.String, Object>();

    @JsonProperty("object_id")
    public Long getObjectId() {
        return objectId;
    }

    @JsonProperty("object_id")
    public void setObjectId(Long objectId) {
        this.objectId = objectId;
    }

    public ObjectInfo withObjectId(Long objectId) {
        this.objectId = objectId;
        return this;
    }

    @JsonProperty("object_name")
    public java.lang.String getObjectName() {
        return objectName;
    }

    @JsonProperty("object_name")
    public void setObjectName(java.lang.String objectName) {
        this.objectName = objectName;
    }

    public ObjectInfo withObjectName(java.lang.String objectName) {
        this.objectName = objectName;
        return this;
    }

    @JsonProperty("object_reference")
    public java.lang.String getObjectReference() {
        return objectReference;
    }

    @JsonProperty("object_reference")
    public void setObjectReference(java.lang.String objectReference) {
        this.objectReference = objectReference;
    }

    public ObjectInfo withObjectReference(java.lang.String objectReference) {
        this.objectReference = objectReference;
        return this;
    }

    @JsonProperty("object_reference_versioned")
    public java.lang.String getObjectReferenceVersioned() {
        return objectReferenceVersioned;
    }

    @JsonProperty("object_reference_versioned")
    public void setObjectReferenceVersioned(java.lang.String objectReferenceVersioned) {
        this.objectReferenceVersioned = objectReferenceVersioned;
    }

    public ObjectInfo withObjectReferenceVersioned(java.lang.String objectReferenceVersioned) {
        this.objectReferenceVersioned = objectReferenceVersioned;
        return this;
    }

    @JsonProperty("type_string")
    public java.lang.String getTypeString() {
        return typeString;
    }

    @JsonProperty("type_string")
    public void setTypeString(java.lang.String typeString) {
        this.typeString = typeString;
    }

    public ObjectInfo withTypeString(java.lang.String typeString) {
        this.typeString = typeString;
        return this;
    }

    @JsonProperty("save_date")
    public java.lang.String getSaveDate() {
        return saveDate;
    }

    @JsonProperty("save_date")
    public void setSaveDate(java.lang.String saveDate) {
        this.saveDate = saveDate;
    }

    public ObjectInfo withSaveDate(java.lang.String saveDate) {
        this.saveDate = saveDate;
        return this;
    }

    @JsonProperty("version")
    public Long getVersion() {
        return version;
    }

    @JsonProperty("version")
    public void setVersion(Long version) {
        this.version = version;
    }

    public ObjectInfo withVersion(Long version) {
        this.version = version;
        return this;
    }

    @JsonProperty("saved_by")
    public java.lang.String getSavedBy() {
        return savedBy;
    }

    @JsonProperty("saved_by")
    public void setSavedBy(java.lang.String savedBy) {
        this.savedBy = savedBy;
    }

    public ObjectInfo withSavedBy(java.lang.String savedBy) {
        this.savedBy = savedBy;
        return this;
    }

    @JsonProperty("workspace_id")
    public Long getWorkspaceId() {
        return workspaceId;
    }

    @JsonProperty("workspace_id")
    public void setWorkspaceId(Long workspaceId) {
        this.workspaceId = workspaceId;
    }

    public ObjectInfo withWorkspaceId(Long workspaceId) {
        this.workspaceId = workspaceId;
        return this;
    }

    @JsonProperty("workspace_name")
    public java.lang.String getWorkspaceName() {
        return workspaceName;
    }

    @JsonProperty("workspace_name")
    public void setWorkspaceName(java.lang.String workspaceName) {
        this.workspaceName = workspaceName;
    }

    public ObjectInfo withWorkspaceName(java.lang.String workspaceName) {
        this.workspaceName = workspaceName;
        return this;
    }

    @JsonProperty("object_checksum")
    public java.lang.String getObjectChecksum() {
        return objectChecksum;
    }

    @JsonProperty("object_checksum")
    public void setObjectChecksum(java.lang.String objectChecksum) {
        this.objectChecksum = objectChecksum;
    }

    public ObjectInfo withObjectChecksum(java.lang.String objectChecksum) {
        this.objectChecksum = objectChecksum;
        return this;
    }

    @JsonProperty("object_size")
    public Long getObjectSize() {
        return objectSize;
    }

    @JsonProperty("object_size")
    public void setObjectSize(Long objectSize) {
        this.objectSize = objectSize;
    }

    public ObjectInfo withObjectSize(Long objectSize) {
        this.objectSize = objectSize;
        return this;
    }

    @JsonProperty("object_metadata")
    public Map<String, String> getObjectMetadata() {
        return objectMetadata;
    }

    @JsonProperty("object_metadata")
    public void setObjectMetadata(Map<String, String> objectMetadata) {
        this.objectMetadata = objectMetadata;
    }

    public ObjectInfo withObjectMetadata(Map<String, String> objectMetadata) {
        this.objectMetadata = objectMetadata;
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
        return ((((((((((((((((((((((((((((("ObjectInfo"+" [objectId=")+ objectId)+", objectName=")+ objectName)+", objectReference=")+ objectReference)+", objectReferenceVersioned=")+ objectReferenceVersioned)+", typeString=")+ typeString)+", saveDate=")+ saveDate)+", version=")+ version)+", savedBy=")+ savedBy)+", workspaceId=")+ workspaceId)+", workspaceName=")+ workspaceName)+", objectChecksum=")+ objectChecksum)+", objectSize=")+ objectSize)+", objectMetadata=")+ objectMetadata)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
