export REPO_HOME=$HOME/repos/doc-builder-ansible-dcnm
export YAML_HOME=$REPO_HOME/yaml
export EXAMPLES_HOME=$REPO_HOME/examples
export DOC_HOME=$REPO_HOME/docs

MODULES="dcnm_fabric "
MODULES+="dcnm_image_policy dcnm_image_upgrade dcnm_image_upload dcnm_interface "
MODULES+="dcnm_inventory dcnm_links dcnm_maintenance_mode dcnm_network "
MODULES+="dcnm_policy dcnm_resource_manager dcnm_rest "
MODULES+="dcnm_service_node dcnm_service_policy dcnm_service_route_peering "
MODULES+="dcnm_template dcnm_vpc_pair dcnm_vrf"

for MODULE in $MODULES; do
    echo "Retrieving Module: $MODULE"
    $REPO_HOME/doc_getter.py $MODULE
done

for MODULE in $MODULES; do
    echo "Processing DOCUMENTATION: $MODULE"
    $REPO_HOME/doc_builder.py $YAML_HOME/$MODULE.yaml > $DOC_HOME/$MODULE.md
done

for MODULE in $MODULES; do
    echo "Processing EXAMPLES: $MODULE"
    echo "" >> $DOC_HOME/$MODULE.md
    echo "## Examples" >> $DOC_HOME/$MODULE.md
    echo "" >> $DOC_HOME/$MODULE.md
    echo '???+ "Details"' >> $DOC_HOME/$MODULE.md
    echo "" >> $DOC_HOME/$MODULE.md
    cat $EXAMPLES_HOME/$MODULE.yaml >> $DOC_HOME/$MODULE.md
done
