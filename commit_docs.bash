REPO_HOME=$HOME/repos/doc-builder-ansible-dcnm
DOC_HOME=$REPO_HOME/docs

DOCPOC_MODULES_HOME=$HOME/repos/dcnm-docpoc/docs/modules/

MODULES="dcnm_fabric "
MODULES+="dcnm_image_policy dcnm_image_upgrade dcnm_image_upload dcnm_interface "
MODULES+="dcnm_inventory dcnm_links dcnm_maintenance_mode dcnm_network "
MODULES+="dcnm_policy dcnm_resource_manager dcnm_rest "
MODULES+="dcnm_service_node dcnm_service_policy dcnm_service_route_peering "
MODULES+="dcnm_template dcnm_vpc_pair dcnm_vrf"

for MODULE in $MODULES; do
    echo "Committing $MODULE"
    cp $DOC_HOME/$MODULE.md $DOCPOC_MODULES_HOME/$MODULE.md
done
