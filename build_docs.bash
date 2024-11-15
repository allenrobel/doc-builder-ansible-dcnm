export REPO_HOME=$HOME/repos/doc-builder-ansible-dcnm
export DOCS_DOCUMENTATION_DIR=$REPO_HOME/documentation
export DOCS_EXAMPLES_DIR=$REPO_HOME/examples
export DOCS_MAIN_DIR=$REPO_HOME/docs
export DOCS_RETURN_DIR=$REPO_HOME/return

MODULES="dcnm_fabric "
MODULES+="dcnm_image_policy dcnm_image_upgrade dcnm_image_upload dcnm_interface "
MODULES+="dcnm_inventory dcnm_links dcnm_maintenance_mode dcnm_network "
MODULES+="dcnm_policy dcnm_resource_manager dcnm_rest "
MODULES+="dcnm_service_node dcnm_service_policy dcnm_service_route_peering "
MODULES+="dcnm_template dcnm_vpc_pair dcnm_vrf"

# pull down the latest documentation for each module from the
# ansible-dcnm repository
for MODULE in $MODULES; do
    echo "Retrieving Module: $MODULE"
    $REPO_HOME/doc_getter.py --module $MODULE
done

# Create file with main DOCUMENATION section for each module
for MODULE in $MODULES; do
    echo "Processing DOCUMENTATION: $MODULE"
    $REPO_HOME/doc_builder.py $DOCS_DOCUMENTATION_DIR/$MODULE.yaml > $DOCS_MAIN_DIR/$MODULE.md
done

# Append the EXAMPLES section to each module's documentation
for MODULE in $MODULES; do
    echo "Processing EXAMPLES: $MODULE"
    echo "" >> $DOCS_MAIN_DIR/$MODULE.md
    echo "## Examples" >> $DOCS_MAIN_DIR/$MODULE.md
    echo "" >> $DOCS_MAIN_DIR/$MODULE.md
    echo '???+ "Details"' >> $DOCS_MAIN_DIR/$MODULE.md
    echo "" >> $DOCS_MAIN_DIR/$MODULE.md
    cat $DOCS_EXAMPLES_DIR/$MODULE.yaml >> $DOCS_MAIN_DIR/$MODULE.md
done

# Append the RETURN section (if it exists) to each module's documentation
for MODULE in $MODULES; do
    if [ ! -s $DOCS_RETURN_DIR/$MODULE.yaml ]; then
        continue;
    fi
    echo "Processing RETURN: $MODULE"
    echo "" >> $DOCS_MAIN_DIR/$MODULE.md
    echo "## Return" >> $DOCS_MAIN_DIR/$MODULE.md
    echo "" >> $DOCS_MAIN_DIR/$MODULE.md
    echo '???+ "Details"' >> $DOCS_MAIN_DIR/$MODULE.md
    echo "" >> $DOCS_MAIN_DIR/$MODULE.md
    cat $DOCS_RETURN_DIR/$MODULE.yaml >> $DOCS_MAIN_DIR/$MODULE.md
done
